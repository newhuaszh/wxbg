# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    birday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=7, choices=(('male', u'男'), ('female', u'女')), default='female',
                              verbose_name=u'性别')
    address = models.CharField(max_length=100, default=u'', verbose_name=u'地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'手机号码')
    image = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100, verbose_name=u'头像')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
