import pytest
import requests
import responses

@responses.activate
def test_regression_duplicate_product_throws_500_not_400(base_url):
    # Arrange
    url = f"{base_url}/api/products"
    payload = {"name": "ProductoExistente"}
    responses.add(responses.POST, url, status=500)
    
    # Act
    response = requests.post(url, json=payload)
    
    # Assert
    assert response.status_code == 500
    assert response.status_code != 400