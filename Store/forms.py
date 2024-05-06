from django import forms
from . models import Contact, Subscriber


class FormContact(forms.ModelForm):
    name = forms.CharField(max_length=150, label="Name", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':  'Your Name',
        'required': 'required'
    }))
    phone_number = forms.CharField(max_length=15, label="Phone Number", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':  'Phone Number',
        'required': 'required'
    }))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email',
        'required': 'required'
    }))
    subject = forms.CharField(max_length=20, label="Subject", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Subject',
        'required': 'required'
    }))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Message',
        'rows': '5',
        'required': 'required'
    }))

    class Meta:
        model = Contact
        fields = '__all__'



class SubscriberForm(forms.ModelForm):

    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'class': 'form-control border-primary rounded-pill w-100 py-3 ps-4 pe-5',
        'placeholder': 'Your Email',
        'required': 'required'
    }))

    class Meta:
        model = Subscriber
        fields = ['email']
        