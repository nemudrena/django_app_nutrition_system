from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('articles', views.articles, name="articles"),
    path('create', views.create, name="create"),
    path('receipts', views.articles_receipts, name="receipts"),
    path('articles_receipts_1', views.articles_receipts_1, name="articles_receipts_1"),
    path('audio', views.articles_audio, name="audio"),
    path('health', views.articles_health, name="health"),
    path('form', views.menu_form, name="form"),
    path('result', views.menu_result, name="result"),
    path('contacts', views.contacts, name="contacts"),

]
