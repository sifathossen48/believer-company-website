from django.db import models

# Create your models here.
class GetQuote(models.Model):
    company = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    def __str__(self):
        return self.company