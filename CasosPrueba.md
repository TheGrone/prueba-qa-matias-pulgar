# Documentación de Casos de Prueba

## POST /api/products
### CP-001 [Crear producto exitoso - Happy Path]
- **Tipo:** Funcional
- **Condición:** No existe un producto con el nombre "Notebook Pro".
- **Entrada:** JSON `{ "name": "Notebook Pro", "price": 1200.00, "stock": 10 }`
- **Resultado esperado:** El sistema registra el producto.
- **Status code esperado:** 201 Created

### CP-002 [Error al crear con nombre duplicado - Caso Borde]
- **Tipo:** Funcional
- **Condición:** Ya existe "Mouse Inalámbrico".
- **Entrada:** JSON `{ "name": "Mouse Inalámbrico", "price": 25.50, "stock": 50 }`
- **Resultado esperado:** Falla validación de negocio.
- **Status code esperado:** 400 Bad Request (Hallazgo: el código actual retorna 500).

### CP-003 [Error al crear con stock negativo - Caso Borde]
- **Tipo:** Funcional
- **Condición:** Ninguna.
- **Entrada:** JSON `{ "name": "Teclado", "price": 45.00, "stock": -5 }`
- **Resultado esperado:** Falla validación `@Min(value = 0)`.
- **Status code esperado:** 400 Bad Request

## GET /api/products
### CP-004 [Obtener todos los productos con datos - Happy Path]
- **Tipo:** Funcional
- **Condición:** Existen productos en la base de datos.
- **Entrada:** Ninguna
- **Resultado esperado:** Retorna un array JSON con los productos.
- **Status code esperado:** 200 OK

### CP-005 [Obtener productos cuando no hay registros - Happy Path]
- **Tipo:** Funcional
- **Condición:** La base de datos está vacía.
- **Entrada:** Ninguna
- **Resultado esperado:** Retorna un array JSON vacío `[]`.
- **Status code esperado:** 200 OK

### CP-006 [Obtener productos con método incorrecto - Caso Borde]
- **Tipo:** Funcional
- **Condición:** Ninguna.
- **Entrada:** Petición POST a la ruta sin body.
- **Resultado esperado:** Rechaza por método no soportado.
- **Status code esperado:** 405 Method Not Allowed

## GET /api/products/{id}
### CP-007 [Obtener producto por ID existente - Happy Path]
- **Tipo:** Funcional
- **Condición:** Existe producto con ID 1.
- **Entrada:** Parámetro `id=1`
- **Resultado esperado:** Retorna el JSON del producto.
- **Status code esperado:** 200 OK

### CP-008 [Obtener producto inexistente - Caso Borde]
- **Tipo:** Funcional
- **Condición:** No existe el ID 999.
- **Entrada:** Parámetro `id=999`
- **Resultado esperado:** Recurso no encontrado.
- **Status code esperado:** 404 Not Found

### CP-009 [Obtener producto con ID inválido - Caso Borde]
- **Tipo:** Funcional
- **Condición:** Ninguna.
- **Entrada:** Parámetro `id=abc` (texto en vez de número).
- **Resultado esperado:** Error de tipo de dato.
- **Status code esperado:** 400 Bad Request

## PUT /api/products/{id}
### CP-010 [Actualizar producto exitoso - Happy Path]
- **Tipo:** Funcional
- **Condición:** Existe producto con ID 1.
- **Entrada:** Parámetro `id=1`, JSON válido.
- **Resultado esperado:** Actualiza y devuelve el objeto modificado.
- **Status code esperado:** 200 OK

### CP-011 [Actualizar producto inexistente - Caso Borde]
- **Tipo:** Funcional
- **Condición:** No existe producto con ID 999.
- **Entrada:** Parámetro `id=999`, JSON válido.
- **Resultado esperado:** No encuentra el recurso a actualizar.
- **Status code esperado:** 404 Not Found

### CP-012 [Actualizar con datos inválidos - Caso Borde]
- **Tipo:** Funcional
- **Condición:** Existe producto con ID 1.
- **Entrada:** JSON `{ "name": "Monitor", "price": -10.00, "stock": 5 }`
- **Resultado esperado:** Falla validación `@DecimalMin`.
- **Status code esperado:** 400 Bad Request

## DELETE /api/products/{id}
### CP-013 [Eliminar producto exitoso - Happy Path]
- **Tipo:** Funcional
- **Condición:** Existe producto con ID 1.
- **Entrada:** Parámetro `id=1`
- **Resultado esperado:** Elimina y no retorna contenido.
- **Status code esperado:** 204 No Content

### CP-014 [Eliminar producto inexistente - Caso Borde]
- **Tipo:** Funcional
- **Condición:** No existe producto con ID 999.
- **Entrada:** Parámetro `id=999`
- **Resultado esperado:** No encuentra el recurso.
- **Status code esperado:** 404 Not Found

### CP-015 [Eliminar producto con ID inválido - Caso Borde]
- **Tipo:** Funcional
- **Condición:** Ninguna.
- **Entrada:** Parámetro `id=abc`
- **Resultado esperado:** Error por formato de parámetro.
- **Status code esperado:** 400 Bad Request

## Integrales y Regresión
### CP-016 [Flujo completo de creación y consulta]
- **Tipo:** Integral
- **Condición:** Sistema operativo.
- **Entrada:** POST válido, seguido de un GET al ID creado.
- **Resultado esperado:** El GET recupera exactamente lo creado por el POST.
- **Status code esperado:** 201 Created y 200 OK

### CP-017 [Validación de persistencia al actualizar]
- **Tipo:** Integral
- **Condición:** Existe producto ID 1.
- **Entrada:** PUT modificando el precio.
- **Resultado esperado:** La base de datos guarda el cambio.
- **Status code esperado:** 200 OK

### CP-018 [Regresión de Stock Cero]
- **Tipo:** Regresión
- **Condición:** Ninguna.
- **Entrada:** JSON con `"stock": 0` en el POST.
- **Resultado esperado:** Valida que la regla `@Min(value = 0)` se mantenga intacta permitiendo el 0.
- **Status code esperado:** 201 Created

### CP-019 [Regresión de límite de caracteres]
- **Tipo:** Regresión
- **Condición:** Ninguna.
- **Entrada:** JSON con nombre de 101 caracteres.
- **Resultado esperado:** La regla `@Size(max = 100)` sigue bloqueando nombres largos.
- **Status code esperado:** 400 Bad Request