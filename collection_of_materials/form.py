from django import forms
from .models import CollectionOfMaterials

class CollectionOfMaterialsForms(forms.ModelForm):
    choice = [
        ("Wideo", "Wideo"),
        ("Czytanie", "Czytanie"),
        ("Słuchanie Pasywne", "Słuchanie Pasywne"),
        ("Gramatyka", "Gramatyka"),
        ("Słownictwo", "Słownictwo"),

    ]
    category = forms.ChoiceField(choices=choice, label="Kategoria")
    class Meta:
        model = CollectionOfMaterials
        fields = ['title','category','url','attention']
        labels = {'title': "Tytuł",
                  'url': "Adres URL",  'attention': "Komentarz"
        }

class Categorie(forms.Form):
    choice = [
        ("Wideo", "Wideo"),
        ("Czytanie", "Czytanie"),
        ("Słuchanie Pasywne", "Słuchanie Pasywne"),
        ("Gramatyka", "Gramatyka"),
        ("Słownictwo", "Słownictwo"),

    ]
    category = forms.ChoiceField(choices=choice, label="Kategoria")