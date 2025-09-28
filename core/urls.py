

from rest_framework import routers

from core import viewsets

router = routers.DefaultRouter()
router.register('albums', viewsets.AlbumViewSet)
router.register('authors', viewsets.AuthorViewSet)
router.register('music', viewsets.MusicViewSet)

urlpatterns = router.urls

