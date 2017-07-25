# coding=utf-8
__author__ = 'szh'
__date__ = '2017/7/12 0012 11:16'

from rest_framework import serializers
from .models import VipCard


class VipcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = VipCard
        fields = ('card', 'name', 'tel', 'integral', 'money', 'gender', 'address', 'birth', 'weixin', 'des', 'add_time')

    def create(self, validated_data):
        return VipCard.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.card = validated_data.get('card', instance.card)
        instance.name = validated_data.get('name', instance.name)
        instance.tel = validated_data.get('tel', instance.tel)
        instance.openid = validated_data.get('openid', instance.openid)
        instance.integral = validated_data.get('integral', instance.integral)
        instance.money = validated_data.get('money', instance.money)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.address = validated_data.get('address', instance.address)
        instance.birth = validated_data.get('birth', instance.birth)
        instance.weixin = validated_data.get('weixin', instance.weixin)
        instance.des = validated_data.get('des', instance.des)
        instance.add_time = validated_data.get('add_time', instance.add_time)
        instance.save()
        return instance
