### CP-006 [Obtener producto inexistente - Caso Borde]
- **Endpoint:** GET /api/products/{id}
- **Tipo:** Funcional
- **Condición:** No existe ningún producto con el ID 999.
- **Entrada:** Parámetro de ruta `id=999`
- **Resultado esperado:** El sistema indica que el recurso no fue encontrado.
- **Status code esperado:** 404 Not Found

### CP-007 [Actualizar producto con datos inválidos - Caso Borde]
- **Endpoint:** PUT /api/products/{id}
- **Tipo:** Funcional
- **Condición:** Existe un producto con ID 1.
- **Entrada:** JSON `{ "name": "Monitor", "price": -10.00, "stock": 5 }` (Precio negativo)
- **Resultado esperado:** Falla la validación `@DecimalMin` y se rechaza la petición.
- **Status code esperado:** 400 Bad Request

### CP-008 [Eliminar producto exitoso - Happy Path]
- **Endpoint:** DELETE /api/products/{id}
- **Tipo:** Funcional
- **Condición:** Existe un producto con ID 1.
- **Entrada:** Parámetro de ruta `id=1`
- **Resultado esperado:** El producto es eliminado de la base de datos y no retorna contenido.
- **Status code esperado:** 204 No Content

### CP-009 [Eliminar producto inexistente - Caso Borde]
- **Endpoint:** DELETE /api/products/{id}
- **Tipo:** Funcional
- **Condición:** No existe el producto con ID 999.
- **Entrada:** Parámetro de ruta `id=999`
- **Resultado esperado:** El sistema informa que no se encontró el recurso a eliminar.
- **Status code esperado:** 404 Not Found

### CP-010 [Flujo completo de creación y consulta]
- **Endpoint:** POST /api/products y GET /api/products/{id}
- **Tipo:** Integral
- **Condición:** El sistema está operativo.
- **Entrada:** JSON válido en el POST, seguido de un GET al ID retornado.
- **Resultado esperado:** El producto creado con el POST se recupera exitosamente e idéntico con el GET.
- **Status code esperado:** 201 Created y 200 OK

### CP-011 [Regresión de Stock Cero]
- **Endpoint:** POST /api/products
- **Tipo:** Regresión
- **Condición:** Ninguna.
- **Entrada:** JSON `{ "name": "Mousepad", "price": 10.00, "stock": 0 }`
- **Resultado esperado:** La validación `@Min(value = 0)` permite el valor 0, validando que la regla de negocio original se mantiene intacta tras nuevos despliegues.
- **Status code esperado:** 201 Created

### CP-012 [Regresión de límite de caracteres en nombre]
- **Endpoint:** POST /api/products
- **Tipo:** Regresión
- **Condición:** Ninguna.
- **Entrada:** JSON con un "name" de 101 caracteres.
- **Resultado esperado:** La validación `@Size(max = 100)` actúa correctamente rechazando el payload.
- **Status code esperado:** 400 Bad Request