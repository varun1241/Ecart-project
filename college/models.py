from django.db import models

# Create your models here.



class College(models.Model):
    college_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=10)
    address=models.TextField()


    def __str__(self):
        return self.name