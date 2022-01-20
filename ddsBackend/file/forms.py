from django import forms
from .models import myFile


class FileForm(forms.ModelForm):
    class Meta:
        model = myFile
        fields = ('title', 'expiary_date', 'doc', 'is_lock')
