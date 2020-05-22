from django import forms
from .models import data

class get_data(forms.ModelForm):
    class Meta:
        model=data
        fields=["comment","User_lat","User_lon"]
