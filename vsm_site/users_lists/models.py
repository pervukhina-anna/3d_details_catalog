from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


#модель пользователей
class Users(models.Model):
    ROLE = (
        ('user', 'Аутентифицированный пользователь'),
        ('operator', 'Оператор 3D принтера'),
        ('admin', 'Администратор')
    )
    last_name = models.CharField('Фамилия', max_length=70)
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
    name = models.CharField('Имя', max_length=70)
    # email и username - уникальные значения -> unique constraint
    email = models.EmailField('E-mail', unique=True)
    phone_number = models.CharField('Телефон', max_length=12, unique=True)
    telegram_id = models.BigIntegerField('телеграмм_id', unique=True)
    location = models.CharField('Локация', choices=CITY, max_length=100, default=0)
    role = models.CharField("Роль", choices=ROLE, max_length=120, default=0)
    password = models.CharField("Пароль", max_length=100)
    # Здесь будет ChoiceField(Админ, сотрудник т.д.)

    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'
        ordering=['last_name']




# Модель Деталей
class Detail(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)  # Предполагается, что это имя создателя 3D-модели
    added_date = models.DateField()
    PROJECT_CHOICES = (
        ('Desiro', 'Ласточка'),
        ('Velaro', 'Сапсан'),
        ('Depot', 'Депо'),
        ('Sample print', 'Пробная печать'),
    )
    project = models.CharField(max_length=100, choices=PROJECT_CHOICES)
    a2v_id = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Деталь'
        verbose_name_plural='Детали'
        ordering=['added_date']

# Модель Изображение детали
class DetailImage(models.Model):
    detail = models.ForeignKey(Detail, related_name='images', on_delete=models.CASCADE)
    image_file = models.ImageField(upload_to='detail_images/')

    def __str__(self):
        return "Изображение "+self.detail.name

    class Meta:
        verbose_name='Изображение детали'
        verbose_name_plural='Изображения деталей'

# Модель 3D детали
class Detail3D(models.Model):
    detail = models.ForeignKey(Detail, related_name='model_3d', on_delete=models.CASCADE)
    model_file = models.FileField(upload_to='detail_3d_models/')

    def __str__(self):
        return "3D-модель детали "+self.detail.name

    class Meta:
        verbose_name='Модель 3D-детали'
        verbose_name_plural='Модели 3D-деталей'



#Модель
class Order(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('processing', 'Обработка'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('canceled', 'Отменен'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'



class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='order_details', on_delete=models.CASCADE)
    detail = models.ForeignKey('Detail', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=(MinValueValidator(1, message='Количество не может быть меньше 1!'),))

    class Meta:
        verbose_name = 'Заказ-деталь'
        verbose_name_plural = 'Заказы-детали'