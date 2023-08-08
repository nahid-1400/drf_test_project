from rest_framework import serializers
from .models import Articel, CateGory
from django.contrib.auth.models import User


class ArticelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    articles = ArticelSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = '__all__'

class CateGorySerializer(serializers.ModelSerializer):
    post_category = ArticelSerializer(read_only=True, many=True)
    class Meta:
        model = CateGory
        fields = '__all__'