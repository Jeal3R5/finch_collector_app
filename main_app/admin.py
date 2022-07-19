from django.contrib import admin

# import your models here
from .models import Germ, Treatment

# Register your models here.
admin.site.register(Germ)
admin.site.register(Treatment)

