from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 100, unique=True)
    description= models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="SubCatergories")
    
    def __str__(self):
        return f"{self.name} ({self.category.name})"