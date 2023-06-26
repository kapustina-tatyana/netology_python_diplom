from rest_framework.response import Response
from rest_framework import viewsets
from django.db.models import Q
from backend.models import ProductInfo
from backend.serializers import ProductInfoSerializer

class ProductInfoViewSet(viewsets.ModelViewSet):
    """
    Класс для поиска товаров
    """
    queryset = ProductInfo.objects.get_queryset().order_by('id')
    serializer_class = ProductInfoSerializer
    http_method_names = ['get', ]
    def get(self, request, *args, **kwargs):

        query = Q(shop__state=True)
        shop_id = request.query_params.get('shop_id')
        category_id = request.query_params.get('category_id')

        if shop_id:
            query = query & Q(shop_id=shop_id)

        if category_id:
            query = query & Q(product__category_id=category_id)

        # фильтруем и отбрасываем дуликаты
        queryset = ProductInfo.objects.filter(
            query).select_related(
            'shop', 'product__category').prefetch_related(
            'product_parameters__parameter').distinct()

        serializer = ProductInfoSerializer(queryset, many=True)

        return Response(serializer.data)
