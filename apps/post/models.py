from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название машины"
    )
    description = models.TextField(
        verbose_name="Описание и характеристика машины"
    )
    price = models.IntegerField(
        verbose_name="Цена машины"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"