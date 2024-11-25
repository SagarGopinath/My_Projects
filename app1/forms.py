'''from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class Feedback_form(forms.Form):
    name = forms.CharField(
        max_length=100,
        validators=[RegexValidator(r'^[a-zA-Z ]+$', 'Enter a valid name using alphabetic characters only')],
        widget=forms.TextInput(attrs={'placeholder': 'Your Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email'})
    )
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Subject'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your Message'}),
        min_length=10
    )'''
    
