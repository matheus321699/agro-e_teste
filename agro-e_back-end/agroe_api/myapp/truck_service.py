from django.core.exceptions import ValidationError
from .models import Truck
from .fipe_service import FipeService


class TruckService:

    @staticmethod
    def create_truck(data: dict) -> Truck:
        if Truck.objects.filter(license_plate=data["license_plate"]).exists():
            raise ValidationError("Já existe um caminhão com essa placa.")


        brand_fipe_id = 59

        fipe_model = FipeService.validate_model_exists(
            brand_id=brand_fipe_id,
            model_name=data["model"]
        )

        # data["fipe_model_code"] = fipe_model["code"]

        return Truck.objects.create(**data)
