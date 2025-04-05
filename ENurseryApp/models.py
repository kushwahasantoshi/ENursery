from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    address = models.CharField(max_length=255, blank=True, null=True)
    pin = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.get_full_name() if self.get_full_name() else self.username


#====================== Category Model =================

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_category():
        return Category.objects.all()


# ================ Products Model ====================

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,default='',blank=True,null=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_category_id_get_all_product(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    
    def __str__(self):
        return self.name