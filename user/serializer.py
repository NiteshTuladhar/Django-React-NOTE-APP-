from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueTogetherValidator

#djoser
from djoser.serializers import UserCreateSerializer

from user.models import Collaborations

# TOKEN OBTAIN WITH EMAIL LOGIN

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id',  'email', 'username', 'password')

# Resgister Serializations
class RegisterSerializations(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['email'],
            email=validated_data['email'], password=make_password(validated_data['password']))
        return user


# USER SERIALIZATION GET
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'date_joined', ]


class CollaborationSerializer(serializers.ModelSerializer):
    collaborator = serializers.SerializerMethodField()

    class Meta:
        
        model = Collaborations
        fields = ['collaborators', 'collaborator', 'permission']

    
    def get_collaborator(self, obj):
        return obj.collaborators.email

   
        # ToDo items belong to a parent list, and have an ordering defined
        # by the 'position' field. No two items in a given list may share
        # the same position.
       
