from rest_framework import serializers 
from .models import Cars_Info, CarPhoto

class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhoto
        fields = ['photo']


class Cars_Serializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()

    class Meta:
        model = Cars_Info
        fields = ['Company_name', 'Car_model_name', 'status', 'price', 'production_year',
                  'Body_styel','Drive', 'Vehicle_Type','Cylinders_type' ,'Keys',
                  'control_type',
                  'mileage', 'Car_Color', 'Fuel_Type', 'description', 'engine_capacity', 'photos']
    
    def get_photos(self, obj):
        request = self.context.get('request')
        return [request.build_absolute_uri(photo.photo.url) for photo in obj.photos.all()]
    
    