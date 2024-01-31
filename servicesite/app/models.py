from django.db import models

# Create your models here.

class contact_details(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    mobile=models.BigIntegerField()
    message=models.TextField()    
    def __ste__(self):
        return self.name
    
    # super user name Theju
    # password 1234