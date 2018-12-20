from django import forms


class DoctorSearchForm(forms.Form):
    county = forms.CharField(max_length=100)
