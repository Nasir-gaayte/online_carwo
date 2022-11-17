from django.db import models
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.


class CategoryModel(models.Model):
    name=models.CharField(max_length=50)
    
    
    def __str__(self) -> str:
        return self.name
    
    
    
class PremotionModel(models.Model):
    image = models.ImageField()
    description = models.TextField(max_length=250)
    
    def __str__(self) -> str:
        return self.description    
    
    
class ShopModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    title_image = models.ImageField(null=False, blank=False, upload_to='images/')
    images=models.ImageField(null=True, blank=True, upload_to='images/')
    description= models.TextField()
   
    
    
    def __str__(self) -> str:
        return f"{self.title}of the {self.category} Category"
      