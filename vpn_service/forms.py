from django import forms
from .models import Site


class URLForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ["name", "url"]
        labels = {
            "name": "Name of site",
            "url": "URL to add",
        }
