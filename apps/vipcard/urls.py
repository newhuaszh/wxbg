# coding=utf-8
__author__ = 'szh'
__date__ = '2017/7/12 0012 11:41'

from django.conf.urls import url, include
from vipcard import views
# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register(r'cards', views.cards)

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^vipcards/$', views.vipcard_list),
    url(r'^vipcards/(?P<pk>[0-9a-zA-Z]+)/$', views.vipcard_detail),
    url(r'^login/$', views.admin_login),
]
