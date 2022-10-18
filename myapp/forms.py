from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model, password_validation
from django.core.mail import send_mail
from django.contrib.auth import  get_user_model


User = get_user_model()


# class UserCreationForm(forms.ModelForm):
#     username = forms.CharField(max_length=80)
#     email = forms.EmailField()
#     password1 = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput,
                               help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    email = forms.EmailField()

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Passwords are not equal')
        password_validation.validate_password(self.cleaned_data.get('password'), None)
        return self.cleaned_data

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )
        send_mail(
            'Send mail',
            'Welcome my  Blog',
            'aydin.aliyev058@gmail.com',
            [self.cleaned_data['email']]
        )


# class RegisterForm(UserCreationForm):
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Password',
#     }), )
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Confirm password',
#     }), )
#
#     class Meta:
#         model = User
#         widgets = {
#             'first_name': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'First name',
#             }),
#             'email': forms.EmailInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Email',
#             }),
#             'username': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Username',
#             }),
#             'last_name': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Last name',
#             }),
#
#         }
#         fields = ['first_name', 'last_name', 'username', 'email',
#                   'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = UsernameField(label="", widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Username', }))
    password = forms.CharField(label="", strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password', }), )