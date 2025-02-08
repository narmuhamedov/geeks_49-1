from django.shortcuts import render
from . import models

#Список всех продуктов
def all_products(request):
    if request.method == "GET":
        query  = models.Product.objects.all().order_by('-id')
        context_object_name = {
            'all_products': query,
        }
        return render(request, template_name='products_home/all_products.html',
                      context=context_object_name)

#для ванной
def bathroom_products(request):
    if request.method == "GET":
        query  = models.Product.objects.filter(tags__name='для ванной комнаты').order_by('-id')
        context_object_name = {
            'bathroom': query,
        }
        return render(request, template_name='products_home/bathroom.html',
                      context=context_object_name)

#для ванной
def kitchen_products(request):
    if request.method == "GET":
        query  = models.Product.objects.filter(tags__name='для кухни').order_by('-id')
        context_object_name = {
            'kitchen': query,
        }
        return render(request, template_name='products_home/kitchen.html',
                      context=context_object_name)
