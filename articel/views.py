from django.shortcuts import render
from rest_framework import viewsets
from .models import Articel, CateGory
from .serializers import ArticelSerializer, UserSerializer, CateGorySerializer
from django.contrib.auth.models import User


class ArticelApi(viewsets.ModelViewSet):
    queryset = Articel.objects.all()
    serializer_class = ArticelSerializer

class CateGoryApi(viewsets.ModelViewSet):
    queryset = CateGory.objects.all()
    serializer_class = CateGorySerializer

class UserApi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

