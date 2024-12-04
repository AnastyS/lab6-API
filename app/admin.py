from django.contrib import admin

# Импорт нужных моделей из текущего каталога (".")
from .models import Service, Review

# Регистрация моделей для административного сайта
admin.site.register(Service)
admin.site.register(Review)
