from django.shortcuts import render
from .models import Component, CustomUser, Order, Product


def show_cake(request):
    components = Component.objects.all()
    return render(request, 'index.html')


def show_profile(request):
    users = CustomUser.objects.all()
    orders = Order.objects.all()
    return render(request, 'profile.html')


def get_signup(request):
    users = CustomUser.objects.all()
    return render(request, 'signup.html')


def make_account(request):
    return render(request, 'signin.html')
