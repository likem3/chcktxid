from drf_yasg import openapi
check_tron_schema = {
    "200": openapi.Response(
        description="valid success transactions",
        examples={
            "application/json": {
                "trx_valid": "boolean",
                "trx_status": "string",
                "api_data": {
                    "icon_url": "string",
                    "symbol": "string",
                    "level": "string",
                    "to_address": "string",
                    "contract_address": "string",
                    "type": "string",
                    "decimals": "integer",
                    "name": "string",
                    "vip": "boolean",
                    "tokenType": "string",
                    "from_address": "string",
                    "amount_str": "decimal",
                    "status": "integer"
                }
            }
        }
    )
}

check_ether_schema = {
    "200": openapi.Response(
        description="valid success transactions",
        examples={
            "application/json": {
                "trx_status": "string",
                "api_data": "json"
            }
        }
    )
}

check_bsc_schema = {
    "200": openapi.Response(
        description="valid success transactions",
        examples={
            "application/json": {
                "trx_status": "string",
                "api_data": "json"
            }
        }
    )
}
