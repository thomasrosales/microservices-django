from django.contrib import admin
from user.models import UserProfile
from pizza.models import Pizzeria, Pizza, Like

# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Pizzeria)
admin.site.register(Pizza)
admin.site.register(Like)
