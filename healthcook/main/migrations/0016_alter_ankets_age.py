# Generated by Django 4.1.7 on 2023-05-26 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_ankets_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ankets',
            name='age',
            field=models.CharField(max_length=3, verbose_name='Возраст'),
        ),
    ]
