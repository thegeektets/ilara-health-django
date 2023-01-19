from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

    def create(self, validated_data):
        category_name = validated_data.get('name', None) 
        
        if category_name is None:
            raise serializers.ValidationError(
                {'category': 'This field is required.'})
        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            raise serializers.ValidationError({'category': 'Invalid category id'})
        category = Category.objects.create(**validated_data)
        return category


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'quantity', 'description', 'category')

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category_name = category_data.get('name', None) 
        
        if category_name is None:
            raise serializers.ValidationError(
                {'category': 'This field is required.'})
        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            raise serializers.ValidationError({'category': 'Invalid category id'})
        product = Product.objects.create(category=category, **validated_data)
        return product
    
    def update(self, instance, validated_data):
        category_data = validated_data.pop('category')
        category_name = category_data.get('name',None)
        if category_name is None:
            raise serializers.ValidationError({'category': 'This field is required.'})
        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            raise serializers.ValidationError({'category': 'Invalid category id'})
        instance.category = category
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
