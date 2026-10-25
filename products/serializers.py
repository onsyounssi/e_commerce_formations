from rest_framework import serializers
from .models import Products, Images

class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model =Products
        fields = '__all__'

class ImagesSerializer(serializers.ModelSerializer):
    class Meta :
        model = Images 
        fields =['image_url', 'product']
        
class AllProductSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only= True)
    class Meta :
        model = Products
        fields = '__all__'
