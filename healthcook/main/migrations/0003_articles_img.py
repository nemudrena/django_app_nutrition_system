# Generated by Django 4.1.7 on 2023-03-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contacts_alter_articles_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='img',
            field=models.FileField(default='default img', upload_to=''),
            preserve_default=False,
        ),
    ]
