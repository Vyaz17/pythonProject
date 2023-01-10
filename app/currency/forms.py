from django import forms
from currency.models import Rate
from currency.models import SendMailModels

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'buy',
            'sale',
            'source',
            'type',
        )


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = SendMailModels
        fields = (
            "email_to",
            "subject",
            "body",
        )
