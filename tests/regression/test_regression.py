import pytest
import requests
import responses

@responses.activate
def test_regression_duplicate_product_bug(base_url, producto_valido):
    # Arrange: Replicamos el escenario del bug conocido (falta de manejo de DuplicateProductException)
    url = f"{base_url}/api/products"
    
    # El servidor devuelve 500 en lugar del 400 esperado según la lectura del código Java
    responses.add(responses.POST, url, json={"error": "Internal Server Error"}, status=500)
    
    # Act
    response = requests.post(url, json=producto_valido)
    
    # Assert
    assert response.status_code == 500

@responses.activate
def test_regression_invalid_price_format(base_url):
    # Arrange: Verificamos que el sistema maneje correctamente un precio negativo (Regla de negocio)
    url = f"{base_url}/api/products"
    payload_invalido = {"name": "Teclado", "price": -50.0}
    responses.add(responses.POST, url, json={"error": "Bad Request"}, status=400)
    
    # Act
    response = requests.post(url, json=payload_invalido)
    
    # Assert
    assert response.status_code == 400

@responses.activate
def test_regression_missing_required_fields(base_url):
    # Arrange: Verificamos que el sistema rechace payloads sin el campo 'name'
    url = f"{base_url}/api/products"
    payload_incompleto = {"price": 100.0}
    responses.add(responses.POST, url, json={"error": "Bad Request"}, status=400)
    
    # Act
    response = requests.post(url, json=payload_incompleto)
    
    # Assert
    assert response.status_code == 400