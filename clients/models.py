from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Client(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    weight = models.FloatField()  # Peso en kg
    height = models.FloatField()  # Altura en cm
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Routine(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='routines')
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.client.user.username}"

class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(default=now)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment: {self.client.user.username} - {self.amount} - {'Paid' if self.is_paid else 'Pending'}"

class ActivityLog(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='activity_logs')
    date = models.DateField(default=now)
    activity = models.TextField()

    def __str__(self):
        return f"{self.date} - {self.client.user.username}"
