from django import forms
from django.contrib.auth.models import User
from .models import event, attendance, band

class createEventForm(forms.ModelForm):


    startTime = forms.DateField(widget=forms.TextInput(
        attrs={'type': 'date'}
    ))

    endTime = forms.DateField(widget=forms.TextInput(
        attrs={'type': 'date'}
    ))

    class Meta:
        model = event
        fields = ['name','location','type','startTime','endTime']



class joinEventForm(forms.ModelForm):

    class Meta:
        model = attendance
        fields = ['event']

class connectBandForm(forms.ModelForm):

    bandID = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = band
        fields = ['bandID','password']