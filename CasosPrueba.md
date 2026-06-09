# Documentación de Casos de Prueba

### CP-001 [Crear producto exitoso - Happy Path]
- **Endpoint:** POST /api/products
- **Tipo:** Funcional
- **Condición:** No existe un producto registrado con el nombre "Notebook Pro".
- **Entrada:** JSON `{ "name": "Notebook Pro", "price": 1200.00, "stock": 10 }`
- **Resultado esperado:** El sistema registra el producto y devuelve el objeto con su ID asignado.
- **Status code esperado:** 201 Created

### CP-002 [Error al crear producto con nombre duplicado - Caso Borde]
- **Endpoint:** POST /api/products
- **Tipo:** Funcional
- **Condición:** Ya existe un producto con el nombre "Mouse Inalámbrico".
- **Entrada:** JSON `{ "name": "Mouse Inalámbrico", "price": 25.50, "stock": 50 }`
- **Resultado esperado:** El sistema rechaza la petición indicando que el nombre ya existe.
- **Status code esperado:** 400 Bad Request (Hallazgo: el código actual retorna 500 por excepción no controlada).

### CP-003 [Error al crear producto con stock negativo - Caso Borde]
- **Endpoint:** POST /api/products
- **Tipo:** Funcional
- **Condición:** Ninguna.
- **Entrada:** JSON `{ "name": "Teclado", "price": 45.00, "stock": -5 }`
- **Resultado esperado:** El sistema rechaza la petición por la validación `@Min(value = 0)`.
- **Status code esperado:** 400 Bad Request

### CP-004 [Obtener producto por ID existente - Happy Path]
- **Endpoint:** GET /api/products/{id}
- **Tipo:** Funcional
- **Condición:** Existe un producto registrado con ID 1.
- **Entrada:** Parámetro de ruta `id=1`
- **Resultado esperado:** Retorna el objeto JSON con los detalles del producto correspondiente.
- **Status code esperado:** 200 OK

### CP-005 [Validación de persistencia al actualizar producto]
- **Endpoint:** PUT /api/products/{id}
- **Tipo:** Integral
- **Condición:** Existe un producto con ID 1.
- **Entrada:** JSON con el precio actualizado a `1500.00`.
- **Resultado esperado:** La base de datos actualiza el registro y la API devuelve el objeto modificado.
- **Status code esperado:** 200 OK