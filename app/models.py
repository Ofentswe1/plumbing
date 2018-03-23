from django.db import models
from django.core.models import User
# Create your models here.
class Bookings(models.Model):
    username = models.ForeignKey(User)
    order_date = models.DateTimeField(default='timestamp')
    price = models.FloatField(default=0.00)
