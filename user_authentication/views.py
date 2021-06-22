from django import http
from django.db.models import query
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import serializers, viewsets


from user_authentication.models import User
from user_authentication.serializers import UserSerializer


@csrf_exempt
def user_list(request):
    if request.method == "GET":
        query = User.objects.all()
        serializer = UserSerializer(query, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":

        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(data=serializer.errors, status=401, safe=False)


@csrf_exempt
def user_detail(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        user.delete()
        return HttpResponse(status=204)
