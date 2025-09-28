from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core import models, serializers, filters


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    filterset_class = filters.AuthorFilter
    permission_classes = [IsAuthenticatedOrReadOnly]
    ordering_fields = '__all__'
    ordering = '-modified_at'


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer
    filterset_class = filters.AuthorFilter
    permission_classes = [IsAuthenticatedOrReadOnly]
    ordering_fields = '__all__'
    ordering = '-modified_at'


class MusicViewSet(viewsets.ModelViewSet):
    queryset = models.Music.objects.all()
    serializer_class = serializers.MusicSerializer
    filterset_class = filters.AuthorFilter
    permission_classes = [IsAuthenticatedOrReadOnly]
    ordering_fields = '__all__'
    ordering = '-modified_at'
