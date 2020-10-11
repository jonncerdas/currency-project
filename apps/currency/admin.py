from django.contrib import admin
from apps.currency.models import Currency, Rate

admin.site.register(Currency)
admin.site.register(Rate)
