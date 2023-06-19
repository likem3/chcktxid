import requests
from main.settings import HANDLER_CONFIG
import sys
import time

class TronScan:
    response_api = {}
    result = {}

    def __init__(self, txid):
        self.config = HANDLER_CONFIG.get('tronscan', {}) 
        self.base_url = self.config.get('api_url', '')
        self.params = {'hash': txid}
        self.header = {'TRON-PRO-API-KEY': self.config.get('api_key', '')}
        self.pre_request()

    def pre_request(self):
        self.validate()

    def validate(self):
        if not self.base_url or not self.params.get('hash', '') or not self.header.get('TRON-PRO-API-KEY'):
            sys.exit()

    def execute(self):
        response_api = requests.request('GET', self.base_url, headers=self.header, params=self.params)
        time.sleep(1/3)
        self.response_api = response_api.json()
        self.check_status(self.response_api)

    def check_status(self, resp):
        try:
            self.result = {
                'trx_status': 'success' if resp['confirmed'] == True else 'pending',
                'api_data': resp
            }
        except Exception as e:
            self.result = {
                'trx_status': 'invalid',
                'api_data': resp
            }

