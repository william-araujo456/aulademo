from rest_framework import serializers

from core import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Music
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Album
        fields = '__all__'
