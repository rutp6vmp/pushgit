# Generated by Django 4.0.5 on 2022-07-10 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0031_alter_productmodel_special_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='pprice',
            field=models.IntegerField(default=0, null=True),
        ),
    ]