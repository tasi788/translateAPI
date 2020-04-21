import json
import uuid
from configparser import ConfigParser

import requests
from googletrans import Translator

config = ConfigParser()
config.read('../config.cfg')


class Translate:
    def __init__(self):
        self.result_list = list()

    def google(self, input_text):
        translator = Translator()
        result = translator.translate(input_text, dest='zh-tw')
        tmp = {'provider': 'Google', 'status': True, 'result': result.text}
        self.result_list.append(tmp)

    def bing(self, input_text):
        subscription_key = config.get('bing', 'secret')
        constructed_url = config.get('bing', 'endpoint')

        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Content-type': 'application/json',
            'Accept-Language': 'zh-Hant',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        body = [{'text': input_text}]
        request = requests.post(constructed_url, headers=headers, json=body)
        response = request.json()[0]['translations'][0]['text']
        tmp = {'provider': 'Bing', 'status': True, 'result': response}
        self.result_list.append(tmp)
