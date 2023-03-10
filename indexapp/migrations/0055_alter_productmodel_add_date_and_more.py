# Generated by Django 4.1.1 on 2022-11-21 15:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0054_rename_pdate_productmodel_mod_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='add_date',
            field=models.DateTimeField(auto_now=True, verbose_name='保存日期'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='mod_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='最後修改日期'),
        ),
    ]
