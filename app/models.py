from django.db import models
from django.contrib.auth.models import User

# Модель услуги
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.title

# Модель отзыва
class Review(models.Model):
    service = models.ForeignKey(Service, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.service.title} by {self.user.username}'

# Модель заказа
class Order(models.Model):
    service = models.ForeignKey(Service, related_name='orders', on_delete=models.CASCADE)
    customer = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    provider = models.ForeignKey(User, related_name='provided_orders', on_delete=models.CASCADE)

    def __str__(self):
        return f'Order #{self.id} - {self.service.title}'
