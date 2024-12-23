from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from .form import UserRegister

# Create your views here.

def sign_up_by_html(request):
    users = ['Петя', 'Вася', 'Лёня']
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password == repeat_password and int(age) >= 18 and username not in users:
            return HttpResponse(f"Приветствуем, {username}!")
        if password != repeat_password:
            info.update({'error': 'Пароли не совпадают'})
        if int(age) < 18:
            info.update({'error': 'Вы должны быть старше 18'})
        if username in users:
            info.update({'error': 'Пользователь уже существует'})
    return render(request, 'fifth_task/registration_page.html', context={'info': info,})

def sign_up_by_django(request):
    users = ['Петя', 'Вася', 'Лёня']
    info = {}
    # form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in users:
                return HttpResponse(f"Приветствуем, {username}!")
            if password != repeat_password:
                info.update({'ERROR1': 'Пароли не совпадают'})
            if int(age) < 18:
                info.update({'ERROR2': 'Вы должны быть старше 18'})
            if username in users:
                info.update({'ERROR3': 'Пользователь уже существует'})
        else:
            form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', context={'info': info, })




