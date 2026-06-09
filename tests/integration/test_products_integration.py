import pytest
import requests
import responses

@responses.activate
def test_create_and_verify_product_flow(base_url):
    # Arrange
    url_base = f"{base_url}/api/products"
    url_id = f"{base_url}/api/products/3"
    payload = {"name": "Teclado", "price": 45.0}
    
    responses.add(responses.POST, url_base, json={"id": 3, "name": "Teclado", "price": 45.0}, status=201)
    responses.add(responses.GET, url_id, json={"id": 3, "name": "Teclado", "price": 45.0}, status=200)
    
    # Act - Paso 1: Crear
    post_response = requests.post(url_base, json=payload)
    
    # Assert - Paso 1
    assert post_response.status_code == 201
    product_id = post_response.json()["id"]
    
    # Act - Paso 2: Verificar
    get_response = requests.get(url_id)
    
    # Assert - Paso 2
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Teclado"

@responses.activate
def test_create_and_delete_flow(base_url):
    # Arrange
    url_base = f"{base_url}/api/products"
    url_id = f"{base_url}/api/products/4"
    payload = {"name": "Monitor", "price": 200.0}
    
    responses.add(responses.POST, url_base, json={"id": 4, "name": "Monitor"}, status=201)
    responses.add(responses.DELETE, url_id, status=204)
    
    # Act - Crear
    post_resp = requests.post(url_base, json=payload)
    
    # Assert - Crear
    assert post_resp.status_code == 201
    
    # Act - Eliminar
    del_resp = requests.delete(url_id)
    
    # Assert - Eliminar
    assert del_resp.status_code == 204