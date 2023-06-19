from django.urls import path
from main.views import CheckTronViewSet, CheckEtherViewSet, CheckBscViewSet, CheckBtcViewSet

urlpatterns = [
    path('check-tron/', CheckTronViewSet.as_view()),
    path('check-ether/', CheckEtherViewSet.as_view()),
    path('check-bsc/', CheckBscViewSet.as_view()),
    path('check-btc/', CheckBtcViewSet.as_view()),
]