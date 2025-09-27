from django_filters import rest_framework as filters

from core import models

# Filtros de pesquisa
LIKE = 'unaccent__icontains'  # Usando unaccent para ignorar acentos e trazer palavras semelhantes
ICONTAINS = 'icontains'  # Usando icontains para trazer palavras semelhantes
UNACCENT_IEXACT = 'unaccent__iexact'  # Usando unaccent para ignorar acentos e trazer palavras exatas
EQUALS = 'exact'  # Usando exact para trazer o campo exatas
STARTS_WITH = 'startswith'  # Usando startswith para trazer palavras que começam com o termo pesquisado
GT = 'gt'  # maior que
LT = 'lt'  # menor que
GTE = 'gte'  # maior ou igual a
LTE = 'lte'  # menor ou igual a
IN = 'in'  # Usando in para trazer palavras que estão na lista


class AuthorFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=LIKE)
    id = filters.NumberFilter(lookup_expr=EQUALS)
    id_start = filters.NumberFilter(field_name='id', lookup_expr=STARTS_WITH)
    created_at = filters.DateFilter(field_name='created_at', lookup_expr=GT)
    modified_at = filters.DateFilter(field_name='modified_at', lookup_expr=GTE)

    class Meta:
        model = models.Author
        fields = ['name', 'id', 'id_start', 'created_at', 'modified_at']


class AlbumFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr=LIKE)
    date = filters.DateFilter(lookup_expr=EQUALS)
    date_gte = filters.DateFilter(field_name='date', lookup_expr=GTE)
    author_name = filters.CharFilter(field_name='author__name', lookup_expr=LIKE)
    author_id = filters.CharFilter(field_name='author', lookup_expr=EQUALS)

    class Meta:
        model = models.Album
        fields = ['title', 'date', 'date_gte', 'author_name', 'author_id']


class MusicFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr=LIKE)
    duration = filters.DurationFilter(lookup_expr=GTE)
    date = filters.DateFilter(field_name='album__date', lookup_expr=GTE)
    album = filters.CharFilter(field_name='album__title', lookup_expr=LIKE)
    author = filters.CharFilter(field_name='album__author__name', lookup_expr=LIKE)

    class Meta:
        model = models.Music
        fields = ['title', 'duration', 'album', 'author', 'date']
