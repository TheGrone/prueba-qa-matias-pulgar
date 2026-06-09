import os
import pytest

@pytest.fixture(scope="session")
def base_url():
    """Retorna la URL base de la API desde variables de entorno."""
    return os.environ.get("API_BASE_URL", "http://localhost:8080")

@pytest.fixture
def producto_valido():
    """Fixture con los datos base de un producto válido."""
    return {
        "name": "Monitor 24 Pulgadas",
        "price": 150.00,
        "stock": 20
    }