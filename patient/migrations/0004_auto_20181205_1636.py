# Generated by Django 2.0.1 on 2018-12-05 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_completedprofile_emergencycontactinformation_insuranceinformation_patientmedicalinformation_personal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emergencycontactinformation',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='insuranceinformation',
            name='patient',
        ),
        migrations.DeleteModel(
            name='EmergencyContactInformation',
        ),
        migrations.DeleteModel(
            name='InsuranceInformation',
        ),
    ]
