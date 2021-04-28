
from .models import Product, Category, ProductSize, ProductSite, Company, Comment,Images
from rest_flex_fields import FlexFieldsModelSerializer
from django.contrib.auth.models import User
from versatileimagefield.serializers import VersatileImageFieldSerializer







class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        #Globally defined sizes in VERSATILEIMAGEFIELD_RENDITION_KEY_SETS in settings.py
        # sizes =[
        #     ('full_size','url'),
        #     ('thumbnail','thumbnail__100x100'),
        # ]
        sizes='product_headshot'
    )

    class Meta:
        model =Images
        fields = '__all__'

#Nested Dynamic Serializers
# In these serializers the user/client can modify the results acoording to his needs dynamically rather than seeing all the
# nested relationships as  default in the api page.
# Three default search params are -
# expand - to expand a relation field class http://127.0.0.1:8000/product/?expand=category
# fields - to select fields to be expanded  http://127.0.0.1:8000/product/?expand&fields=created,updated,sites.url
# Using expand & fields togetherhttp://127.0.0.1:8000/cat/?expand=products&fields=pk,products.content
# omit - to remove unwanted fields
# http://127.0.0.1:8000/cat/?expand=products&omit=products.content


class CompanySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Company
        fields = ['pk','name','url']

class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['pk','name']
        expandable_fields ={
            'products':('reviews.ProductSerializer',{'many':True})
             }
#reviews.serializer_name is generally used to avoid any kind of cyclic import error.
#{'many':True} has to be returned as a parameter for working on serializer classes with multiple instances.

class ProductSizeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['pk','name']

class ProductSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['pk','content','content', 'created', 'updated']
        expandable_fields={
            'image':('reviews.ImageSerializer',{'many':True}),
            'category':('reviews.CategorySerializer', {'many':True}),
            'sites':('reviews.ProductSiteSerializer',{'many':True}),
            'comments':('reviews.CommentSerializer',{'many':True}),
        }

class ProductSiteSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSite
        fields = ['pk', 'name', 'price', 'url', 'created', 'updated']
        expandable_fields = {
            'product':('reviews.ProductSerializer', {'many':True}),
            'productsize': ('reviews.ProductSizeSerializer',{'many':True}),
            'company' : ('reviews.CompanySerializer', {'many':True})
        }
class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'title', 'content', 'created', 'updated']
        expandable_fields = {
            'product': 'reviews.CategorySerializer',
            'user': 'reviews.UserSerializer'
        }