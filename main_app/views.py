from django.shortcuts import render

# Create your views here.

from .serializers import AuthUserSerializer, EdiFdsCacmSerializer
from .models import AuthUser, EdiFdsCacm
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

class Register(viewsets.ModelViewSet):
    serializer_class = AuthUserSerializer
    queryset = AuthUser.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['post', 'get']

class Dividend(viewsets.ModelViewSet):
    serializer_class = EdiFdsCacmSerializer
    queryset = EdiFdsCacm.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['get']    