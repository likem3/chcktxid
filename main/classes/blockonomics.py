import requests
from main.settings import HANDLER_CONFIG
import sys
import time
from decimal import Decimal

class BlockConomics:
    response_api = {}
    result = {}
    txid = None
    from_address = None
    to_address = None
    amount = None
    trx_data = {}

    def __init__(self, txid, from_address, to_address, amount):
        self.txid = txid
        self.from_address = from_address
        self.to_address = to_address
        self.amount = amount
        self.config = HANDLER_CONFIG.get('blockonomics', {})
        self.base_url = self.config.get('api_url', '')
        self.params_path = txid
        self.pre_request()

    def pre_request(self):
        self.validate()

    def validate(self):
        if not self.base_url or not self.params_path:
            sys.exit()

    def execute(self):
        params = {
            'txid': self.txid
        }
        response_api = requests.request('GET', self.base_url, params=params)
        time.sleep(1/3)
        self.response_api = response_api.json()
        self.trx_data = self.validate_response(self.response_api)
        self.check_status(self.response_api)


    def get_trx_status(self, status):
        status_dict = {
            'Confirmed': 'success',
            'Unconfirmed': 'pendding',
        }

        return status_dict[status] if status_dict[status] else 'invalid'

    def validate_response(self, resp):
        try:
            in_obj = resp['vin'][0]
            out_obj = resp['vout'][0]
            breakpoint()
            if out_obj['address'] != self.to_address or out_obj['value']/Decimal('1e8') != Decimal(self.amount) or in_obj['address'] != self.from_address:
                return {
                    'status': 'Invalid'
                }
            
            return {
                'status': resp['status'],
                'to_address': out_obj['address'],
                'amount_recieve': out_obj['value']/Decimal('1e8'),
                'from_address': in_obj['address'],
                'amount_send': in_obj['value']/Decimal('1e8')
            }

        except Exception as e:
            return {
                'status': 'Invalid'
            }


    def check_status(self, resp):
        try:
            if self.trx_data['status'] != 'Invalid':
                self.result = {
                    'trx_valid': True if self.trx_data['status'] != 'Invalid' else False,
                    'trx_status': self.get_trx_status(self.trx_data['status']),
                    'api_data': self.trx_data
                }
            else:
                self.result = {
                    'trx_status': 'invalid',
                    'api_data': resp
                } 
               
        except Exception as e:
            self.result = {
                'trx_status': 'invalid',
                'api_data': resp
            }

