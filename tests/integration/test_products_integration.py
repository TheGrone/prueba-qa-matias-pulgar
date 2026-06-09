import pytest
import requests
import responses

BASE_URL = "http://localhost:8080/api/products"

@responses.activate
def test_create_and_verify_product_flow():
    # Arrange: Mockeamos la creación y luego la consulta
    payload = {"name": "Teclado", "price": 45.0}
    responses.add(responses.POST, BASE_URL, json={"id": 3, "name": "Teclado", "price": 45.0}, status=201)
    responses.add(responses.GET, f"{BASE_URL}/3", json={"id": 3, "name": "Teclado", "price": 45.0}, status=200)
    
    # Act & Assert - Paso 1: Crear
    post_response = requests.post(BASE_URL, json=payload)
    assert post_response.status_code == 201
    product_id = post_response.json()["id"]
    
    # Act & Assert - Paso 2: Verificar que se creó consultándolo
    get_response = requests.get(f"{BASE_URL}/{product_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Teclado"

@responses.activate
def test_create_and_delete_flow():
    payload = {"name": "Monitor", "price": 200.0}
    responses.add(responses.POST, BASE_URL, json={"id": 4, "name": "Monitor"}, status=201)
    responses.add(responses.DELETE, f"{BASE_URL}/4", status=204)
    
    # Crear
    post_resp = requests.post(BASE_URL, json=payload)
    assert post_resp.status_code == 201
    
    # Eliminar
    del_resp = requests.delete(f"{BASE_URL}/4")
    assert del_resp.status_code == 204