from django.shortcuts import render, redirect
from .models import Articles
from .models import Infos
from .forms import ContactsForm
from .forms import AnketsForm
from django.core.cache import cache
import csv
from django.views.generic import DetailView



# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def articles(request):
    return render(request, 'main/articles.html')


def articles_receipts(request):
    # receipts = Articles.objects.all()
    return render(request, 'main/receipts.html')  # {'receipts': receipts})


def articles_receipts_1(request):
    return render(request, 'main/articles_receipts_1.html')


def create(request):
    return render(request, 'main/create.html')


def articles_audio(request):
    return render(request, 'main/audio.html')


def articles_health(request):
    return render(request, 'main/health.html')


def menu_form(request):
    error = ''
    if request.method == 'POST':
        form = AnketsForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            cache.set('age', request.POST['age'])
            cache.set('height', request.POST['height'])
            cache.set('weight', request.POST['weight'])
            cache.set('gender', request.POST['gender'])
            cache.set('goal', request.POST['goal'])
            cache.set('sport', request.POST['sport'])
            cache.set('bf', request.POST['breakfast'])
            cache.set('lc', request.POST['lunch'])
            cache.set('dr', request.POST['dinner'])
            return redirect("result")
        else:
            error = 'Форма заполнена неверно'
    form = AnketsForm()
    data = {
        'form': form
    }
    return render(request, 'main/form.html', data)


def menu_result(request):
    age = cache.get('age')
    height = cache.get('height')
    weight = cache.get('weight')
    gender = cache.get('gender')
    goal = cache.get('goal')
    sport = cache.get('sport')
    breakfast = cache.get('bf')
    lunch = cache.get('lc')
    dinner = cache.get('dn')
    bf = []
    lc = []
    dn = []
    linkbf = []
    linklc = []
    linkdn = []
    active = {'': 1.2, '0': 1.375, '1': 1.55, '2': 1.7, '3': 1.9}
    goal_dict = {'': 0.85, '0': 1, '1': 1.15}
    type_bf = {'': 'Блюда из яиц','0': 'Блюда из творога','1': 'Каши','2': 'Мучные изделия'}
    type_lc = {'': 'Суп', '0': 'Горячее блюдо с гарниром', '1': 'Салат'}
    type_dn = {'': 'Горячее блюдо с гарниром', '0': 'Салат', '1': 'Десерт'}
    data = {}
    if gender == '':
        calories = round((66 + 13.7 * int(weight) + 5 * int(height) - 6.76 * int(age)) * active[sport] * goal_dict[goal])
    if gender == '0':
        calories = round((655 + 9.6 * int(weight) + 1.8 * int(height) - 4.7 * int(age)) * active[sport] * goal_dict[goal])
    if goal == '':
        protein = round(0.3*calories/4)
        carbon = round(0.4*calories/4)
        lipid = round(0.3*calories/9)
    if goal == '0':
        protein = round(0.3*calories/4)
        carbon = round(0.5*calories/4)
        lipid = round(0.2*calories/9)
    if goal == '1':
        protein = round(0.3*calories/4)
        carbon = round(0.55*calories/4)
        lipid = round(0.15*calories/9)
    dishes = Infos.objects.all()
    for dish in dishes:
        if dish.calories < calories/3 and dish.protein < protein/3 and dish.lipid < lipid/3 and dish.carbon < carbon/3 and dish.type == type_bf[breakfast]:
            bf.append(dish.name)
            linkbf.append(dish.link)
        if dish.calories < calories / 3 and dish.protein < protein / 3 and dish.lipid < lipid / 3 and dish.carbon < carbon / 3 and dish.type == type_bf[lunch]:
            lc.append(dish.name)
            linklc.append(dish.link)
        if dish.calories < calories / 3 and dish.protein < protein / 3 and dish.lipid < lipid / 3 and dish.carbon < carbon / 3 and dish.type == type_bf[dinner]:
            dn.append(dish.name)
            linkdn.append(dish.link)
        if len(dn) == 7 and len(bf)==7 and len(lc)==7:
            break

    data = {
        'calories': calories,
        'protein': protein,
        'carbon': carbon,
        'lipid': lipid,
        'bf':bf,
        'linkbf':linkbf,
        'lc':lc,
        'linklc':linklc,
        'dn':dn,
        'linkdn':linkdn
    }
    return render(request, 'main/result.html', context = data)



def contacts(request):
    error = ''
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            error = 'Ваше сообщение отправлено, мы вернемся к вам с ответом в ближайшее время'
        else:
            error = 'Форма была неверной'

    form = ContactsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/contacts.html', data)
