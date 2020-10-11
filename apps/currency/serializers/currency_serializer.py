from apps.currency.models import Currency
from rest_framework import serializers

class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = ['code']

