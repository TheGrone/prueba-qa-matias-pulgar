import requests
import pytest

def test_crear_producto_aparece_en_listado(base_url, producto_valido):
    # Arrange
    payload = {**producto_valido, "name": "Producto Integral Lista"}

    # Act: crear producto
    create_response = requests.post(f"{base_url}/api/products", json=payload)
    assert create_response.status_code == 201
    product_id = create_response.json()["id"]

    # Act: obtener lista
    list_response = requests.get(f"{base_url}/api/products")

    # Assert
    assert list_response.status_code == 200
    ids_en_lista = [p["id"] for p in list_response.json()]
    assert product_id in ids_en_lista

    # Teardown
    requests.delete(f"{base_url}/api/products/{product_id}")


def test_crear_actualizar_verificar_producto(base_url, producto_valido):
    # Arrange
    payload = {**producto_valido, "name": "Producto Integral Update"}

    # Act: crear
    create_response = requests.post(f"{base_url}/api/products", json=payload)
    assert create_response.status_code == 201
    product_id = create_response.json()["id"]

    # Act: actualizar
    update_payload = {"name": "Producto Actualizado Integral", "price": 500.00, "stock": 99}
    update_response = requests.put(f"{base_url}/api/products/{product_id}", json=update_payload)
    assert update_response.status_code == 200

    # Act: verificar con GET
    get_response = requests.get(f"{base_url}/api/products/{product_id}")

    # Assert
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["name"] == update_payload["name"]
    assert float(data["price"]) == update_payload["price"]
    assert data["stock"] == update_payload["stock"]

    # Teardown
    requests.delete(f"{base_url}/api/products/{product_id}")


def test_crear_eliminar_verificar_404(base_url, producto_valido):
    # Arrange
    payload = {**producto_valido, "name": "Producto Integral Delete"}

    # Act: crear
    create_response = requests.post(f"{base_url}/api/products", json=payload)
    assert create_response.status_code == 201
    product_id = create_response.json()["id"]

    # Act: eliminar
    delete_response = requests.delete(f"{base_url}/api/products/{product_id}")
    assert delete_response.status_code == 204

    # Act: intentar obtener
    get_response = requests.get(f"{base_url}/api/products/{product_id}")

    # Assert
    assert get_response.status_code == 404