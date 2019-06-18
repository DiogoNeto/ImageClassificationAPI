from rest_framework import routers, serializers, viewsets
from .models import Image, XPTO

class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Image
        fields = ('id', 'description', 'image')

class XPTOSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = XPTO
        fields = ('id', 'description')