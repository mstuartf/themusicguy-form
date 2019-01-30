import json

from flask_cors import CORS
from flask import Flask, jsonify, request

from send_email import send_receipt_confirmation, forward_customer_enquiry


app = Flask(__name__)


cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/send_message', methods=["POST"])
def send_email_endpoint():

    data = json.loads(request.data)
    
    send_receipt_confirmation(
        data['name'], 
        data['email_address']
    )

    forward_customer_enquiry(
        data['name'], 
        data['email_address'],
        data['message']
    )
    
    return jsonify({"message": "Message sent!"})
