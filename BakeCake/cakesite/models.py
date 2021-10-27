from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import AbstractUser


class Component(models.Model):
    LEVEL = 'LV'
    FORM = 'FM'
    TOPPING = 'TP'
    BERRIES = 'BR'
    DECORATION = 'DC'
    COMPONENT_TYPE_CHOICES = [
        (LEVEL, 'Уровень'),
        (FORM, 'Форма'),
        (TOPPING, 'Топпинг'),
        (BERRIES, 'Ягоды'),
        (DECORATION, 'Декор'),
        
    ]
    name = CharField(
        'название',
        max_length=100,
    )
    price = IntegerField(
        'цена',
        validators=[MinValueValidator(0)]
    )
    component_type = CharField(
        max_length=2,
        choices=COMPONENT_TYPE_CHOICES
    )
    is_vegan = BooleanField(
        'Веганское блюдо',
        default=False
    )
    contain_
    class Meta:
        verbose_name = 'Компонент'
        verbose_name_plural = 'Компоненты'


class CustomUser(AbstractUser):
    address = CharField(
        'адрес доставки',
        blank=True,
    )
    first_name = CharField(
        'Имя',
        max_length=50,
    )
    second_name = CharField(
        'Фамилия',
        max_length=64,
    )
    consent_with_pd = BooleanField(
        'Согласие на обработку персональных данных',
        default=False,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Order(models.Model):

    # добавить вид заказа: торт, капкейп и т.п. Но пока работаем только с тортом для МВП

    customer = ForeignKey(
        CustomUser,
        on_delete=CASCADE,
        related_name='orders',
        verbose_name='Заказчик')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'