from django import forms
from item.models import ContactForm

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['first_name', 'last_name', 'email', 'number', 'address', 'company_name', 'message']