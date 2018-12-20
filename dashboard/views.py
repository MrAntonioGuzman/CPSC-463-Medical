from django.shortcuts import render
from .forms import ScheduleAppointmentForm, InboxMessageForm, SearchRecipes
from patient.models import Appointments, InboxIn, InboxOut
from django.http import JsonResponse
from django.core import serializers


def home(request):
    return render(request, 'dashboard/home.html')


def schedule_appt(request):
    if request.method == 'POST':
        form = ScheduleAppointmentForm(request.POST)
        if form.is_valid():
            user = request.user
            date = form.cleaned_data.get('date')
            reason = form.cleaned_data.get('reason')

            appt = Appointments.objects.create(patient=user, first_name=user.first_name, last_name=user.last_name, date=date, reason=reason)
            sender = 'donotreply@company.name'
            title = 'REMINDER - Scheduled Appointment'
            message = 'Patient: {}, {}\n\n' \
                      '\tYour appointment has been scheduled at: {}\n' \
                      '\tPlease remember to arrive 15 minutes early to your appointment\n' \
                      '\tPlease do not respond to this email\n'.format(user.last_name, user.first_name, date)
            inbox_in = InboxIn.objects.create(patient=user, sender=sender, title=title, message=message)
            success = True
            return render(request, 'dashboard/schedule.html', {'form': form, 'success': success})
    else:
        form = ScheduleAppointmentForm()
    return render(request, 'dashboard/schedule.html', {'form': form})


def inbox(request):
    user = request.user
    inbox_in = InboxIn.objects.filter(patient=user)
    if request.method == 'POST':
        form = InboxMessageForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data.get('recipient')
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            new_inbox_out = InboxOut.objects.create(patient=user, recipient=recipient, title=title, message=message)
    else:
        form = InboxMessageForm()

    inbox_out = InboxOut.objects.filter(patient=user)
    return render(request, 'dashboard/inbox.html', {'form': form, 'inbox_in': inbox_in, 'inbox_out': inbox_out})


def ajax_inbox(request):
    if request.is_ajax():
        id = request.GET.get('id', None)
        inbox_in = InboxIn.objects.get(id=id)
        data = serializers.serialize('json', [inbox_in])
    else:
        data = 'fail'
    return JsonResponse(data, safe=False)


def ajax_inbox_history(request):
    if request.is_ajax():
        id = request.GET.get('id', None)
        inbox_out = InboxOut.objects.get(id=id)
        data = serializers.serialize('json', [inbox_out])
    else:
        data = 'fail'

    return JsonResponse(data, safe=False)


def provider(request):
    return render(request, 'dashboard/provider.html')


def recipes(request):
    form = SearchRecipes()
    return render(request, 'dashboard/healthy_recipes.html', {'form': form})


def before_logout(request):
    return render(request, 'dashboard/lgout.html')
