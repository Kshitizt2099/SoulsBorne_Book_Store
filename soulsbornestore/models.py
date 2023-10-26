from django.db import models
from datetime import datetime

# Create your models here.
class customusers(models.Model):
    id=models.CharField(primary_key=True,max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    Emailid=models.CharField(null=True,max_length=100,blank=True)
    def __str__(self):
        return self.id
    
class Adminusers(models.Model):
    id=models.CharField(primary_key=True,max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    Emailid=models.CharField(null=True,max_length=100,blank=True)
    def __str__(self):
        return self.id
    
class productslist(models.Model):
    id=models.CharField(primary_key=True,max_length=50)
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)
    Genre=models.CharField(max_length=10)
    Year=models.CharField(max_length=10)
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    def __str__(self):
        return self.name
class CartCheckout(models.Model):
    user_id=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=10)
    qty=models.IntegerField(default=1)
    def __str__(self):
        return self.name
class newlist(models.Model):
  
    user_id=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=10)
    def __str__(self):
        return self.name
class CartCheckoutmk85(models.Model):
    p_id=models.CharField(max_length=50)
    user_id=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=10)
    qty=models.IntegerField(default=1)
    def __str__(self):
        return self.name
class productslist1(models.Model):
    id=models.CharField(primary_key=True,max_length=50)
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)
    Genre=models.CharField(max_length=10)
    Year=models.CharField(max_length=10)
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    def __str__(self):
        return self.name
    
class review(models.Model):
    userid=models.TextField(max_length=10)
    desc=models.TextField(max_length=100)
    name=models.TextField(max_length=50)
    pid=models.TextField(max_length=50)
    score=models.IntegerField(default=1,null=True)
    def __str__(self):
        return self.userid
class sales(models.Model):
    products=models.TextField(max_length=10)
    total=models.IntegerField(default=1)
    username=models.TextField(max_length=50)
    date=models.DateField()
    
    def __str__(self):
        return self.userid
class sales1(models.Model):
    products=models.TextField(max_length=100)
    total=models.IntegerField(default=1)
    username=models.TextField(max_length=50)
    date=models.DateField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.username
class reviewmk1(models.Model):
    username=models.CharField(max_length=100)
    userid=models.TextField(max_length=10)
    desc=models.TextField(max_length=100)
    name=models.TextField(max_length=50)
    pid=models.TextField(max_length=50)
    score=models.IntegerField(default=1,null=True)
    def __str__(self):
        return self.userid