from django.db import models

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
