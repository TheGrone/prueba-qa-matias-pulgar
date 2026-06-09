import pytest
import requests
import responses

@responses.activate
def test_get_all_products_200(base_url):
    # Arrange
    url = f"{base_url}/api/products"
    responses.add(responses.GET, url, json=[{"id": 1, "name": "Laptop"}], status=200)
    
    # Act
    response = requests.get(url)
    
    # Assert
    assert response.status_code == 200
    assert len(response.json()) == 1

@responses.activate
def test_get_product_by_id_404(base_url):
    # Arrange
    url = f"{base_url}/api/products/999"
    responses.add(responses.GET, url, json={"error": "Not Found"}, status=404)
    
    # Act
    response = requests.get(url)
    
    # Assert
    assert response.status_code == 404

@responses.activate
def test_post_create_product_201(base_url, producto_valido):
    # Arrange
    url = f"{base_url}/api/products"
    responses.add(responses.POST, url, json={"id": 2, "name": "Monitor 24 Pulgadas", "price": 150.0}, status=201)
    
    # Act
    response = requests.post(url, json=producto_valido)
    
    # Assert
    assert response.status_code == 201
    assert response.json()["id"] == 2

@responses.activate
def test_post_duplicate_product_500(base_url):
    # Arrange
    url = f"{base_url}/api/products"
    payload = {"name": "Laptop", "price": 1000.0}
    responses.add(responses.POST, url, json={"error": "Internal Server Error"}, status=500)
    
    # Act
    response = requests.post(url, json=payload)
    
    # Assert
    assert response.status_code == 500

@responses.activate
def test_put_update_product_200(base_url):
    # Arrange
    url = f"{base_url}/api/products/1"
    payload = {"name": "Laptop Pro", "price": 1200.0}
    responses.add(responses.PUT, url, json={"id": 1, "name": "Laptop Pro", "price": 1200.0}, status=200)
    
    # Act
    response = requests.put(url, json=payload)
    
    # Assert
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop Pro"

@responses.activate
def test_delete_product_204(base_url):
    # Arrange
    url = f"{base_url}/api/products/1"
    responses.add(responses.DELETE, url, status=204)
    
    # Act
    response = requests.delete(url)
    
    # Assert
    assert response.status_code == 204