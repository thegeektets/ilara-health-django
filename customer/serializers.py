from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(required=False, queryset=User.objects.all())

    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        if 'user' not in validated_data:
            user = User.objects.create(username=validated_data['email'])
            validated_data['user'] = user
        return super().create(validated_data)
