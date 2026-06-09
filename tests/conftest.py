import pytest
import requests
import os

@pytest.fixture
def base_url():
    """URL base de la API, leída desde variable de entorno."""
    return os.getenv("API_BASE_URL", "http://localhost:8080")

@pytest.fixture
def producto_valido():
    """Datos de un producto válido para usar en los tests."""
    return {
        "name": "Producto Test Automatizado",
        "price": 99.99,
        "stock": 10
    }

@pytest.fixture
def producto_creado(base_url, producto_valido):
    """Crea un producto antes del test y lo elimina después (teardown)."""
    # Setup: crear el producto
    response = requests.post(f"{base_url}/api/products", json=producto_valido)
    data = response.json()
    product_id = data["id"]

    yield data  # Aquí corre el test

    # Teardown: eliminar el producto al terminar
    requests.delete(f"{base_url}/api/products/{product_id}")