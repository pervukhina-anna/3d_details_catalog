from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.



#Модель деталь
class details(models.Model):
    title=models.CharField("Название детали", max_length=255)
    author=models.ForeignKey('User', on_delete=models.CASCADE)
    add_date=models.DateTimeField("дата публикации", auto_now_add=True)
    a2v=models.CharField("Проект", max_length=255)
    description=models.TextField("Описание")

    def __str__(self):
        return self.title

#Модель Изображение детали
class image_detail(models.Model):
    detail_id = models.ForeignKey('details', on_delete=models.CASCADE)
    detail_img = models.ImageField(upload_to='media/', height_field=None, width_field=None)



#Модель Пользователя
class User(models.Model):
    last_name = models.CharField('Фамилия', max_length=70)
    name = models.CharField('Имя', max_length=70)
    email = models.EmailField("E-mail")
    phone_number = models.CharField('Телефон', max_length=12)
    telegram_id = models.BigIntegerField('телеграмм_id')
    location = models.CharField('Локация', max_length=100)

    #Здесь будет ChoiceField(Админ, сотрудник т.д.)
    role = models.CharField('Роль', max_length=100)

    def __str__(self):
        return self.email


#Модель заказа
class orders(models.Model):
    user_id = models.ForeignKey('user', on_delete=models.CASCADE, null=True)

    #поставить ChoiceField
    status= models.TextField("статус заказа")
    data_order=models.DateTimeField("дата заказа")

    def __str__(self):
        return self.id



#Модель заказ-деталь
class orders_details(models.Model):
    orders_id = models.ForeignKey('orders', on_delete=models.CASCADE, null=True)
    details_id= models.ForeignKey('details', on_delete=models.CASCADE, null=True)
    amount=models.IntegerField('количество', validators=(MinValueValidator(1, message='Количество не может быть меньше 1!'),))



