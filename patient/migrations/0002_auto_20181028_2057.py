# Generated by Django 2.0.1 on 2018-10-28 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inboxin',
            name='received_at',
        ),
        migrations.RemoveField(
            model_name='inboxout',
            name='sent_at',
        ),
    ]
