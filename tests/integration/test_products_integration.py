import requests
import responses

@responses.activate
def test_crear_actualizar_verificar_producto(base_url, producto_valido):
    # Arrange
    url_post = f"{base_url}/api/products"
    url_put = f"{base_url}/api/products/1"
    
    # Simulamos que la creación devuelve el producto con ID 1
    producto_creado = {"id": 1, **producto_valido}
    responses.add(responses.POST, url_post, json=producto_creado, status=201)
    
    # Simulamos que la actualización cambia el precio
    producto_actualizado = {**producto_valido, "price": 200.0}
    responses.add(responses.PUT, url_put, json={"id": 1, **producto_actualizado}, status=200)

    # Act
    res_crear = requests.post(url_post, json=producto_valido)
    res_actualizar = requests.put(url_put, json=producto_actualizado)

    # Assert
    assert res_crear.status_code == 201
    assert res_actualizar.status_code == 200
    assert res_actualizar.json()["price"] == 200.0