# Generated by Django 4.0.5 on 2022-07-10 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0030_productmodel_press'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='special_offer',
            field=models.IntegerField(default=0, null=True),
        ),
    ]