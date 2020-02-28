from rest_framework import serializers
from . models import AuthUser, EdiFdsCacm
from django.contrib.auth.hashers import make_password

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser 
        fields = ['username', 'password', 'email', 'is_superuser', 'is_staff', 'is_active', 'date_joined'  ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        user.password = make_password(validated_data['password'])
        user.save()
        return user
      
class EdiFdsCacmSerializer(serializers.ModelSerializer):
    class Meta:
        model = EdiFdsCacm        
        fields = "__all__"