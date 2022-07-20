from django.contrib import admin

# import your models here
from .models import Germ, Treatment, Symptom, Photo

# Register your models here.
admin.site.register(Germ)
admin.site.register(Treatment)
admin.site.register(Symptom)
admin.site.register(Photo)