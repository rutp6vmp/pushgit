# Generated by Django 4.0.3 on 2022-05-08 13:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0010_productmodel_pimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='upload_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='pimages',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]