from rest_framework.serializers import ModelSerializer
from .models import car_details 

class carserializer(ModelSerializer):
    class Meta:
        model=car_details
        fields=['company','model','total_km','fuel_type','car_image']


class mainserializer(ModelSerializer):
    class Meta:
        model=car_details
        fields='__all__'

        