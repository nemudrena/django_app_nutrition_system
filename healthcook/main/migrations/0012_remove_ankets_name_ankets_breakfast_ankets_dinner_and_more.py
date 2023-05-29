# Generated by Django 4.1.7 on 2023-05-26 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_ankets_medical_1_remove_ankets_medical_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ankets',
            name='name',
        ),
        migrations.AddField(
            model_name='ankets',
            name='breakfast',
            field=models.CharField(blank='False', choices=[('', 'Блюда из яиц'), ('0', 'Блюда из творога'), ('1', 'Каши'), ('2', 'Мучные изделия')], max_length=100),
        ),
        migrations.AddField(
            model_name='ankets',
            name='dinner',
            field=models.CharField(blank='False', choices=[('', 'Блюда из яиц'), ('0', 'Блюда из творога'), ('1', 'Каши'), ('2', 'Мучные изделия')], max_length=100),
        ),
        migrations.AddField(
            model_name='ankets',
            name='goal',
            field=models.CharField(blank='False', choices=[('', 'Похудение'), ('0', 'Поддержание веса'), ('1', 'Набор массы')], max_length=100),
        ),
        migrations.AddField(
            model_name='ankets',
            name='lunch',
            field=models.CharField(blank='False', choices=[('', 'Блюда из яиц'), ('0', 'Блюда из творога'), ('1', 'Каши'), ('2', 'Мучные изделия')], max_length=100),
        ),
        migrations.AddField(
            model_name='ankets',
            name='sport',
            field=models.CharField(blank='False', choices=[('', 'Сидячий образ жизни, отсутствие тренировок'), ('0', 'Сидячий образ жизни, тренировки несколько раз в неделю'), ('1', 'От трёх до четырёх тренировок в неделю'), ('2', 'Ежедневные тренировки или работа с регулярными физ. нагрузками'), ('3', 'Длительный рабочий день, требующий физ. нагрузки, или профессиональный спортсмен')], max_length=300),
        ),
        migrations.AlterField(
            model_name='ankets',
            name='gender',
            field=models.CharField(blank='False', choices=[('', 'Мужчина'), ('0', 'Женщина')], max_length=11),
        ),
        migrations.AlterField(
            model_name='articles',
            name='full_text',
            field=models.TextField(verbose_name='Рецепт'),
        ),
    ]
