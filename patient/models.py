from django.db import models
from django.contrib.auth.models import User


# Appointments Model
class Appointments(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    reason = models.CharField(max_length=5000)


# Messages Received Model
class InboxIn(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=5000)


# Messages Sent Model
class InboxOut(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=5000)


# Completed Profile Model
class CompletedProfile(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    

# Personal Information Model
class PersonalInformation(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    social_security = models.CharField(max_length=9)
    dob = models.CharField(max_length=50)

    # SEX ATTRIBUTE #
    FEMALE = 'F'
    MALE = 'M'
    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    sex = models.CharField(max_length=2, choices=SEX_CHOICES, default=MALE)
    # END SEX ATTRIBUTE #

    # MARTIAL STATUS ATTRIBUTE #
    MARRIED = 'M'
    SINGLE = 'S'
    DIVORCED = 'D'
    WIDOWED = 'W'
    MARTIAL_STATUS_CHOICES = (
        (SINGLE, 'Single'),
        (MARRIED, 'Married'),
        (DIVORCED, 'Divorced'),
        (WIDOWED, 'Widow')
    )
    martial_status = models.CharField(max_length=2, choices=MARTIAL_STATUS_CHOICES, default=SINGLE)
    primary_phone = models.CharField(max_length=13)
    # END MARTIAL STATUS ATTRIBUTE #


# Patient Medical Information Model
class PatientMedicalInformation(models.Model):

    # BLOOD TYPE INFORMATION
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    A_POSITIVE = 'A+'
    O_POSITIVE = 'O+'
    B_POSITIVE = 'B+'
    AB_POSITIVE = 'AB+'
    A_NEGATIVE = 'A-'
    O_NEGATIVE = 'O-'
    B_NEGATIVE = 'B-'
    AB_NEGATIVE = 'AB-'

    BLOOD_TYPE_CHOICES = (
        (A_POSITIVE, 'A+'),
        (O_POSITIVE, 'O+'),
        (B_POSITIVE, 'B+'),
        (AB_POSITIVE, 'AB+'),
        (A_NEGATIVE, 'A-'),
        (O_NEGATIVE, 'O-'),
        (B_NEGATIVE, 'B-'),
        (AB_NEGATIVE, 'AB-'),
    )

    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES, default=A_POSITIVE)
    # END BLOOD TYPE INFORMATION

    # Height in cm
    height = models.CharField(max_length=4)

    # Weight in pounds
    weight = models.CharField(max_length=4)
    allergies = models.CharField(max_length=200)
    medications = models.CharField(max_length=200)

    # HEALTH HISTORY (Does not include everything, but you get the point)
    YES = 'Y'
    NO = 'N'
    HISTORY_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No')
    )

    stroke = models.CharField(max_length=1, choices=HISTORY_CHOICES, default=NO)
    diabetes = models.CharField(max_length=1, choices=HISTORY_CHOICES, default=NO)
    arthritis = models.CharField(max_length=1, choices=HISTORY_CHOICES, default=NO)
    alcoholism = models.CharField(max_length=1, choices=HISTORY_CHOICES, default=NO)
    tuberculosis = models.CharField(max_length=1, choices=HISTORY_CHOICES, default=NO)
    # END HEALTH HISTORY



