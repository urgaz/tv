from django import forms
from django.forms.forms import Form

class Service_net_useForm(forms.Form):
    ip = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'input'}))

    