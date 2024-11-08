from django.shortcuts import render
from .models import Portfolio
from .serializer import PortfolioSerializer
from rest_framework import viewsets


class PortflioView(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

# Create your views here.
