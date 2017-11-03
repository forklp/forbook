from django.db import models

# Create your models here.
class Books(models.Model):
    bookname = models.CharField(max_length=64,default='BookName')
    model_pic = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    number = models.CharField(max_length=32,default='Number')
    pub_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.bookname

class comment(models.Model):
    account = models.CharField(max_length=32, default='Name')
    contents = models.TextField(null=True)
    bookname = models.CharField(max_length=64,default='Name')
    pub_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.contents