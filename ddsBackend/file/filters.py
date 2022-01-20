import django_filters

from .models import myFile, ArchivedFile


# Provide the search option for myFile model.
class myFileFilter(django_filters.FilterSet):
    class Meta:
        model = myFile
        fields = ['index', 'title', 'author', 'uploader', 'expiary_date', 'is_lock', 'is_private']


# Provide the search option for ArchivedFile model.
class ArchivedFileFilter(django_filters.FilterSet):
    class Meta:
        model = ArchivedFile
        fields = ['index', 'title', 'author', 'uploader', 'archive_date', 'is_private', 'expiary_date']
