# Generated by Django 4.1.1 on 2022-12-07 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0068_authorized_checkbox'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorized',
            name='Checkbox',
        ),
    ]