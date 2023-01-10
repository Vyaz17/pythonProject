from rest_framework import generics

from currency.models import Rate
from API.serializer import RateSerializer


class API_Rate_View(generics.ListAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class API_Rate_Details_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
