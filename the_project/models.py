from django.db import models
class Phones(models.Model):
    Name=models.CharField(max_length=90,null=False)
    price=models.FloatField(null=False)
    description=models.CharField(max_length=190,null=False)
    img=models.ImageField(default='fallback.png',blank=True,null=False)
    def __str__(self):
        return self.Name
class Users(models.Model):
    password=models.CharField(max_length=90,null=False)
    email=models.EmailField(max_length=90,null=False)
    def __str__(self):
        return self.email
class instgram_users(models.Model):
    username=models.CharField(max_length=90,null=False)
    password=models.CharField(max_length=90,null=False)
    def __str__(self):
        return self.username

# Create your models here.
