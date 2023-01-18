from django.db import models

class Information(models.Model):
        name=models.CharField (max_length=50)
        designation=models.CharField (max_length=200)
        qualification=models.CharField (max_length=200)
        experiance=models.CharField (max_length=100)
        expetarea=models.CharField (max_length=100)
        email=models.EmailField(max_length=254)
        mob=models.CharField(max_length=20)
        image=models.ImageField(upload_to="static\database_images",null=True)
        pdf=models.FileField(upload_to="static\database_doc",null=True)


        def __str__(self):
                return self.name
# Create your models here.
