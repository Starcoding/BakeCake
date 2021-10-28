from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [path('', views.show_cake, name='index'),
               path('profile', views.show_profile, name='profile'),
               path('signin', views.make_account, name='signin'),
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
