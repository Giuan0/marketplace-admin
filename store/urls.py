from django.urls import path
from rest_framework import routers
from django.conf.urls import url, include

from product.views import StoreProductViewSet
from .views import StoreView

router = routers.DefaultRouter()

router.register(r'products', StoreProductViewSet)
router.register(r'', StoreView)

urlpatterns = [
    url(r'^', include(router.urls)),
    # path('', views.index, name='index'),
]