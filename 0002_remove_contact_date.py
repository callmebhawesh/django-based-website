# Generated by Django 2.2.15 on 2020-08-26 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
    ]
