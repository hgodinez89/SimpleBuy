from django import forms

from users.models import User

from django.utils.translation import gettext_lazy as _

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=4, max_length=50,
                                label=_('Username'),
                                widget=forms.TextInput(attrs= {
                                   'class': 'form-control',
                                   'id': 'username'
                                }))
    email = forms.EmailField(required=True,
                             label=_('Email'),
                             widget=forms.EmailInput(attrs= {
                                   'class': 'form-control',
                                   'id': 'email'
                                }))
    password = forms.CharField(required=True,
                               label=_('Password'),
                               widget=forms.PasswordInput(attrs= {
                                   'class': 'form-control',
                                   'id': 'password'
                                }))

    confirm_password = forms.CharField(required=True,
                                       label=_('Confirm Password'),
                                       widget=forms.PasswordInput(attrs= {
                                           'class': 'form-control',
                                           'id': 'confirm_password'
                                        }))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(_('Username does already exists'))

        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_('Email does already exists'))

        return email

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            self.add_error('confirm_password', _('The password does not match'))

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )