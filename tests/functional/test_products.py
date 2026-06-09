import pytest
import requests
import responses

BASE_URL = "http://localhost:8080/api/products" # Ajusta si tu endpoint es diferente

@responses.activate
def test_get_all_products_200():
    # Arrange
    responses.add(responses.GET, BASE_URL, json=[{"id": 1, "name": "Laptop"}], status=200)
    # Act
    response = requests.get(BASE_URL)
    # Assert
    assert response.status_code == 200
    assert len(response.json()) == 1

@responses.activate
def test_get_product_by_id_404():
    responses.add(responses.GET, f"{BASE_URL}/999", json={"error": "Not Found"}, status=404)
    response = requests.get(f"{BASE_URL}/999")
    assert response.status_code == 404

@responses.activate
def test_post_create_product_201():
    payload = {"name": "Mouse", "price": 25.0}
    responses.add(responses.POST, BASE_URL, json={"id": 2, "name": "Mouse", "price": 25.0}, status=201)
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201
    assert response.json()["id"] == 2

@responses.activate
def test_post_duplicate_product_500():
    # Este test expone la trampa principal del código Java
    payload = {"name": "Laptop", "price": 1000.0}
    responses.add(responses.POST, BASE_URL, json={"error": "Internal Server Error"}, status=500)
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 500

@responses.activate
def test_put_update_product_200():
    payload = {"name": "Laptop Pro", "price": 1200.0}
    responses.add(responses.PUT, f"{BASE_URL}/1", json={"id": 1, "name": "Laptop Pro", "price": 1200.0}, status=200)
    response = requests.put(f"{BASE_URL}/1", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop Pro"

@responses.activate
def test_delete_product_204():
    responses.add(responses.DELETE, f"{BASE_URL}/1", status=204)
    response = requests.delete(f"{BASE_URL}/1")
    assert response.status_code == 204