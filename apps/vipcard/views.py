from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import VipCard
from .serializers import VipcardSerializer


class cards(viewsets.ModelViewSet):
    queryset = VipCard.objects.all()
    serializer_class = VipcardSerializer


@csrf_exempt
def admin_login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        if isinstance(data, dict):
            user_name = data['name']
            pass_word = data['password']
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return HttpResponse(status=status.HTTP_200_OK)
            else:
                return HttpResponse(status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def vipcard_list(request):
    if not request.user.is_authenticated():
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        vipcards = VipCard.objects.all()
        serializer = VipcardSerializer(vipcards, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if isinstance(data, list):
            err = False
            for d in data:
                if isinstance(d, dict):
                    serializer = VipcardSerializer(data=d)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        err = True
                else:
                    err = True
            if err:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        elif isinstance(data, dict):
            serializer = VipcardSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # vipcards = VipCard.objects.filter(Q(card=11111111) | Q(card=44455566))
        vipcards = VipCard.objects.all()
        vipcards.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def vipcard_detail(request, pk):
    try:
        vipcard = VipCard.objects.get(name=pk)
    except VipCard.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VipcardSerializer(vipcard)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VipcardSerializer(vipcard, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        vipcard.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
