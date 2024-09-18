from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import *

class LoginUserForm(AuthenticationForm):
    username=forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class':'form-input'}))
    #email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))

class AddPostForm(forms.ModelForm):
    # name=forms.CharField(label='Название детали' ,widget=forms.TextInput(attrs={'class':'form-input'}))
    # author=forms.CharField(label='Автор' ,widget=forms.TextInput(attrs={'class':'form-input'}))
    # project=forms.(label='Автор' ,widget=forms.TextInput(attrs={'class':'form-input'}))
    # a2v_id=
    # description=
    # image_1=
    # image_2 =
    # image_3 =
    # image_4 =
    # model_file =
    class Meta:
        model= Detail
        fields=['name','author','project','a2v_id','description','image_1','image_2','image_3','image_4','model_file',]

class MakeOrderForm(forms.Form):
    a2v_id=forms.CharField(label='a2v_id'
                           ,widget=forms.TextInput(attrs={'class':'form-input'}))
    detail_name=forms.CharField(label='Название детали')
    counted=forms.CharField(label='Кол-во')
    user = forms.CharField(label='пользователь')
    location = forms.CharField(label='Локация')
    status = forms.CharField(label='Статус')

    # class Meta:
    #     model=Orders
    #     fields=['a2v_id','detail_name','counted','user','location','status','added_date']
