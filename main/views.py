# from django.views.generic.base import TemplateView
#
# class Main(TemplateView):
#     template_name = 'main.html'

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import List
from django.core.paginator import Paginator
from django.db.models import Q
# from .forms import Menuform
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_sameorigin

def Main(request):
    return render(request, 'main.html')


def Place(request):
    return render(request, 'place.html')


def Face(request):
    return render(request, 'face.html')


def Load(request):
    return render(request, 'load.html')

@xframe_options_sameorigin
def Menu(request):
    return render(request, 'menu.html')

@xframe_options_sameorigin
def Menu1(request):
    q = List.objects.values_list('category', flat=True).distinct()
    page = request.GET.get('page', '1')  # 페이지
    coffee_category = List.objects.filter(category='커피')
    coffee_paginator = Paginator(coffee_category, 6)  # 페이지당 n개씩 보여주기
    coffee_page_obj = coffee_paginator.get_page(page)
    context = {
        'coffee_category':coffee_page_obj,
        'q':q,
        }
    return render(request, 'menu1.html', context)

@xframe_options_sameorigin
def Menu2(request):
    q = List.objects.values_list('category', flat=True).distinct()
    page = request.GET.get('page', '1')  # 페이지
    tea_category = List.objects.filter(category='차')
    tea_paginator = Paginator(tea_category, 6)  # 페이지당 n개씩 보여주기
    tea_page_obj = tea_paginator.get_page(page)
    context = {
        'tea_category':tea_page_obj,
        'q':q,
        }
    return render(request, 'menu2.html', context)

@xframe_options_sameorigin
def Menu3(request):
    q = List.objects.values_list('category', flat=True).distinct()
    page = request.GET.get('page', '1')  # 페이지
    beverage_category = List.objects.filter(category='음료')
    beverage_paginator = Paginator(beverage_category, 6)  # 페이지당 n개씩 보여주기
    beverage_page_obj = beverage_paginator.get_page(page)
    context = {
        'beverage_category':beverage_page_obj,
        'q':q,
        }
    return render(request, 'menu3.html', context)

@xframe_options_sameorigin
def Menu4(request):
    q = List.objects.values_list('category', flat=True).distinct()
    page = request.GET.get('page', '1')  # 페이지
    dessert_category = List.objects.filter(category='디저트')
    dessert_paginator = Paginator(dessert_category, 6)  # 페이지당 n개씩 보여주기
    dessert_page_obj = dessert_paginator.get_page(page)
    context = {
        'dessert_category':dessert_page_obj,
        'q':q,
        }
    return render(request, 'menu4.html', context)

def Order(request):
    return render(request, 'order.html')


def Kitchen(request):
    return render(request, 'kitchen.html')


def Favorlist(request):
    return render(request, 'favor.html')

# MenuList 관련 View ------------------------------

def MenuList(request):
    food_list = List.objects.order_by('food_num')
    context = {'food_list':food_list}
    return render(request, 'menulist.html', context)


def food_detail(request, food_id):
    food = get_object_or_404(List, pk=food_id)
    context = {'food': food}
    return render(request, 'food_detail.html', context)


def Category_test(request, word):
    food_category = List.objects.filter(category=word).values()
    return HttpResponse(food_category)

def test(request):
    q = List.objects.values_list('category', flat=True).distinct()
    q_dict = {
        'q':q,
    }

    return HttpResponse(q_dict)