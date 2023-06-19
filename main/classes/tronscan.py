import requests
from main.settings import HANDLER_CONFIG
import sys
import time
from decimal import Decimal


class TronScan:
    response_api = {}
    result = {}
    trx_data = {}
    txid = None
    from_address = None
    to_address = None
    amount = None

    def __init__(self, txid, from_address, to_address, amount):
        self.txid = txid
        self.from_address = from_address
        self.to_address = to_address
        self.amount = amount
        self.config = HANDLER_CONFIG.get('tronscan', {}) 
        self.base_url = self.config.get('api_url', '')
        self.pre_request()

    def pre_request(self):
        self.validate()

    def validate(self):
        if not self.base_url or not self.txid:
            sys.exit()

    def get_transaction_data(self, resp):
        try:
            data = resp['tokenTransferInfo']
            if data['from_address'] != self.from_address \
                or data['to_address'] != self.to_address \
                or int(data['amount_str'])/Decimal('1e{}'.format(data['decimals'])) != Decimal(self.amount):
                return {}
            data['amount_str'] = '{:.5f}'.format(float(int(data['amount_str'])/Decimal('1e{}'.format(data['decimals']))))
            return data
        except Exception as e:
            return {}

    def execute(self):
        response_api = requests.request('GET', self.base_url, params={'hash': self.txid})
        time.sleep(1/3)
        self.response_api = response_api.json()
        self.trx_data = self.get_transaction_data(self.response_api)
        self.check_status(self.response_api)

    def check_status(self, resp):
        try:
            self.result = {
                'trx_valid': True if self.trx_data else False,
                'trx_status': 'success' if resp['confirmed'] == True else 'pending',
                'api_data': self.trx_data
            }
        except Exception as e:
            self.result = {
                'trx_valid': False,
                'trx_status': 'invalid',
                'api_data': resp
            }

