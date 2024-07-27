from django.shortcuts import render
from rest_framework import viewsets

from .models import Dacha
from .serializers import DachaSerializer


# Create your views here.


class DachaViewSet(viewsets.ModelViewSet):
    queryset = Dacha.objects.all()
    serializer_class = DachaSerializer

