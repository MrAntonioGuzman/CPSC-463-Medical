from django import forms


class ScheduleAppointmentForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    date = forms.DateField()
    reason = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 10}))


class InboxMessageForm(forms.Form):
    recipient = forms.CharField(max_length=50)
    title = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 10}))


class SearchRecipes(forms.Form):
    medicine = forms.CharField(max_length=100)

