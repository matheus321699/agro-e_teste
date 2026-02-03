import requests
from django.core.exceptions import ValidationError
from django.core.cache import cache

FIPE_BASE_URL = "https://fipe.parallelum.com.br/api/v2/cars"


class FipeService:

    @staticmethod
    def get_models_by_brand(brand_id: int) -> list:
        cache_key = f"fipe_models_brand_{brand_id}"
        cached = cache.get(cache_key)

        if cached:
            return cached

        url = f"{FIPE_BASE_URL}/brands/{brand_id}/models"

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.RequestException:
            raise ValidationError("Erro ao consultar a tabela FIPE.")

        models = response.json()
        cache.set(cache_key, models, timeout=60 * 60)  # 1 hora

        return models

    @staticmethod
    def validate_model_exists(brand_id: int, model_name: str):
        models = FipeService.get_models_by_brand(brand_id)

        normalized_model = model_name.strip().lower()

        for model in models:
            if normalized_model == model["name"].strip().lower():
                return model

        raise ValidationError(
            f"Modelo '{model_name}' não encontrado na tabela FIPE."
        )
