from drf_yasg import openapi
check_tron_schema = {
    "200": openapi.Response(
        description="valid success transactions",
        examples={
            "application/json": {
                "status": "boolean",
                "confirmed": "boolean",
                "confirmations": "integer",
                "trx_info": 
                    {
                        "from": "string",
                        "to": "string",
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
