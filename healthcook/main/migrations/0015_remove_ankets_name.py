# Generated by Django 4.1.7 on 2023-05-26 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_ankets_dinner_alter_ankets_lunch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ankets',
            name='name',
        ),
    ]