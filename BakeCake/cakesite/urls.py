from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [path('', views.constructor, name='index'),
               path('profile', views.show_profile, name='profile'),
               path('signin', views.make_account, name='signin'),
               path('checkout', views.show_checkout, name='checkout'),
               path('statistics', views.export_statistics, name='statistics'),
               path('login/', views.user_login, name='login'),
               path('register/', views.register, name='register'),
               path('create_cake', views.create_cake, name='create_cake')
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
