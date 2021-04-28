from .serializers import ProductSerializer,ImageSerializer
from .models import Product,Images
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_flex_fields.views import FlexFieldsMixin,FlexFieldsModelViewSet
from rest_flex_fields import is_expanded
from rest_framework.permissions import IsAuthenticated,AllowAny




class ProductViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permit_list_expands = ['category','sites', 'comments', 'sites.company', 'sites.productsize']
# permit_list_expands used to hide credentials or to restrict client searches by allowing specific fields to be included as search params.
    filterset_fields=('category',)
    
class ImageViewSet(FlexFieldsModelViewSet):

    serializer_class = ImageSerializer
    queryset = Images.objects.all()
    permission_classes=[IsAuthenticated]


