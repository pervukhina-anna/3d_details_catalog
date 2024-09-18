from rest_framework import serializers
from .models import *


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Detail
        fields=('id','name','author','added_date','project','a2v_id','description','image_1',
                'image_2','image_3','image_4','model_file')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields=('id','a2v_id','detail_name','counted','user','location','status','added_date')