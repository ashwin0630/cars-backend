from rest_framework.serializers import ModelSerializer
from .models import car_details 

class carserializer(ModelSerializer):
    class Meta:
        model=car_details
        fields='__all__'


class mainserializer(ModelSerializer):
    class Meta:
        model=car_details
        fields='__all__'

        