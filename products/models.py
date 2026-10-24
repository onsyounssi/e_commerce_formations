from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subcategory = models.ManyToManyField(
        "category.SubCategory",
        related_name= "products"
    )
    def __str__(self):
        
        return self.name
    
class Images(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="image")
    image_url = models.CharField(max_length=800)
    
    class Meta:
     db_table = "images"   