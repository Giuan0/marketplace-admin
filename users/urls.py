from django.conf.urls import url
from .views import CreateUserAPIView, authenticate_user
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'^login/$', authenticate_user),
]