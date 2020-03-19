from rest_framework import serializers
from . models import *
from django.contrib.auth.hashers import make_password

class EdiFdsCacmSerializer(serializers.ModelSerializer):
    class Meta:
        model = EdiFdsCacm        
        fields = "__all__"



class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser 
        fields = ['username', 'password', 'email', 'is_superuser', 'is_staff', 'is_active', 'date_joined']
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        user.password = make_password(validated_data['password'])
        user.save()
        return user
      
class AuthPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthPermission 
        fields = ['id', 'name', 'content_type', 'codename']

    def create(self, validated_data):
        permission = super().create(validated_data)
        permission.save()
        return permission

class AuthGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroup 
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        role = super().create(validated_data)
        role.save()
        return role





class AuthGroupPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroupPermissions  
        fields = ['id', 'group', 'permission']

    def create(self, validated_data):
        groups_data = validated_data.get('group')
        groups = AuthGroup.objects.get(id= groups_data.id)
        permission_data = validated_data.get('permission')
        permissions = AuthPermission.objects.get(id= permission_data.id)
        data = AuthGroupPermissions(group=groups, permission=permissions)
        data.save()
        return data

class AuthUserGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserGroups
        fields = ['id', 'user', 'group']
    
    def create(self, validated_data):
        user_data = validated_data.get('user')
        users = AuthUser.objects.get(id= user_data.id)
        groups_data = validated_data.get('group')
        groups = AuthGroup.objects.get(id= groups_data.id)
        data = AuthUserGroups(user=users, group=groups)
        data.save()
        return data

class AuthUserUserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserUserPermissions
        fields = ['id', 'user', 'permission']

    def create(self, validated_data):
        user_data = validated_data.get('user')
        users = AuthUser.objects.get(id = user_data.id)
        permissions_data = validated_data.get('permission')
        permissions = AuthPermission.objects.get(id = permissions_data.id)
        data = AuthUserUserPermissions(user=users, permission=permissions)
        data.save()
        return data




class AuthGroupPermissions2Serializer(serializers.ModelSerializer):
    permission = AuthPermissionSerializer()
    class Meta:
        model = AuthGroupPermissions  
        fields = ['id', 'group', 'permission']

class AuthUserGroups2Serializer(serializers.ModelSerializer):
    group = AuthGroupSerializer()
    class Meta:
        model = AuthUserGroups
        fields = ['id', 'user', 'group']


class AuthUserUserPermissions2Serializer(serializers.ModelSerializer):
    permission = AuthPermissionSerializer() 
    class Meta:
        model = AuthUserUserPermissions
        fields = ['id', 'user', 'permission']



class AuthUserGroups3Serializer(serializers.ModelSerializer):
    user = AuthUserSerializer()
    class Meta:
        model = AuthUserGroups
        fields = ['id', 'user', 'group']