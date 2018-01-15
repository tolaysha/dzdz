from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class SubscruberForms(forms.ModelForm):
    class Meta:
        model = Subscribers
        exclude = [""]


class BandsForms(forms.ModelForm):
    class Meta:
        model = Band
        exclude = ["user"]


class BandsUsernames(forms.ModelForm):
    class Meta:
        model = BandUsername
        exclude = [""]


class ConcertAgencyForms(forms.ModelForm):
    class Meta:
        model = ConcertAgency
        exclude = [""]


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput, label='E-mail')
    firstname = forms.CharField(label='Имя')
    surname = forms.CharField(label='Фамилия')
