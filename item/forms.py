from django import forms
from item.models import Message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['first_name', 'last_name', 'email', 'number', 'address', 'company_name', 'message']