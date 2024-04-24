# customers/forms.py

from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'building_details', 'city', 'state', 'postal_code']
