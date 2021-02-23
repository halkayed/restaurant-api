from rest_framework import serializers

from .models import Customer, Menu, Item


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

        
        
        
class MenuSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    
    class Meta:
        model = Menu 
        fields = ['theme','items']


class CustomerMenuSerializer(serializers.ModelSerializer):
    
    menus = MenuSerializer(many=True)
    class Meta:
        model = Customer
        fields = ['name','address','mobile','menus']