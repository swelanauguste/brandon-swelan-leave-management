# Generated by Django 4.0.4 on 2022-05-20 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0002_employeeleave_leaverequest_delete_leave'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverequest',
            name='days_requested',
            field=models.IntegerField(default=0),
        ),
    ]