from django.contrib import admin
from .models import Order, OrderLine, Product, Status

class OrderLineInLine(admin.TabularInline):
    model = OrderLine
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date', 'status']
    inlines = [OrderLineInLine]

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)
admin.site.register(Product)
admin.site.register(Status)
