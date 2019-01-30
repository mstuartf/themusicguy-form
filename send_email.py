import os
import boto3

# set environment variable when testing locally
# os.environ['TMG_EMAIL'] = ''

client = boto3.client('ses', region_name="eu-west-1")


def send_email(recipient, subject, body_text):

    print 'Sending email from {} to {} with subject {}'.format(os.environ.get('TMG_EMAIL'), recipient, subject)

    response = client.send_email(
        Destination={
            'ToAddresses': [
                recipient,
            ],
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': "UTF-8",
                    'Data': body_text,
                },
            },
            'Subject': {
                'Charset': "UTF-8",
                'Data': subject,
            },
        },
        Source="The Music Guy <{}>".format(os.environ.get('TMG_EMAIL'))
    )

    return response['MessageId']


def send_receipt_confirmation(name, email_address):
    return send_email(
        email_address,
        "Thanks for your enquiry!",
        "Hi {},\n\nThanks for your enquiry.\n\nI'll be in touch soon!\n\nKind regards,\n\nTim\n\nThe Music Guy\n07805 305 001\nthemusicguy.co.uk".format(name)
    )


def forward_customer_enquiry(name, email_address, message):
    return send_email(
        os.environ.get('TMG_EMAIL'),
        "New TMG enquiry!",
        "Hi Tim,\n\nYou've had a new enquiry from themusicguy.co.uk:\n\nName: {}\n\nEmail: {}\n\nMessage: {}\n\nKind regards,\n\nTMG\n".format(name, email_address, message)
    )


