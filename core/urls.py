from django.conf.urls import url
from django.contrib import admin

from .views import *


urlpatterns = [
    url(r'^news\/(?P<pk>\d+)/$',NewsDetailAPIView.as_view(), name='news'),
    url(r'^news/type\/(?P<pk>\d+)/$',NewsTypeAPIView.as_view(), name='type'),
    url(r'^news/category\/(?P<pk>\d+)/$',NewsCategoryAPIView.as_view(), name='category'),
    url(r'^news/catcher\/(?P<pk>\d+)/$',NewsCatcherAPIView.as_view(), name='catcher'),
    url(r'^news/map/$',NewsMapAPIView.as_view(), name='news'),
]