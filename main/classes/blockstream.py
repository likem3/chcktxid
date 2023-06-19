import requests
from main.settings import HANDLER_CONFIG
import sys
import time

class BlockStream:
    response_api = {}
    result = {}

    def __init__(self, txid):
        self.config = HANDLER_CONFIG.get('blockstream', {}) 
        self.base_url = self.config.get('api_url', '')
        self.params_path = txid
        self.pre_request()

    def pre_request(self):
        self.validate()

    def validate(self):
        if not self.base_url or not self.params_path:
            sys.exit()

    def execute(self):
        furl = self.base_url + self.params_path
        response_api = requests.request('GET', furl)
        time.sleep(1/3)
        self.response_api = response_api.json()
        self.check_status(self.response_api)

    def check_status(self, resp):
        try:
            self.result = {
                'trx_status': 'success' if resp['status']['confirmed'] == True else 'pending',
                'api_data': resp
            }
        except Exception as e:
            self.result = {
                'trx_status': 'invalid',
                'api_data': resp
            }

