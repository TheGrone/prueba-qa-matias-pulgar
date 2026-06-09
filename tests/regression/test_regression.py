import requests
import pytest

def test_regresion_nombre_duplicado_devuelve_error_cliente(base_url, producto_creado):
    """
    Regresión: DuplicateProductException no está manejada en el controlador.
    Spring devuelve 500 en vez de 400 o 409.
    Este test documenta el bug y fallará cuando se corrija correctamente.
    """
    # Arrange
    payload = {
        "name": producto_creado["name"],
        "price": 50.00,
        "stock": 1
    }

    # Act
    response = requests.post(f"{base_url}/api/products", json=payload)

    # Assert: documentamos el bug — debería ser 400/409, actualmente es 500
    assert response.status_code in [400, 409], (
        f"BUG ACTIVO: nombre duplicado devuelve {response.status_code} en vez de 400/409. "
        "El controlador no maneja DuplicateProductException."
    )


def test_regresion_stock_cero_permitido(base_url):
    """
    Regresión: stock=0 debe ser válido según la anotación @Min(value = 0).
    Verifica que no se rechace por error de validación.
    """
    # Arrange
    payload = {"name": "Producto Regresion Stock Cero", "price": 10.00, "stock": 0}

    # Act
    response = requests.post(f"{base_url}/api/products", json=payload)

    # Assert
    assert response.status_code == 201
    data = response.json()
    assert data["stock"] == 0

    # Teardown
    requests.delete(f"{base_url}/api/products/{data['id']}")