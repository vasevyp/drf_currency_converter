import requests
from rest_framework import viewsets

from .serializers import CurrencyRateSerializer
from main.models import CurrencyRate


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = CurrencyRate.objects.all()
    my_currency = 'RUB'
    currency_rate_list = ['RUB', 'USD', 'EUR', 'CNY', 'JPY']
    CurrencyRate.objects.all().delete()
    for currency in currency_rate_list:
        rate = requests.get(
            f"https://open.er-api.com/v6/latest/{currency}").json()['rates'][f'{my_currency}']
        print(f'1{currency} = {round(rate,2)} {my_currency}')
        CurrencyRate.objects.create(
            currency=currency, rate=rate)
    serializer_class = CurrencyRateSerializer
