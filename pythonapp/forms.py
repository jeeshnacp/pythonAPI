from django import forms
from django.contrib.auth.forms import UserCreationForm

from pythonapp.models import Login


class DoctorRegister(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2', 'name', 'contact_no', 'email', 'address')


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class PatientRegister(UserCreationForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2', 'name', 'age', 'gender', 'contact_no', 'address')