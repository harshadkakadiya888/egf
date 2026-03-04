from django.db import models


# Create your models here.

# =========================
# Customer Address Model
# =========================
class Address(models.Model):
    name1 = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name