from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, IntegerField, TextField, DateTimeField
from django.db.models.fields.related import ForeignKey
from phonenumber_field.modelfields import PhoneNumberField


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
    contains_sugar = BooleanField(
        'Содержит сахар',
        default=False
    )

    def __str__(self):
        return f'{self.name}{self.price}'

    class Meta:
        verbose_name = 'Компонент'
        verbose_name_plural = 'Компоненты'


class CustomUser(AbstractUser):
    address = CharField(
        'адрес доставки',
        blank=True,
        max_length=120
    )
    first_name = CharField(
        'Имя',
        max_length=50,
    )
    second_name = CharField(
        'Фамилия',
        max_length=64,
    )
    phone_number = CharField(
        verbose_name='Номер телефона',
        max_length=20,
        help_text='+79991234567',
        default=''
    )
    clear_phone_number = PhoneNumberField(
        verbose_name='Нормализованный номер телефона',
        blank=True
    )
    social_id = CharField(
        max_length=50,
        verbose_name='Ссылка на соцсеть',
        null=True,
        blank=True)
    consent_with_pd = BooleanField(
        'Согласие на обработку персональных данных',
        default=False,
    )

    def __str__(self):
        return f'{self.first_name}{self.second_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Order(models.Model):
    # добавить вид заказа: торт, капкейп и т.п. Но пока работаем только с тортом для МВП

    customer = ForeignKey(
        CustomUser,
        on_delete=CASCADE,
        related_name='orders',
        verbose_name='Заказчик'
    )

    lettering = TextField(
        max_length=100,
        verbose_name='Надпись',
        help_text='Мы можем разместить на торте любую надпись, например: «С днем рождения!»',
        null=True
    )

    delivery_date = DateTimeField(
        verbose_name='Дата доставки',
        blank=True,
        auto_now=True
    )

    delivery_time = DateTimeField(
        verbose_name='Время доставки',
        blank=True,
        auto_now=True
    )

    is_ordered = BooleanField(
        verbose_name='Заказ сделан',
        default=False
    )

    date_ordered = DateTimeField(
        verbose_name='Дата создания заказа',
        null=True
    )

    comment = TextField(
        max_length=500,
        verbose_name='Комментарий к заказу',
        null=True)

    promo_code = CharField(
        max_length=15,
        verbose_name='Промокод',
        null=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
