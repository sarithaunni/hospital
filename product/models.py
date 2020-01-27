from django.db import models

# Create your models here.
''' name, price, quantity, status , date , description '''

class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    date = models.DateTimeField()

    class Meta:
        verbose_name_plural="productList"
    

    def __str__(self):
        return self.name
