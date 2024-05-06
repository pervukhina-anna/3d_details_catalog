from rest_framework import serializers
from .models import *

#Сериализатор UserCart хранит информацию о деталях, добавленных в корзину пользователем.
class UserCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCart
        fields = '__all__'

#Сериализатор OrderConfirmation представляет информацию о подтвержденном заказе.
class OrderConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderConfirmation
        fields = '__all__'


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Detail
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Users.objects.create_user(**validated_data)
        return user

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=DetailImage
        fields="__all__"


class Detail3DSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail3D
        fields = "__all__"

#
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

#
class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = "__all__"





    #Вместо изображения получаем url изображения
    # def get_photo_url(self, obj):
    #     request=self.context.get('request')
    #     photo_url=obj.image_file.url
    #     return request.build_absolute_url(photo_url)

# class UsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = "__all__"
#         extra_kwargs = {'password': {'write_only': True}}
#
#
#     #Создание нового пользователя
#     # def create(self, validated_data):
#     #     user = Users.objects.create_user(**validated_data)
#     #     return user