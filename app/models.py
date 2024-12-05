from django.db import models

# Модель услуги
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.title


# Пользователь
class User(models.Model):
    user_name = models.CharField(max_length=255)
    number = models.CharField(max_length=16, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.user_name

# Модель заказа
class Order(models.Model):
    service = models.ForeignKey(Service, related_name='orders', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.id} - {self.customer.user_name} - {self.service.title}'
