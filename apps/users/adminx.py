# coding=utf-8
__author__ = 'szh'
__date__ = '2017/7/11 0011 10:04'

import xadmin
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = u'芷茜印象后台管理系统'
    site_footer = u'芷茜印象'
    menu_style = 'accordion'


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
