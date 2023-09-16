from rest_framework import serializers

from main.models import CurrencyRate


class CurrencyRateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = ('currency', 'rate')
