from django.contrib import admin
from .models import Siswa

models_list = [Siswa]
admin.site.register(models_list)
