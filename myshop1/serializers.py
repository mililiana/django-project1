from rest_framework import serializers
from .models import User, Item, OrderItem

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'size', 'color']



class OrderItemSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'date', 'amount', 'user', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        order_item = OrderItem.objects.create(**validated_data)

        for item_data in items_data:
            Item.objects.create(order_item =order_item , **item_data)

        return order_item
class UserSerializer(serializers.ModelSerializer):
    # orders = OrderItemSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'date_of_birth', 'contact_number']

    # def create(self, validated_data):
    #     orders_data = validated_data.pop('orders', [])
    #     user = User.objects.create(**validated_data)
    #
    #     for order_data in orders_data:
    #         OrderItem.objects.create(user=user, **order_data)
    #
    #     return user
