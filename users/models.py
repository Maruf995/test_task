from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=100)
    number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.username}'
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("customer-profile")

class Freelancer(models.Model):
    username = models.CharField(max_length=100)
    number = models.IntegerField()
    email = models.EmailField()
    experience = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.username}'
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("freelancer-profile")

class Task(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=10000)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("freelancer-profile")