from django.db import models

# Create your models here.
class User(models.Model):
    account = models.CharField(max_length=32,default='Account')
    password = models.CharField(max_length=32,default='Password')
    def __str__(self):
        return self.account

class ShoppingCart(models.Model):
    account = models.CharField(max_length=32,default='Account')
    bookname = models.CharField(max_length=64, default='BookName')
    model_pic = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    number = models.CharField(max_length=32, default='Number')