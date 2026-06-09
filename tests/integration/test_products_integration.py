import pytest
import requests
import responses

@responses.activate
def test_product_lifecycle_integration(base_url, producto_valido):
    # Arrange: Preparamos las URLs y los mocks para todo el ciclo de vida del producto
    url_base = f"{base_url}/api/products"
    url_id = f"{base_url}/api/products/2"
    
    # Mock para Crear (POST)
    responses.add(responses.POST, url_base, json={"id": 2, "name": "Monitor 24 Pulgadas", "price": 150.0}, status=201)
    # Mock para Consultar (GET)
    responses.add(responses.GET, url_id, json={"id": 2, "name": "Monitor 24 Pulgadas", "price": 150.0}, status=200)
    # Mock para Actualizar (PUT)
    payload_update = {"name": "Monitor 24 Pulgadas Pro", "price": 180.0}
    responses.add(responses.PUT, url_id, json={"id": 2, "name": "Monitor 24 Pulgadas Pro", "price": 180.0}, status=200)
    # Mock para Eliminar (DELETE)
    responses.add(responses.DELETE, url_id, status=204)
    # Mock para Consultar producto eliminado (GET)
    responses.add(responses.GET, url_id, json={"error": "Not Found"}, status=404)

    # Act & Assert: Ejecutamos y validamos paso a paso el ciclo de vida
    
    # 1. Crear
    response_post = requests.post(url_base, json=producto_valido)
    assert response_post.status_code == 201
    
    # 2. Leer
    response_get = requests.get(url_id)
    assert response_get.status_code == 200
    assert response_get.json()["id"] == 2
    
    # 3. Actualizar
    response_put = requests.put(url_id, json=payload_update)
    assert response_put.status_code == 200
    assert response_put.json()["price"] == 180.0
    
    # 4. Eliminar
    response_delete = requests.delete(url_id)
    assert response_delete.status_code == 204
    
    # 5. Verificar que ya no existe
    response_verify = requests.get(url_id)
    assert response_verify.status_code == 404