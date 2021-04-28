from django.contrib import admin
from django.conf.urls import url
from reviews.views import ProductViewSet,ImageViewSet
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Product Review Backend",
      default_version='v1',
      description="Product Review API",
      terms_of_service="https://anon.com/policies/terms/",
      contact=openapi.Contact(email="harsh@harsh.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='Product')
router.register(r'image',ImageViewSet,basename='imagess')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'info', include(router.urls)),
    path('auth/',include('authe.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    