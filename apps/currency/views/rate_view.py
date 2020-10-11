from apps.currency.serializers import RateSerializer
from apps.currency.models import Rate
from rest_framework import viewsets

# ViewSets define the view behavior.
class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

