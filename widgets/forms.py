from django import forms
from .models import Subscribers,Contact

class SubscribersForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    # mode = forms.CharField(max_length=10 )

    class Meta:
        model = Subscribers
        fields = ('email')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
