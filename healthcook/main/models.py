from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    img = models.FileField()
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Рецепт')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Contacts(models.Model):
    name = models.CharField('Имя', max_length=100)
    email = models.CharField('Email', max_length=250)
    message = models.TextField('Сообщение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Ankets(models.Model):
    age = models.CharField('Возраст', max_length=3)
    GENDER = (
        ('', 'Мужчина'),
        ('0', 'Женщина'),
    )
    gender = models.CharField(blank='False', max_length=11, choices=GENDER)
    height = models.IntegerField('Рост')
    weight = models.IntegerField('Вес')
    GOAL = (
        ('', 'Похудение'),
        ('0', 'Поддержание веса'),
        ('1', 'Набор массы')
    )
    goal = models.CharField(blank='False', max_length=100, choices=GOAL)
    SPORT = (
        ('', 'Сидячий образ жизни, отсутствие тренировок'),
        ('0', 'Сидячий образ жизни, тренировки несколько раз в неделю'),
        ('1', 'От трёх до четырёх тренировок в неделю'),
        ('2', 'Ежедневные тренировки или работа с регулярными физ. нагрузками'),
        ('3', 'Длительный рабочий день, требующий физ. нагрузки, или профессиональный спортсмен')
    )
    sport = models.CharField(blank='False', max_length=300, choices=SPORT)
    BREAKFAST = (
        ('', 'Блюда из яиц'),
        ('0', 'Блюда из творога'),
        ('1', 'Каши'),
        ('2', 'Мучные изделия')
    )
    breakfast = models.CharField(blank='False', max_length=100, choices=BREAKFAST)
    LUNCH = (
        ('', 'Суп'),
        ('0', 'Горячее блюдо с гарниром'),
        ('1', 'Салат')
    )
    lunch = models.CharField(blank='False', max_length=100, choices=LUNCH)
    DINNER = (
        ('', 'Горячее блюдо с гарниром'),
        ('0', 'Салат'),
        ('1', 'Десерт')
    )
    dinner = models.CharField(blank='False', max_length=100, choices=DINNER)

    def __str__(self):
        return self.age

    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'


class Infos(models.Model):
    name = models.CharField('Название', max_length=50)
    link = models.CharField('Ссылка', max_length=100)
    calories = models.IntegerField('Калории')
    protein = models.IntegerField('Белки')
    lipid = models.IntegerField('Жиры')
    carbon = models.IntegerField('Углеводы')
    type = models.CharField('Тип', max_length=100)

    def __str__(self):
        return self.name
