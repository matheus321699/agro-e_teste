from rest_framework import serializers
from .models import Truck

class TruckSerializer(serializers.ModelSerializer):

    class Meta:

        model = Truck
        fields = '__all__'
        # fields = ('id','license_plate','brand','model','manufacturing_year')