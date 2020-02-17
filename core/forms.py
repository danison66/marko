from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name',
                    widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name',
                    widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )

        def signup(self, request, user):
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.save()
            return user

        def __init__(self, *args, **kwargs):
            super(CustomSignupForm, self).__init__(*args, **kwargs)
            for fieldname, field in self.fields.items():
                field.widget.attrs.update({
                'class': 'signup'
                })
