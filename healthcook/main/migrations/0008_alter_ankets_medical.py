# Generated by Django 4.1.7 on 2023-03-23 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_ankets_medical'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ankets',
            name='medical',
            field=models.CharField(choices=[('', 'Изжога'), ('0', 'Непереносимость глютена'), ('1', 'Непереносимость лактозы'), ('2', 'Диабет'), ('3', 'Язва'), ('5', 'Повышенный холестерин')], max_length=255),
        ),
    ]
