from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# superuserpass - 12345

class Category(models.Model):
    name = models.CharField(max_length= 255)
    
    class Meta:
        ordering = ('name',)  # This means that when you query the Category model, the results will be ordered by the name field in ascending order by default.
        verbose_name_plural = 'Categories'  #  This changes the plural name of the model in the Django admin interface from the default (Categorys) to Categories.
        
    def __str__(self):
        """This method defines how the Category object should be represented as a string.
        When you print a Category instance or view it in the Django admin interface, 
        it will display the value of the name field.
        """
        return self.name
    

class Item(models.Model):
    category = models.ForeignKey(Category, related_name= 'items', on_delete= models.CASCADE)
    name = models.CharField(max_length= 255)
    description = models.TextField(blank= True, null= True)
    price = models.FloatField()
    image = models.ImageField(upload_to= 'item_images', blank= True, null= True)
    isSold = models.BooleanField(default= False)
    created_by = models.ForeignKey(User, related_name= 'items', on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)  # the auto_now_add=True argument means that the field is automatically set to the current date and time when the Item object is created.

    def __str__(self):
        return self.name