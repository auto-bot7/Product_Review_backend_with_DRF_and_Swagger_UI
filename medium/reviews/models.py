from django.db import models
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField,PPOIField
# Create your models here.
class Images(models.Model):
    name = models.CharField(max_length=255)
    image= VersatileImageField(
        'Images',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi=PPOIField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Image"
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    url = models.TextField()
    class Meta:
        verbose_name_plural = "Company"
    # Admin site appending 's' in beginning of each model name. Use verbose_name_plural to rectify that.
    def __str__(self):
        return self.name
    
class ProductSize(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "ProductSize"
    def __str__(self):
        return self.name
        # The __str__() method is the default human-readable representation of the object.
        #  Django will use it in many places, such as the administration site.

class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Category"
    def __str__(self):
        return self.name
          
class Product(models.Model):
    category = models.ManyToManyField(Category,related_name='products')
    image=models.ManyToManyField(Images,related_name='products')
    # on_delete is not a valid argument on a ManyToManyField.
    # TypeError: __init__() got an unexpected keyword argument 'on_delete'
    content = models.TextField()
    name =models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   
    class Meta:
        verbose_name_plural = "Product"
        ordering = ['-created']
        # The Meta class inside the model contains metadata. 

    def __str__(self):
        return self.name
    
class ProductSite(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sites', related_query_name='site')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='sites', related_query_name='site')
    productsize = models.ForeignKey(ProductSize, on_delete=models.CASCADE, related_name='sites', related_query_name='site')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    url = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "ProductSite"
    def __str__(self):
        return self.name
        verbose_name_plural = "ProductSite"

        # related_query_name enable you to use “comment” as a lookup parameter in a queryset,]
        #  like: Product.objects.filter(comment=filter_what_you_want).


class Comment(models.Model):
    product = models.ForeignKey(Product,related_name='comments', on_delete= models.CASCADE)
    user = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Comment"
    def __str__(self):
        return self.title
    
    

    