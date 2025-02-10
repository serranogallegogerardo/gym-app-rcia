from django.contrib import admin

# Register your models here.
#clients/admin.py

from django.contrib import admin
from .models import Client, Routine, Payment, ActivityLog

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'gender', 'weight', 'height')

@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'date_created')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('client', 'amount', 'payment_date', 'due_date', 'is_paid')
    list_filter = ('is_paid',)

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('client', 'date', 'activity')
