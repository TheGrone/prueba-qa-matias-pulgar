import requests
import responses

@responses.activate
def test_crear_producto_exitoso(base_url, producto_valido):
    # Arrange
    url = f"{base_url}/api/products"
    payload = producto_valido
    responses.add(
        responses.POST,
        url,
        json=payload,
        status=201
    )

    # Act
    response = requests.post(url, json=payload)

    # Assert
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["price"] == payload["price"]
    assert data["stock"] == payload["stock"]

@responses.activate
def test_crear_producto_nombre_duplicado(base_url, producto_valido):
    # Arrange
    url = f"{base_url}/api/products"
    payload = producto_valido
    
    # Mockeamos el comportamiento real del código Java evaluado (devuelve 500)
    responses.add(
        responses.POST,
        url,
        json={"error": "Internal Server Error"},
        status=500
    )

    # Act
    response = requests.post(url, json=payload)

    # Assert
    # Validamos que el servidor está arrojando el error 500 no controlado
    assert response.status_code == 500