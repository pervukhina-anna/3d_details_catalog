from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import *

class LoginUserForm(AuthenticationForm):
    username=forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class':'form-input'}))
    #email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))

class AddPostForm(forms.ModelForm):
    # name=forms.CharField(max_length=255, label="Название детали")
    # author=forms.ModelChoiceField(queryset=Users.objects.all(),empty_label="без автора",required=False,)
    # project=forms.ModelChoiceField(queryset=Users.objects.all(),empty_label="без автора",required=False,)
    # a2v_id='уникальный id'
    # description='описание'
    # image_1='картинка 1'
    # image_2='картинка 2'
    # image_3='картинка 3'
    # image_4='картинка 4'
    # model_file='файл модели'
    class Meta:
        model = Detail
        fields="__all__"
        #fields = ['name', 'author', 'project' ,'a2v_id','description']
