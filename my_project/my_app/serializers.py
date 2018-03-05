from rest_framework import serializers
from .models import Purchase, Product


class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    product_names = serializers.ReadOnlyField(source='get_names')
    total = serializers.ReadOnlyField(source='total_price')

    class Meta:
        model = Purchase
        fields = ('url', 'id', 'products', 'product_names', 'time', 'total')
