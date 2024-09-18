from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    ROLE = (
        ('user', 'Аутентифицированный пользователь'),
        ('operator', 'Оператор 3D принтера'),
        ('admin', 'Администратор')
    )
    CITY = (
        ('Podmoskovnaya', 'Подмосковная'),
        ('Andronovka', 'Андроновка'),
        ('Metallostroy', 'Металлострой'),
        ('Kaliningrad', 'Калининград'),
        ('Kryukovo', 'Крюково'),
        ('Ekaterinburg', 'Екатеринбург'),
        ('Samara', 'Самара'),
        ('Nizhny Novgorod', 'Нижний Новгород'),
        ('Chelyabinsk', 'Челябинск'),
        ('Adler', 'Адлер'),
        ('Perm', 'Пермь'),
        ('Ufa', 'Уфа')
    )
    last_name = models.CharField('Фамилия', max_length=70)
    name = models.CharField('Имя', max_length=70)
    # email и username - уникальные значения -> unique constraint
    email = models.EmailField('E-mail', unique=True)
    phone_number = models.CharField('Телефон', max_length=12, unique=True)
    # telegram_id = models.BigIntegerField('телеграмм_id', unique=True)
    location = models.CharField('Локация', choices=CITY, max_length=100, default=0)
    role = models.CharField("Роль", choices=ROLE, max_length=120, default=0)
    password = models.CharField("Пароль", max_length=100)

    # Здесь будет ChoiceField(Админ, сотрудник т.д.)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['last_name']


#Модель деталей
class Detail(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)  # Предполагается, что это имя создателя 3D-модели
    added_date = models.DateField(auto_now_add=True)
    PROJECT_CHOICES = (
        ('Desiro', 'Ласточка'),
        ('Velaro', 'Сапсан'),
        ('Depot', 'Депо'),
        ('Sample print', 'Пробная печать'),
    )

    project = models.CharField(max_length=100, choices=PROJECT_CHOICES)
    a2v_id = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)
    image_1= models.ImageField(upload_to='detail_images/')
    image_2 = models.ImageField(upload_to='detail_images/')
    image_3 = models.ImageField(upload_to='detail_images/')
    image_4 = models.ImageField(upload_to='detail_images/')
    model_file = models.FileField(upload_to='detail_3d_models/')


    def __str__(self):
        # пока оставлю вывод названия
        # но потом поменяю на название+av2_номер
        return self.name

    class Meta:
        verbose_name='Деталь'
        verbose_name_plural='Детали'
        ordering=['added_date']

class Orders(models.Model):
    ORDER_STATUS_CHOICES = [
        ('processing', 'Заказ в обработке'),
        ('in_progress', 'Заказ выполняется'),
        ('ready', 'Заказ готов'),
    ]
    CITY = (
        ('Podmoskovnaya', 'Подмосковная'),
        ('Andronovka', 'Андроновка'),
        ('Metallostroy', 'Металлострой'),
        ('Kaliningrad', 'Калининград'),
        ('Kryukovo', 'Крюково'),
        ('Ekaterinburg', 'Екатеринбург'),
        ('Samara', 'Самара'),
        ('Nizhny Novgorod', 'Нижний Новгород'),
        ('Chelyabinsk', 'Челябинск'),
        ('Adler', 'Адлер'),
        ('Perm', 'Пермь'),
        ('Ufa', 'Уфа')
    )
    # a2v_id=models.CharField(max_length=100)
    # detail_name=models.CharField(max_length=100)

    # a2v_id объединю с названием детали ибо как отдельно друг от друга из модели вызывать не умею
    detail_name=models.ForeignKey(Detail, on_delete=models.CASCADE)
    counted=models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # location=models.CharField('Локация', choices=CITY, max_length=100, default=0)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='processing')
    added_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'Заказ №{self.id}'

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'
        ordering = ['added_date']


