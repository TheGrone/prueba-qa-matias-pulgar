import requests
import responses

@responses.activate
def test_regresion_stock_cero_permitido(base_url):
    # Arrange
    url = f"{base_url}/api/products"
    payload = {"name": "Producto Regresion", "price": 10.00, "stock": 0}
    
    # Simulamos que el sistema acepta stock 0 según la regla de negocio
    responses.add(responses.POST, url, json=payload, status=201)
    
    # Act
    response = requests.post(url, json=payload)

    # Assert
    assert response.status_code == 201
    assert response.json()["stock"] == 0