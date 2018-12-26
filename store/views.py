from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets
import json

from .models import Store
from .serializers import StoreSerializer


class StoreView(viewsets.ModelViewSet):

    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def create(self, request, *args, **kwargs):
        body = json.loads(request.body.decode('utf-8'))

        owner = User.objects.get(id=body['owner_id'])
        Store.objects.create(owner=owner, name=body['name'])

        return Response({"data": "Successfully created!"})
