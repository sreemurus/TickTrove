from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('product_by_category', args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='Product', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('product_details', args=[self.category.slug, self.slug])



