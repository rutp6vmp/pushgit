# Generated by Django 4.1.1 on 2022-11-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0058_productmodel_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='file_title',
            field=models.CharField(max_length=30, verbose_name='檔名'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='uploadedFile',
            field=models.FileField(upload_to='file', verbose_name='檔案'),
        ),
    ]
