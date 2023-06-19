from rest_framework.views import APIView
from rest_framework.response import Response 
from main.serializers import CheckTXIDSerializer
from main.classes.tronscan import TronScan
from main.classes.etherscan import EtherScan
from main.classes.bscscan import BscScan
from main.classes.blockonomics import BlockConomics
from drf_yasg.utils import swagger_auto_schema
from main.schemas import check_tron_schema, check_ether_schema, check_bsc_schema


class CheckTronViewSet(APIView):
    @swagger_auto_schema(
        request_body=CheckTXIDSerializer, 
        operation_summary="check transaction status of tron network",
        responses=check_tron_schema
    )
    def post(self, request):
        serializer = CheckTXIDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        trons_data = TronScan(**serializer.data)
        trons_data.execute()
        
        return Response(trons_data.result)


class CheckEtherViewSet(APIView):
    @swagger_auto_schema(
        request_body=CheckTXIDSerializer, 
        operation_summary="check transaction status of ether network",
        responses=check_ether_schema
    )
    def post(self, request):
        serializer = CheckTXIDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ether_data = EtherScan(serializer.data.get('txid'))
        ether_data.execute()
        
        return Response(ether_data.result)


class CheckBscViewSet(APIView):
    @swagger_auto_schema(
        request_body=CheckTXIDSerializer, 
        operation_summary="check transaction status of bsc network",
        responses=check_bsc_schema
    )
    def post(self, request):
        serializer = CheckTXIDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        bsc_data = BscScan(serializer.data.get('txid'))
        bsc_data.execute()
        
        return Response(bsc_data.result)
    
class CheckBtcViewSet(APIView):
    @swagger_auto_schema(
        request_body=CheckTXIDSerializer, 
        operation_summary="check transaction status of btc maiinet",
        responses=check_bsc_schema
    )
    def post(self, request):
        serializer = CheckTXIDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        btc_data = BlockConomics(**serializer.data)
        btc_data.execute()
        
        return Response(btc_data.result)

