from rest_framework import serializers
from orderApp.models import OrderProduct, OrderService


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('product', 'payment_type', 'amount')
        read_only_fields = ('customer', 'status', 'order_date')

    def create(self, validated_data):
        validated_data['customer'] = self.context['request'].user
        product = validated_data['product']
        amount = validated_data['amount']

        if OrderProduct.status == '2':
            if product.stock_quantity < amount:
                raise serializers.ValidationError("Not enough stock for this product.")
            product.stock_quantity -= amount
            product.save()

        return super().create(validated_data)

class OrderServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderService
        fields = ('service', 'payment_type')
        read_only_fields = ('customer', 'status')

    def create(self, validated_data):
        validated_data['customer'] = self.context['request'].user
        return super().create(validated_data)

