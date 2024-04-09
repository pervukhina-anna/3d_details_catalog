from django.contrib import admin

from .models import *

admin.site.register(Users)
admin.site.register(Detail)
admin.site.register(DetailImage)
admin.site.register(Detail3D)
admin.site.register(Order)
admin.site.register(OrderDetail)

# Register your models here.
