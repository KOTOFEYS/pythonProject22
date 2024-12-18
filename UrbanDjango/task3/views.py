from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home(requests):
    title = 'Детский магазин "МЕДВЕЖЁНОК"'
    text1 = 'Главная'
    text2 = 'Магазин'
    text3 = 'Корзина'
    context = {
        'title': title,
        'text1': text1,
        'text2': text2,
        'text3': text3
    }
    return render(requests, 'platform.html', context)

def shop(requests):
    title = 'Детские товары'
    text = 'Детские товары'
    text1 = 'Велосипед'
    text2 = 'Кукла'
    text3 = 'Конструктор'
    context = {
        'title': title,
        'text': text,
        'text1': text1,
        'text2': text2,
        'text3': text3
    }
    return render(requests, 'games.html', context)

    

def basket(requests):
    title = 'Корзина'
    text = 'Извините, ваша корзина пуста'
    context = {
        'title': title,
        'text': text
    }
    return render(requests, 'cart.html', context)

