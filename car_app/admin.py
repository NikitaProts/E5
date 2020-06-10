from django.contrib import admin
from car_app.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
