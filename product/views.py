from django.conf.urls import url, include
from .models import Product
from rest_framework import routers, viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer