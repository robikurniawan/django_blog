from django.forms import ModelForm
from django import forms
from .models import Artikel


class ArtikelForm(forms.Form,ModelForm):
    class Meta:
        model = Artikel
        fields = [
            'judul',
            'isi',
            'kategori',
            'gambar'
        ]

