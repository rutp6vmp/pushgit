# Generated by Django 4.1.1 on 2022-11-21 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0061_alter_productmodel_add_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='file_title',
            field=models.CharField(max_length=10, verbose_name='檔名'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='pdata',
            field=models.TextField(blank=True, max_length=10, null=True, verbose_name='歸類'),
        ),
    ]
