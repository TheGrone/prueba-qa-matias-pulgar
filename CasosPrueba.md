# Casos de Prueba — API de Productos

## Funcionales — GET /api/products

### CP-001 — Obtener lista de productos exitosamente
- **Endpoint:** GET /api/products
- **Tipo:** Funcional
- **Condición:** Existen productos registrados en la base de datos
- **Entrada:** Request sin parámetros
- **Resultado esperado:** Lista de productos con sus atributos (id, name, price, stock)
- **Status code esperado:** 200

### CP-002 — Obtener lista cuando no hay productos
- **Endpoint:** GET /api/products
- **Tipo:** Funcional
- **Condición:** La base de datos está vacía
- **Entrada:** Request sin parámetros
- **Resultado esperado:** Lista vacía `[]`
- **Status code esperado:** 200

### CP-003 — Obtener producto por ID existente
- **Endpoint:** GET /api/products/{id}
- **Tipo:** Funcional
- **Condición:** Existe un producto con el ID indicado
- **Entrada:** ID válido (ej: 1)
- **Resultado esperado:** Objeto producto con id, name, price y stock correctos
- **Status code esperado:** 200

### CP-004 — Obtener producto por ID inexistente
- **Endpoint:** GET /api/products/{id}
- **Tipo:** Funcional
- **Condición:** No existe producto con ese ID
- **Entrada:** ID que no existe (ej: 9999)
- **Resultado esperado:** Respuesta vacía o mensaje de error
- **Status code esperado:** 404

### CP-005 — Obtener producto con ID en formato inválido
- **Endpoint:** GET /api/products/{id}
- **Tipo:** Funcional
- **Condición:** Se envía un ID no numérico
- **Entrada:** ID = "abc"
- **Resultado esperado:** Error de tipo de dato
- **Status code esperado:** 400

---

## Funcionales — POST /api/products

### CP-006 — Crear producto exitosamente
- **Endpoint:** POST /api/products
- **Tipo:** Funcional
- **Condición:** El nombre no existe previamente
- **Entrada:** `{ "name": "Laptop", "price": 999.99, "stock": 10 }`
- **Resultado esperado:** Producto creado con los mismos datos y un ID asignado
- **Status code esperado:** 201

### CP-007 — Crear producto con nombre duplicado
- **Endpoint:** POST /api/products
- **Tipo:** Funcional
- **Condición:** Ya existe un producto con el mismo nombre
- **Entrada:** `{ "name": "Laptop", "price": 500.00, "stock": 5 }`
- **Resultado esperado:** Error indicando nombre duplicado
- **Status code esperado:** 400 o 409 (actualmente devuelve 500 — BUG detectado: DuplicateProductException no está manejada en el controlador)

### CP-008 — Crear producto sin nombre
- **Endpoint:** POST /api/products
- **Tipo:** Funcional
- **Condición:** Request sin campo name
- **Entrada:** `{ "price": 100.00, "stock": 5 }`
- **Resultado esperado:** Error de validación
- **Status code esperado:** 400

### CP-009 — Crear producto con precio 0
- **Endpoint:** POST /api/products
- **Tipo:** Funcional
- **Condición:** Se envía precio igual a 0
- **Entrada:** `{ "name": "Mouse", "price": 0, "stock": 5 }`
- **Resultado esperado:** Error de validación (precio mínimo es 0.01)
- **Status code esperado:** 400

### CP-010 — Crear producto con stock negativo
- **Endpoint:** POST /api/products
- **Tipo:** Funcional
- **Condición:** Se envía stock menor a 0
- **Entrada:** `{ "name": "Teclado", "price": 50.00, "stock": -1 }`
- **Resultado esperado:** Error de validación
- **Status code esperado:** 400

### CP-011 — Crear producto con nombre de exactamente 100 caracteres
- **Endpoint:** POST /api/products
- **Tipo:** Funcional
- **Condición:** Nombre en el límite máximo permitido
- **Entrada:** `{ "name": "A"*100, "price": 10.00, "stock": 1 }`
- **Resultado esperado:** Producto creado exitosamente
- **Status code esperado:** 201

