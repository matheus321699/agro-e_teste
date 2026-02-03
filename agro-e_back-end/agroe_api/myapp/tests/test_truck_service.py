import pytest
from django.core.exceptions import ValidationError
from unittest.mock import patch

from myapp.truck_service import TruckService
from myapp.models import Truck


@pytest.mark.django_db
class TestTruckService:

    def test_create_truck_success(self):
        data = {
            "license_plate": "ABC1D23",
            "brand": "Volvo",
            "model": "Volvo FH",
            "manufacturing_year": 2022,
            "fipe_price": 450000,
        }

        with patch(
            "myapp.truck_service.FipeService.validate_model_exists",
            return_value={"name": "Volvo FH", "code": "123"},
        ):
            truck = TruckService.create_truck(data)

            assert isinstance(truck, Truck)
            assert truck.license_plate == "ABC1D23"

    def test_create_truck_duplicate_license_plate(self):
        Truck.objects.create(
            license_plate="ABC1D23",
            brand="Volvo",
            model="Volvo FH",
            manufacturing_year=2022,
            fipe_price=450000,
        )

        data = {
            "license_plate": "ABC1D23",
            "brand": "Volvo",
            "model": "Volvo FH",
            "manufacturing_year": 2022,
            "fipe_price": 450000,
        }

        with pytest.raises(
            ValidationError,
            match="Já existe um caminhão com essa placa."
        ):
            TruckService.create_truck(data)

    def test_create_truck_invalid_fipe_model(self):
        data = {
            "license_plate": "XYZ9Z99",
            "brand": "Volvo",
            "model": "Modelo Inexistente",
            "manufacturing_year": 2021,
            "fipe_price": 300000,
        }

        with patch(
            "myapp.truck_service.FipeService.validate_model_exists",
            side_effect=ValidationError("Modelo inválido"),
        ):
            with pytest.raises(ValidationError, match="Modelo inválido"):
                TruckService.create_truck(data)
