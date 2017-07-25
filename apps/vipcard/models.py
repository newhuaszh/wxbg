# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class VipCard(models.Model):
    card = models.CharField(max_length=20, verbose_name=u'卡号', default='')
    name = models.CharField(max_length=50, verbose_name=u'姓名', null=True, blank=True)
    tel = models.CharField(max_length=50, verbose_name=u'手机号码', null=True, blank=True)
    openid = models.CharField(max_length=50, verbose_name=u'微信ID', null=True, blank=True)
    integral = models.IntegerField(default=0, verbose_name=u'积分')
    money = models.IntegerField(default=0, verbose_name=u'储值余额')
    gender = models.CharField(max_length=7, choices=(('male', u'男'), ('female', u'女')), default='female',
                              verbose_name=u'性别')
    address = models.CharField(max_length=200, verbose_name=u'家庭地址', null=True, blank=True)
    birth = models.DateField(verbose_name=u'生日', null=True, blank=True)
    weixin = models.CharField(max_length=20, verbose_name=u'微信号', null=True, blank=True)
    des = models.CharField(max_length=200, verbose_name=u'描述', null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'会员卡'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "{0} {1}".format(self.card, self.name)
