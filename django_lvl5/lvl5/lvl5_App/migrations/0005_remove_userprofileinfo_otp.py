# Generated by Django 3.0.3 on 2020-06-05 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lvl5_App', '0004_userprofileinfo_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='otp',
        ),
    ]
