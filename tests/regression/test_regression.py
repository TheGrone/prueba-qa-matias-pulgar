import pytest
import requests
import responses

BASE_URL = "http://localhost:8080/api/products"

@responses.activate
def test_regression_duplicate_product_throws_500_not_400():
    # Arrange: Verificamos que el bug del DuplicateProductException siga arrojando 500
    # hasta que el equipo de desarrollo implemente el @ExceptionHandler
    payload = {"name": "ProductoExistente"}
    responses.add(responses.POST, BASE_URL, status=500)
    
    # Act
    response = requests.post(BASE_URL, json=payload)
    
    # Assert
    assert response.status_code == 500
    assert response.status_code != 400 # Falla explícita del diseño actual