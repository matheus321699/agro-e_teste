from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Truck
from .serializers import TruckSerializer
from .truck_service import TruckService

class TruckList(generics.ListCreateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            truck = TruckService.create_truck(serializer.validated_data)
        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            TruckSerializer(truck).data,
            status=status.HTTP_201_CREATED
        )





