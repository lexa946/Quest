from django.forms import ModelForm

from .models import Hero

class HeroForm(ModelForm):
    class Meta:
        model = Hero
