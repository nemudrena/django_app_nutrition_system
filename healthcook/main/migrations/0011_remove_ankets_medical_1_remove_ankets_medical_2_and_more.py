# Generated by Django 4.1.7 on 2023-03-23 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_ankets_medical_ankets_medical_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ankets',
            name='medical_1',
        ),
        migrations.RemoveField(
            model_name='ankets',
            name='medical_2',
        ),
        migrations.RemoveField(
            model_name='ankets',
            name='medical_3',
        ),
    ]
