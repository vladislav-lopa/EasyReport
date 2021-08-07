from django import forms
from presentation.models import PresentationData


class SignUpForm(forms.ModelForm):
    class Meta:
        model = PresentationData
        fields = '__all__'