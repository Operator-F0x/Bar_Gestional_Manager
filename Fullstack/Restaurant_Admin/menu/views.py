from django.shortcuts import render
from .models import juice, menucold,menuhot, special


def menus(requests):

    menuItemsCold = menucold.objects.all
    menuItemsHot = menuhot.objects.all
    menuItemsjuice = juice.objects.all
    menuSpecial = special.objects.all

    context = {

        'itemscold': menuItemsCold,
        'itemshot': menuItemsHot,
        'itemsjuice': menuItemsjuice,
        'itemspecial': menuSpecial

        }
    return render(requests, 'menu/index.html',context)
