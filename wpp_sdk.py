
from flask import Flask, jsonify
# import requests
from dotenv import load_dotenv
import os
import logging

app = Flask(__name__)

class WppMessage:
    def __init__(
            self, 
            from_,
            to_,
            type_,
            recipient_type,
            messaging_product='whatsapp'
            
    ):
        self.from_ = from_
        self.to_ = to_
        self.type_ = type_,
        self.messaging_product = messaging_product
        self.recipient_type = recipient_type

class WppTextMessage(WppMessage):
    def __init__(self, from_, to_, text):
        super().__init__(
            from_=from_,
            to_=to_,
            type='text',
            recipient_type='individual'
        )
        self.text = text
        

class WhatAppSDK:
    def __init__(self):
        load_dotenv()

        self.logger = logging.getLogger(__name__)
        
        self.WHATSAPP_API_VERSION=os.getenv('WHATSAPP_API_VERSION')
        self.WHATSAPP_API_TOKEN = f'Bearer {os.getenv('WHATSAPP_API_TOKEN')}'
        self.WHATSAPP_TEST_NUMBER_ID = os.getenv('WHATSAPP_TEST_NUMBER_ID')
        self.WHATSAPP_URL = f'https://graph.facebook.com/{self.WHATSAPP_API_VERSION}/{self.WHATSAPP_TEST_NUMBER_ID}/messages'

    @app.route('/webhook', methods=['GET'])
    async def webhook(self, request):

        self.logger.info(f'==========\nIncoming webwook message\n==========\n\n')
        self.logger.info(f'msg body:\n{jsonify(request['body'])}')

        # Aceita apenas mensagens do tipo text
        if request['body']['type'] != 'text':
            return jsonify(
                'Endpoint aceita, por enquanto, apenas mensagens do tipo texto.',
                status=400,
                
            )
        
        msg_raw = dict(request['body']['text'])

    def _send_typing_indicator(self):
        # url = f'https://api.twilio.com/2010-04-01/Accounts/{ACCOUNT_SID}/Messages.json'
        # payload = {
        #     'From': f'whatsapp:{WHATSAPP_NUMBER}',
        #     'To': f'whatsapp:{to}',
        #     'StatusCallback': 'typing_on'
        # }
        # response = requests.post(url, data=payload, auth=HTTPBasicAuth(ACCOUNT_SID, AUTH_TOKEN))
        # return response.json()
        raise NotImplementedError
    
    def send_message(self, receipt_number, message=''):
        # headers = {
        #     'Authorization': self.WHATSAPP_API_TOKEN,
        #     'Content-Type': 'application/json'
        # }
        # data = {
        #     'messaging_product': 'whatsapp',
        #     'to': receipt_number,
        #     'type': 'template',
        #     'template': {
        #         'name': 'hello_world',
        #         'language': {
        #             'code': 'pt_BR'
        #         }
        #     }
        # }

        # data = json.dumps(data)
        
        # return requests.post(
        #     url=self.WHATSAPP_URL,
        #     headers=headers,
        #     data=data
        # )
        raise NotImplementedError


    async def process_message(self, message):
        raise NotImplementedError


if __name__ == '__main__':
    app.run()