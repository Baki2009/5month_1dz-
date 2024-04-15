from django.contrib import admin

from apps.post.models import Car

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')