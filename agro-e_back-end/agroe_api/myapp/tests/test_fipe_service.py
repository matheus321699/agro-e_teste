import pytest
from django.core.exceptions import ValidationError
from django.core.cache import cache
from unittest.mock import patch

from myapp.fipe_service import FipeService

@pytest.mark.django_db
class TestFipeService:

    @patch("myapp.fipe_service.requests.get")
    def test_get_models_by_brand_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"name": "Volvo FH", "code": "123"},
            {"name": "Scania R440", "code": "456"},
        ]

        models = FipeService.get_models_by_brand(brand_id=59)

        assert len(models) == 2
        assert models[0]["name"] == "Volvo FH"

    @patch("myapp.fipe_service.requests.get")
    def test_get_models_by_brand_request_error(self, mock_get):
        mock_get.side_effect = Exception()

        with pytest.raises(ValidationError, match="Erro ao consultar a tabela FIPE."):
            FipeService.get_models_by_brand(brand_id=59)

    def test_get_models_by_brand_uses_cache(self):
        cache_key = "fipe_models_brand_59"
        cached_data = [{"name": "Modelo Cache", "code": "999"}]
        cache.set(cache_key, cached_data, timeout=60)

        models = FipeService.get_models_by_brand(brand_id=59)

        assert models == cached_data

    def test_validate_model_exists_success(self):
        with patch.object(
            FipeService,
            "get_models_by_brand",
            return_value=[
                {"name": "Volvo FH", "code": "123"},
                {"name": "Scania R440", "code": "456"},
            ],
        ):
            model = FipeService.validate_model_exists(
                brand_id=59,
                model_name="  volvo fh "
            )

            assert model["code"] == "123"

    def test_validate_model_exists_not_found(self):
        with patch.object(
            FipeService,
            "get_models_by_brand",
            return_value=[{"name": "Scania R440", "code": "456"}],
        ):
            with pytest.raises(
                ValidationError,
                match="Modelo 'Volvo FH' não encontrado na tabela FIPE."
            ):
                FipeService.validate_model_exists(
                    brand_id=59,
                    model_name="Volvo FH"
                )
