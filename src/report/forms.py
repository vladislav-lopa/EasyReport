from django import forms
from django.contrib.auth.models import User
from django.forms import EmailInput, TextInput, HiddenInput
from report.models import Config


class SignUpForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
                'type': 'password',
                'class': 'form-control top-indent',
                'pattern':'.{8,18}',
                'placeholder': 'Password',
                'title': "8 to 18 symbols."
                }))
    password_confirm = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={
                'type': 'password',
                'class': 'form-control top-indent',
                'pattern':'.{8,18}',
                'placeholder': 'Password confirm',
                'title': "8 to 18 symbols.",
                }))


    class Meta:
        model = User
        fields = ('email', 'username',)
        widgets = {
            "email": EmailInput(attrs={
                'type': 'email',
                'class': 'form-control top-indent',
                'placeholder': 'Email',
            }),
            "username": TextInput(attrs={
                'type': 'text',
                'class': 'form-control top-indent',
                'pattern': '.{4,18}',
                'placeholder': 'Username',
                'title': "4 to 18 symbols.",
            }),
        }

    def clean_password_confirm(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_confirm']:
            raise forms.ValidationError('Password mismatch')
        return cd['password']


class ConfigForm(forms.ModelForm):
    class Meta:
        model = Config
        fields = '__all__'
        widgets = {
            "name_project": TextInput(attrs={
                'type': 'text',
                'class': 'form-control top-indent',
                'placeholder': 'Name project',
                'pattern': '.{4}{32}',
                'title': "4-32 symbols."
            }),
            "key": TextInput(attrs={
                'type': 'text',
                'class': 'form-control top-indent',
                'placeholder': 'Key',
                'pattern': '.{32}',
                'title': "32 symbols."
            }),
            "token": TextInput(attrs={
                'type': 'text',
                'class': 'form-control top-indent',
                'pattern': '.{64}',
                'placeholder': 'Token',
                'title': "64 symbols.",
            }),
            "todo_id": TextInput(attrs={
                'type': 'text',
                'class': 'form-control top-indent',
                'pattern': '.{24}',
                'placeholder': 'Todo id',
                'title': "24 symbols.",
            }),
            "in_progress_id": TextInput(attrs={
                'type': 'text',
                'class': 'form-control top-indent',
                'pattern': '.{24}',
                'placeholder': 'In progress id',
                'title': "24 symbols.",
            }),
            "code_review_id": TextInput(attrs={
                'type': 'text',
                'class': 'form-control top-indent',
                'pattern': '.{24}',
                'placeholder': 'Code review id',
                'title': "24 symbols.",
            }),
            "in_test_id": TextInput(attrs={
                'type': 'text',
                'class': 'form-control top-indent',
                'pattern': '.{24}',
                'placeholder': 'In test id',
                'title': "24 symbols.",
            }),
            "release_id": TextInput(attrs={
                'type': 'text',
                'class': 'form-control top-indent',
                'pattern': '.{24}',
                'placeholder': 'Release id',
                'title': "24 symbols.",
            }),
            "done_id": TextInput(attrs={
                'type': 'text',
                'class': 'form-control top-indent',
                'pattern': '.{24}',
                'placeholder': 'Done id',
                'title': "24 symbols.",
            }),
            "board_id": TextInput(attrs={
                'type': 'text',
                'class': 'form-control top-indent',
                'pattern': '.{24}',
                'placeholder': 'Board id',
                'title': "24 symbols.",
            }),
            "user": HiddenInput()
        }