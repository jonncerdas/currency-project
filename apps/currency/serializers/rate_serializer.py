from apps.currency.models import Rate
from rest_framework import serializers

class RateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rate
        fields = ['rate']
