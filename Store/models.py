from django.db import models
 #https://matthiasomisore.com/web-programming/display-image-in-a-django-template-using-imagefield/
 

class Products(models.Model):
    title = models.CharField(max_length=120)
    img = models.ImageField()
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
