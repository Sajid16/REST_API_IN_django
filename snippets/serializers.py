from rest_framework import serializers
from .models import Snippet, UserList


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields = ['username', 'password']
