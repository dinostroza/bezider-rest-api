from django.conf.urls import url
# from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^public-perfil\/(?P<pk>\d+)/$',PublicUserPerfilAPIView.as_view(), name='user-perfil'),
]