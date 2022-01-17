from django.db import models

# Create your models here.

class Type(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi
class Product(models.Model):
    nomi = models.CharField(max_length =30)
    narxi = models.IntegerField()
    tur  = models.ForeignKey(Type,on_delete=models.CASCADE)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media',null=True,blank=True)
    rasm3 = models.ImageField(upload_to='media',null=True,blank=True)

class New(models.Model):
    nomi = models.CharField(max_length=30)
    malumot = models.TextField()
    rasm = models.ImageField(upload_to='media')

class Sotib_olingan_maxsulotlar(models.Model):
    nomi = models.CharField(max_length=30)
    narxi = models.IntegerField()
    miqdori = models.IntegerField()
    mijoz_username = models.CharField(max_length=20)
    mijoz_id = models.IntegerField()

    
class Murojatlar(models.Model):
    ism = models.CharField(max_length=30)
    mail = models.EmailField(max_length=30)
    tel = models.CharField(max_length=20)
    matn = models.TextField()

class Comment(models.Model):
    ism = models.CharField(max_length=30)
    mail = models.EmailField(max_length=30)
    tel = models.CharField(max_length=20)
    matn = models.TextField()
    tur = models.CharField(max_length=30)

