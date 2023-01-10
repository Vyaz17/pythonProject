import uuid

from django import forms
from accounts.models import User


class SingUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2',
        )


    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise forms.ValidationError("Пароли не совпадают")
            # self.add_error("password2", "Пароли не совпадают")
        return cleaned_data


    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.username = str(uuid.uuid4())
        instance.set_password(self.cleaned_data['password1'])
        instance.is_active = False

        from django.urls import reverse


        import settings.settings


        from accounts.utils_activate_email import activate_email
        activate_email(
            f'{settings.settings.HTTP_SCHEMA}://{settings.settings.DOMAIN}'
            f'{reverse("accounts:activate-link", args=[instance.username])}',
            instance.email
        )

        if commit:
            instance.save()
        return instance
