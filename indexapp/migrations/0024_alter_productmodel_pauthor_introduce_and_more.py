# Generated by Django 4.0.4 on 2022-05-29 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0023_alter_productmodel_pauthor_introduce_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='pauthor_introduce',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='pdata',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='pdescription',
            field=models.TextField(default='', max_length=1000),
        ),
    ]