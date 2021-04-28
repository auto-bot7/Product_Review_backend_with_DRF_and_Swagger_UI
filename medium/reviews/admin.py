from django.contrib import admin
from .models import Images,Product,Category,Company,Comment,ProductSize,ProductSite
from django.contrib.auth.models import Group

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content', )
    list_filter = ('category', 'name' )

    
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(ProductSize)
admin.site.register(ProductSite)
admin.site.register(Comment)
admin.site.register(Images)

admin.site.unregister(Group)
# To unregister default models in admin site