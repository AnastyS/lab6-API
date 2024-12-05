
from app.views import ServiceViewSet, UserViewSet, OrderViewSet  # Импортируем view из приложения
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


# Настройка схемы Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Service Marketplace",
        default_version='v1',
        description="You can choose any service",
    ),
    public=True,
    # permission_classes=[permissions.IsAuthenticated],  # Доступ к Swagger только для авторизованных
)


# Создаем роутер и регистрируем viewsets
router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'user', UserViewSet)
router.register(r'order', OrderViewSet)

# Основные маршруты
urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('api/', include(router.urls)),  # API маршруты через роутер
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    
]
