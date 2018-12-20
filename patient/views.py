from django.shortcuts import render, redirect
from .forms import PatientSignUpForm, PersonalInformationForm, PatientMedicalInformationForm
from django.contrib.auth import login, authenticate
from .models import PersonalInformation, PatientMedicalInformation


def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('personal_info_signup') # Original was 'home'

    else:
        form = PatientSignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


def personal_info_signup(request):
    if request.method == 'POST':
        form = PersonalInformationForm(request.POST)
        if form.is_valid():
            user = request.user
            address = form.cleaned_data.get('street_address')
            city = form.cleaned_data.get('city')
            state = form.cleaned_data.get('state')
            zip = form.cleaned_data.get('zip')
            social = form.cleaned_data.get('social_security')
            dob = form.cleaned_data.get('dob')
            sex = form.cleaned_data.get('sex')
            martial_status = form.cleaned_data.get('martial_status')
            phone = form.cleaned_data.get('primary_phone')
            personal = PersonalInformation.objects.create(patient=user, street_address=address, city=city, state=state,
                                                          zip=zip, social_security=social, dob=dob, sex=sex,
                                                          martial_status=martial_status, primary_phone=phone)
            return redirect('medical_info_signup')
    else:
        form = PersonalInformationForm()
    return render(request, 'registration/personal_info_signup.html', {'form': form})


def medical_info_signup(request):
    if request.method == 'POST':
        form = PatientMedicalInformationForm(request.POST)
        if form.is_valid():
            user = request.user
            blood_type = form.cleaned_data.get('blood_type')
            height = form.cleaned_data.get('height')
            weight = form.cleaned_data.get('weight')
            allergies = form.cleaned_data.get('allergies')
            medications = form.cleaned_data.get('medications')
            stroke = form.cleaned_data.get('stroke')
            diabetes = form.cleaned_data.get('diabetes')
            arthritis = form.cleaned_data.get('arthritis')
            alcohol = form.cleaned_data.get('alcoholism')
            tuber = form.cleaned_data.get('tuberculosis')
            medical_info = PatientMedicalInformation.objects.create(patient=user, blood_type=blood_type, height=height,
                                                                    weight=weight, allergies=allergies,
                                                                    medications=medications, stroke=stroke,
                                                                    diabetes=diabetes, arthritis=arthritis,
                                                                    alcoholism=alcohol, tuberculosis=tuber)

            return redirect('home')
    else:
        form = PatientMedicalInformationForm()
    return render(request, 'registration/medical_info_signup.html', {'form': form})


def view_profile(request):
    user = request.user
    personal = PersonalInformation.objects.get(patient=user)
    medical = PatientMedicalInformation.objects.get(patient=user)
    return render(request, 'profile/view_profile.html', {'user': user, 'personal': personal, 'medical': medical})


def edit_profile(request):
    signUpForm = PatientSignUpForm()
    personalForm = PersonalInformationForm()
    patientForm = PatientMedicalInformationForm()
    return render(request, 'profile/edit_profile.html',
                  {'signupForm': signUpForm, 'personalForm': personalForm, 'patientForm': patientForm})

