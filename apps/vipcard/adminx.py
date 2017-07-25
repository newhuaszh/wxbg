# coding=utf-8
__author__ = 'szh'
__date__ = '2017/7/11 0011 10:13'

import xadmin
from .models import VipCard


class VipCardAdmin(object):
    list_display = ['card', 'name', 'tel', 'openid', 'integral', 'money', 'gender', 'address', 'birth', 'weixin', 'des',
                    'add_time']
    search_fields = ['card', 'name', 'tel', 'openid', 'integral', 'money', 'gender', 'address', 'birth', 'weixin',
                     'des']
    list_filter = ['card', 'name', 'tel', 'openid', 'integral', 'money', 'gender', 'address', 'birth', 'weixin', 'des',
                   'add_time']
    list_editable = ['integral', 'money']
    list_export = ('xls',)
    model_icon = 'fa fa-credit-card'


xadmin.site.register(VipCard, VipCardAdmin)
