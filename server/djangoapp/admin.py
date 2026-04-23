from django.contrib import admin
from .models import CarMake, CarModel


class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id')
    search_fields = ('name',)
    list_filter = ('type', 'year', 'car_make')


class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'created_at')
    search_fields = ('name',)
    inlines = [CarModelInline]


admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)