from django.forms import ModelForm, PasswordInput
from django.contrib.auth.models import User


class UserFrom(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': PasswordInput(),

        }
