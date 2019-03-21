from django.contrib.auth.models import User, Group
from rest_framework import serializers

from models import Input, LANGUAGE_CHOICES, STYLE_CHOICES



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'idade', 'genero', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class InputSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    photo = serializers.FilePathField(required=False, allow_blank=True, max_length=100)
    gender = serializers.CharField(style={'base_template': 'textarea.html'})
    age = serializers.BooleanField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Input` instance, given the validated data.
        """
        #return Input.objects.create(**validated_data)
        return ""

    def update(self, validated_data):
        """
        Create and return a new `Input` instance, given the validated data.
        """
        #return Input.objects.create(**validated_data)
        return ""
        
    def get(self, validated_data):
        #return Input.objects.get(**validated_data)
        return ""
