CRYPTO_CURRENCIES = (
    ('BTC', 'BTC'),
    ('ETH', 'ETH'),
    ('USDT', 'USDT'),
    ('LUNA', 'LUNA')
)

TOKENS = {
    'TRC20': 'TRC20',
    'ERC20': 'ERC20',
    'BEP20': 'BEP20',
    'WBTC': 'WBTC',
    'BTCT': 'BTCT',
    'RenBTC': 'RenBTC'
}

HANDLER_CONFIG = {
    'tronscan': {
        'api_url': 'https://apilist.tronscanapi.com/api/transaction-info',
        'api_key': '',
    },
    'etherscan': {
        'api_url': 'https://api.etherscan.io/api',
        'api_key': '',
    },
    'bscscan': {
        'api_url': 'https://api.bscscan.com/api',
        'api_key': '',
    },
    'blockstream': {
        'api_url': 'https://blockstream.info/api/tx/',
        'api_key': '',
    },
}