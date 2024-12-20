from django.contrib import admin
from .models import CustomUser, Brand, Laptop, Feedback
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Brand)
admin.site.register(Laptop)
admin.site.register(Feedback)