### CP-012 — Crear producto con nombre de 101 caracteres
- **Endpoint:** POST /api/products
- **Tipo:** Funcional
- **Condición:** Nombre supera el límite máximo
- **Entrada:** `{ "name": "A"*101, "price": 10.00, "stock": 1 }`
- **Resultado esperado:** Error de validación
- **Status code esperado:** 400

---

## Funcionales — PUT /api/products/{id}

### CP-013 — Actualizar producto exitosamente
- **Endpoint:** PUT /api/products/{id}
- **Tipo:** Funcional
- **Condición:** El producto existe
- **Entrada:** ID válido + `{ "name": "Monitor Nuevo", "price": 300.00, "stock": 5 }`
- **Resultado esperado:** Producto actualizado con los nuevos datos
- **Status code esperado:** 200

### CP-014 — Actualizar producto con ID inexistente
- **Endpoint:** PUT /api/products/{id}
- **Tipo:** Funcional
- **Condición:** No existe producto con ese ID
- **Entrada:** ID=9999 + datos válidos
- **Resultado esperado:** Respuesta de no encontrado
- **Status code esperado:** 404

### CP-015 — Actualizar producto con datos inválidos
- **Endpoint:** PUT /api/products/{id}
- **Tipo:** Funcional
- **Condición:** Producto existe, se envían datos con validación fallida
- **Entrada:** ID válido + `{ "price": -5, "stock": -1 }`
- **Resultado esperado:** Error de validación
- **Status code esperado:** 400

---

## Funcionales — DELETE /api/products/{id}

### CP-016 — Eliminar producto exitosamente
- **Endpoint:** DELETE /api/products/{id}
- **Tipo:** Funcional
- **Condición:** Producto existe
- **Entrada:** ID válido
- **Resultado esperado:** Sin cuerpo de respuesta
- **Status code esperado:** 204

### CP-017 — Eliminar producto inexistente
- **Endpoint:** DELETE /api/products/{id}
- **Tipo:** Funcional
- **Condición:** No existe producto con ese ID
- **Entrada:** ID=9999
- **Resultado esperado:** Error de no encontrado
- **Status code esperado:** 404

---

## Integrales

### CP-018 — Crear producto y verificar que aparece en el listado
- **Endpoint:** POST /api/products → GET /api/products
- **Tipo:** Integral
- **Condición:** La base de datos puede recibir registros
- **Entrada:** Crear producto válido, luego pedir el listado
- **Resultado esperado:** El producto creado aparece en la lista
- **Status code esperado:** 201 luego 200

### CP-019 — Crear, actualizar y verificar cambios
- **Endpoint:** POST → PUT → GET /api/products/{id}
- **Tipo:** Integral
- **Condición:** API funciona correctamente
- **Entrada:** Crear producto, actualizarlo, luego obtenerlo por ID
- **Resultado esperado:** El GET devuelve los datos actualizados
- **Status code esperado:** 201, 200, 200

### CP-020 — Crear y eliminar producto, verificar que no existe
- **Endpoint:** POST → DELETE → GET /api/products/{id}
- **Tipo:** Integral
- **Condición:** API funciona correctamente
- **Entrada:** Crear producto, eliminarlo, intentar obtenerlo por ID
- **Resultado esperado:** El GET devuelve 404 tras el DELETE
- **Status code esperado:** 201, 204, 404

---

## Regresión

### CP-021 — DuplicateProductException genera 500 en vez de 400/409
- **Endpoint:** POST /api/products
- **Tipo:** Regresión
- **Condición:** Ya existe un producto con el mismo nombre
- **Entrada:** Nombre duplicado
- **Resultado esperado:** 400 o 409 con mensaje de error claro (BUG ACTUAL: devuelve 500)
- **Status code esperado:** 400 o 409

### CP-022 — El stock con valor 0 es válido
- **Endpoint:** POST /api/products
- **Tipo:** Regresión
- **Condición:** Se envía stock=0
- **Entrada:** `{ "name": "ProductoSinStock", "price": 10.00, "stock": 0 }`
- **Resultado esperado:** Producto creado exitosamente (0 es permitido, el mínimo es 0)
- **Status code esperado:** 201