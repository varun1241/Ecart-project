from django.db import models

from django.db.models.signals import pre_save
from django.dispatch import receiver  
# Create your models here.
class Product(models.Model):

    product_id=models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    strap_color=models.CharField(max_length=100)
    highlights=models.CharField(max_length=100)
    image =  models.ImageField(upload_to="product")
    status=models.BooleanField()

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(product_id__in =ids)


       

    def __str__(self):
        return self.product_name




def task_handler(sender,instance,**kwargs):

    print("you are in")
    print(instance)


pre_save.connect(task_handler, sender=Product)




class Student(models.Model):

    name=models.CharField(max_length=10)
    age=models.ImageField()
    address=models.TextField()


    def __str__(self):
        return self.name