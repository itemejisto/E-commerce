from django.db import models
from django.urls import reverse
from django.utils.text import slugify



# Create your models here.
class categories(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True,blank=True)

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])

class shop(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True,blank=True)
    desc=models.TextField()
    img=models.ImageField(upload_to="images",null=True, blank=True)
    price=models.IntegerField()
    # category=models.CharField(max_length=50,null=True,blank=True)
    stock=models.IntegerField(null=True, blank=True)
    available=models.BooleanField(null=True, blank=True)
    category=models.ForeignKey(categories, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)