from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PersonalInformation, PatientMedicalInformation


class PatientMedicalInformationForm(ModelForm):
    class Meta:
        model = PatientMedicalInformation
        fields = (
            'blood_type', 'height', 'weight', 'allergies', 'medications', 'stroke', 'diabetes', 'arthritis',
            'alcoholism', 'tuberculosis')


class PersonalInformationForm(ModelForm):
    class Meta:
        model = PersonalInformation
        fields = (
            'street_address', 'city', 'state', 'zip', 'social_security', 'dob', 'sex', 'martial_status',
            'primary_phone')


class PatientSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

