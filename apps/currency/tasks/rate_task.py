from apps.currency.models import Currency, Rate
from django.shortcuts import render
from django.conf import settings
import requests
import json

class RateTask:

    def __init__(self, currency):
        self.currency = currency 

    def get_rate(self):

        qs = Currency.objects.all().values_list('code', flat=True)
        url = 'http://api.currencylayer.com/live?access_key=%s&currencies=%s&format=1' % (settings.ACCESS_KEY, ','.join( list(qs) ))

        r = requests.get(url)

        result = json.loads(r.text)

        for q in result['quotes']:
            code = q[3:]
            currency = Currency.objects.filter(code=code).first()

            if currency:
                rate = Rate.objects.create(currency=currency, rate=result['quotes'][q])
