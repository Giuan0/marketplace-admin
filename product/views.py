from rest_framework.decorators import action

from store.models import Store
from rest_framework import viewsets
from rest_framework.response import Response
import json

from .models import Product
from .serializers import ProductSerializer


class StoreProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #Detail=True lets you get a argument, ex: products/{pk}/test
    @action(methods=['get'], detail=False, url_path='teste', url_name='teste')
    def teste(self, request, pk=None):
        return Response({"data": "Teste"})

    def retrieve(self, request, *args, pk=None):
        store_products = Product.objects.filter(store_id=pk)
        print(store_products)
        serialized_store_products = self.get_serializer(store_products, many=True).data
        return Response(serialized_store_products)

    def create(self, request, *args, **kwargs):
        body = json.loads(request.body.decode('utf-8'))
        store_id = body['store_id']

        store = Store.objects.get(id=store_id)
        Product.objects.create(store=store,
                               name=body['name'],
                               price=body['price'],
                               quantity=body['quantity'])

        return Response({"data": "Product successfully created!"})

    def list(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
