# Generated by Django 4.0.3 on 2022-05-02 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0005_alter_productmodel_pauthor_introduce_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='pdescription',
            field=models.TextField(default='', max_length=290),
        ),
    ]
