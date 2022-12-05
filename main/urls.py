from django.urls import path
from . import views

app_name = 'kiosk'

urlpatterns = [
    path('', views.Main, name='main'),
    path('place/', views.Place, name='place'),
    path('face/', views.Face, name='face'),
    path('face/load/', views.Load, name='load'),
    path('menu/', views.Menu, name='menu'),
    path('menu1/', views.Menu1, name='menu1'),
    path('menu2/', views.Menu2, name='menu2'),
    path('menu3/', views.Menu3, name='menu3'),
    path('menu4/', views.Menu4, name='menu4'),
    # path('menu5/', views.Menu5, name='menu5'),
    path('menu/order/', views.Order, name='order'),
    path('kitchen/', views.Kitchen, name='kitchen'),
    path('favor/', views.Favorlist, name='favor'),

    path('menulist/', views.MenuList, name='menulist'),
    path('menulist/<int:food_id>/', views.food_detail, name='food_detail'),
    # path('menulist/add_menulist/', views.add_menulist, name='add_menulist'),
]