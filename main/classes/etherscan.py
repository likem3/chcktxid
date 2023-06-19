import requests
from main.settings import HANDLER_CONFIG
import sys
import time

class EtherScan:
    response_api = {}
    result = {}

    def __init__(self, txid):
        self.config = HANDLER_CONFIG.get('etherscan', {}) 
        self.base_url = self.config.get('api_url', '')
        self.params = {
            'module': 'transaction',
            'action': 'gettxreceiptstatus',
            'txhash': txid,
            'apikey': self.config.get('api_key', '')
        }
        self.pre_request()

    def pre_request(self):
        self.validate()

    def validate(self):
        if not self.base_url or not self.params.get('txhash', '') or not self.params.get('apikey'):
            sys.exit()

    def execute(self):
        response_api = requests.request('GET', self.base_url, params=self.params)
        time.sleep(1/3)
        self.response_api = response_api.json()
        self.check_status(self.response_api)
    
    def check_status(self, resp):
        result = resp.get('result', {})
        if result and result.get('status') == "1":
            self.result = {
                'trx_status': "success",
                'api_data': resp
            }
        elif result and result.get('status') == "0":
            self.result = {
                'trx_status': "failed",
                'api_data': resp
            }
        else:
            self.result = {
                'trx_status': "invalid",
                'api_data': resp
            }