from django.shortcuts import render


# Create your views here.
def home(requests):
    title = 'Детский магазин "МЕДВЕЖЁНОК"'
    text = 'Главная страница'

    context = {
        'title': title,
        'text': text,
    }
    return render(requests, 'fourth_task/platform.html', context)


def shop(requests):
    title = 'Детские товары'
    text = 'Детские товары'
    list_shop = ['Велосипед', 'Кукла', 'Конструктор']
    context = {
        'title': title,
        'text': text,
        'list_shop': list_shop
    }
    return render(requests, 'fourth_task/games.html', context)


def basket(requests):
    title = 'Корзина'
    text = 'Корзина'
    text1 = 'Извините, ваша корзина пуста'

    context = {
        'title': title,
        'text': text,
        'text1': text1
    }
    return render(requests, 'fourth_task/cart.html', context)
# def parent(requests):
#     return render(requests, 'fourth_task/menu.html')