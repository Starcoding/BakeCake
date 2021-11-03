from django.http.response import HttpResponse
import pandas as pd
import numpy as np
from django.shortcuts import render
from .models import Component, CustomUser, Order, Product
from .admin import OrderResourse
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def constructor(request):
    components = list(Component.objects.all())
    levels = [component for component in components if component.component_type=='LV']
    berries = [component for component in components if component.component_type=='BR']
    decorations = [component for component in components if component.component_type=='DC']
    toppings = [component for component in components if component.component_type=='TP']
    form = [component for component in components if component.component_type=='FM']
    components = {
        'levels': levels,
        'berries': berries,
        'decorations': decorations,
        'toppings': toppings,
        'form': form,
    }
    print(components)
    return render(request, 'constructor.html', context= {'components': components})


def show_profile(request):
    users = CustomUser.objects.all()
    orders = Order.objects.all()
    return render(request, 'profile.html')


def get_signup(request):
    users = CustomUser.objects.all()
    return render(request, 'signup.html')


def make_account(request):
    return render(request, 'signin.html')


def show_checkout(request):
    return render(request, 'checkout.html')


def export_statistics(request):
    cancelled_orders = Order.objects.filter(status='CD')
    cancelled_orders_statistics = OrderResourse().export(cancelled_orders)
    with open('Статистика.csv', 'w'):
        pass
    
    print(cancelled_orders_statistics.csv)
    # df = pd.read_csv(cancelled_orders_statistics.csv)
    # print(df)
    user_counter = CustomUser.objects.count()
    print(user_counter)
    components = list(Component.objects.all())
    for component in components:
        print(component.name, component.product.count())
    pass
    # return
    

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = request.POST
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'profile.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def create_cake(request):
    components = list(Component.objects.all())
    components_types = ['levels', 'toppings', 'decorations', 'form', 'berries']
    ids_from_form = []
    for component_type in components_types:
        ids_from_form.append(int(request.POST.get(component_type)))
    lettering = request.POST.get('lettering')
    components_for_cake = [component for component in components if component.id in ids_from_form]
    cake = Product(category='CK')
    if lettering:
        cake.lettering = lettering
        cake.price =+ 500
    else:
        cake.price = 0
    # cake.component.set(components)
    print(cake)
    return HttpResponse('ok')