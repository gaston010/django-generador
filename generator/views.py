from django.shortcuts import render
import random as rd 
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    leng = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))

    for x in range(leng):
        generated_password += rd.choice(characters)

    return render(request, 'password.html', {'password': generated_password})

