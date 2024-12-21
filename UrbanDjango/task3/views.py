from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home(requests):
    title = 'Детский магазин "МЕДВЕЖЁНОК"'
    text1 = 'Главная страница'
    text2 = 'Главная'
    text3 = 'Магазин'
    text4 = 'Корзина'
    context = {
        'title': title,
        'text': text1,
        'text1': text2,
        'text2': text3,
        'text3': text4
    }
    return render(requests, 'third_task/platform.html', context)

def shop(requests):
    title = 'Детские товары'
    text5 = 'Детские товары'
    list_shop = ['Велосипед','Кукла','Конструктор']
    context = {
        'title': title,
        'text': text5,
        'list_shop': list_shop
    }
    return render(requests, 'third_task/games.html', context)

    

def basket(requests):
    title = 'Корзина'
    text6 = 'Корзина'
    text7 = 'Извините, ваша корзина пуста'

    context = {
        'title': title,
        'text': text6,
        'text1': text7
    }
    return render(requests, 'third_task/cart.html', context)

