from django.shortcuts import render

# Create your views here.

from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

class Register(viewsets.ModelViewSet):
    serializer_class = AuthUserSerializer
    queryset = AuthUser.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['post', 'get', 'put']

class Dividend(viewsets.ModelViewSet):
    serializer_class = EdiFdsCacmSerializer
    queryset = EdiFdsCacm.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['get'] 
     
class Dated_Dividend(viewsets.ModelViewSet):
    serializer_class = EdiFdsCacmSerializer

    def get_queryset(self):
        queryset = EdiFdsCacm.objects.all()
        required_date = self.request.query_params.get('required_date')
        queryset = queryset.filter(ex_date = required_date)
        return queryset
        
    queryset = EdiFdsCacm.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['get'] 





class Add_permission(viewsets.ModelViewSet):
    serializer_class = AuthPermissionSerializer
    queryset = AuthPermission.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['post', 'get', 'put', 'delete']

class Add_role(viewsets.ModelViewSet):
    serializer_class = AuthGroupSerializer
    queryset = AuthGroup.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['post', 'get', 'put', 'delete']




class Assign_permission(viewsets.ModelViewSet):
    serializer_class = AuthGroupPermissionsSerializer
    queryset = AuthGroupPermissions.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['post', 'get', 'delete']

class Role_permission(viewsets.ModelViewSet):
    serializer_class = AuthGroupPermissions2Serializer

    def get_queryset(self):
        queryset = AuthGroupPermissions.objects.all()
        required_group = self.request.query_params.get('required_group')
        queryset = queryset.filter(group = required_group)
        return queryset

    permission_classes = (AllowAny,)
    http_method_names = ['get']





class Assign_role(viewsets.ModelViewSet):
    serializer_class = AuthUserGroupsSerializer
    queryset = AuthUserGroups.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['post', 'get', 'delete']

class User_role(viewsets.ModelViewSet):
    serializer_class = AuthUserGroups2Serializer

    def get_queryset(self):
        queryset = AuthUserGroups.objects.all()
        required_user = self.request.query_params.get('required_user')
        queryset = queryset.filter(user = required_user)
        return queryset

    permission_classes = (AllowAny,)
    http_method_names = ['get']




class Role_user(viewsets.ModelViewSet):
    serializer_class = AuthUserGroups3Serializer

    def get_queryset(self):
        queryset = AuthUserGroups.objects.all()
        required_group = self.request.query_params.get('required_group')
        queryset = queryset.filter(group = required_group)
        return queryset

    permission_classes = (AllowAny,)
    http_method_names = ['get']





class Assign_user_permission(viewsets.ModelViewSet):
    serializer_class = AuthUserUserPermissionsSerializer
    queryset = AuthUserUserPermissions.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'post']

class User_permission(viewsets.ModelViewSet):
    serializer_class = AuthUserUserPermissions2Serializer
    
    def get_queryset(self):
        queryset = AuthUserUserPermissions.objects.all()
        required_user = self.request.query_params.get('required_user')
        queryset = queryset.filter(user = required_user)
        return queryset

    permission_classes = (AllowAny,)
    http_method_names = ['get']
