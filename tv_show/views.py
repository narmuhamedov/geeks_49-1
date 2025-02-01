from django.shortcuts import render
from django.http import HttpResponse

def emodji(request):
    if request.method == 'GET':
        return HttpResponse('😀 😅 😜')

def text(request):
    if request.method == 'GET':
        return HttpResponse('Lorem ipsum dolor sit amet')

def image(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Hello</h1>'
                            '<img src="https://wp-s.ru/wallpapers/0/6/345228397232059/fon-rabochego-stola-microsoft-belyj-na-chernom.jpg" />')