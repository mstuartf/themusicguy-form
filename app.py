import os
import json

import boto3

from flask_cors import CORS
from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

client = boto3.client('ses', region_name="eu-west-1")


SENDER_EMAIL = 'mstuartflood@gmail.com'
RECIPIENT_EMAIL = 'mstuartflood@gmail.com'


@app.route('/new_enquiry', methods=["POST"])
def send_email_endpoint():

	data = json.loads(request.data)

	send_email(
        RECIPIENT_EMAIL,
        "/new_enquiry payload",
        json.dumps(data, indent=2)
    )
	
	return jsonify({"message": "Message sent!"})


def send_email(recipient, subject, body_text):

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
        Source="/new_enquiry payload <{}>".format(SENDER_EMAIL)
    )

    return response['MessageId']

