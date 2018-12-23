from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # path('', views.index, name='index'),
]