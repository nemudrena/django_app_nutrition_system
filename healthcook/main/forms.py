from .models import Contacts
from .models import Ankets
from django.forms import ModelForm, TextInput, EmailInput, Textarea, RadioSelect, Select, CheckboxInput, CheckboxSelectMultiple,ChoiceField,BooleanField


class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'message']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваша почта'
            }),
            'message': Textarea(attrs={
                'class': 'form-control'
            })
        }


class AnketsForm(ModelForm):
    class Meta:
        model = Ankets
        fields = ['age', 'gender', 'height', 'weight', 'goal', 'sport', 'breakfast', 'lunch', 'dinner']

        widgets = {
            'age': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш возраст, лет'
            }),
            'gender': RadioSelect(),
            'height': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш рост, см'
            }),
            'weight': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш вес, кг'
            }),
            'goal': RadioSelect(),
            'sport': RadioSelect(),
            'breakfast': RadioSelect(),
            'lunch': RadioSelect(),
            'dinner': RadioSelect()
        }
