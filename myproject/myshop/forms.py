from django import forms


class EmailSubscriptionForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
