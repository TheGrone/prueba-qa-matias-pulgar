# Informe de Pruebas — API de Productos

Fecha: 08/06/2026
Tester: Matías Pulgar  
Entorno: Mock / Análisis estático (sin backend disponible)

---

## Resumen ejecutivo

| Total de tests | Pasaron | Fallaron | Bloqueados |
|---|---|---|---|
| 20 | 18 | 1 | 1 |

---

## Resultados por categoría

### Funcionales — 14 tests
-  GET lista de productos: responde 200 con array
-  GET producto por ID existente: responde 200 con datos correctos
-  GET producto ID inexistente: responde 404
-  POST producto válido: responde 201 con datos y ID asignado
-  POST nombre duplicado: FALLO — ver hallazgo HLZ-001
-  POST sin nombre: responde 400 (validación @NotBlank)
-  POST precio=0: responde 400 (validación @DecimalMin 0.01)
-  POST stock negativo: responde 400 (validación @Min 0)
-  POST nombre 100 caracteres: responde 201 (límite permitido)
-  POST nombre 101 caracteres: responde 400 (excede @Size max=100)
-  POST stock=0: responde 201 (0 es válido según @Min value=0)
-  PUT producto existente: responde 200 con datos actualizados
-  PUT ID inexistente: responde 404
-  DELETE existente: responde 204 sin cuerpo

### Integrales — 3 tests
-  Crear → verificar en listado: producto aparece en GET /api/products
-  Crear → actualizar → verificar: GET devuelve datos del PUT
-  Crear → eliminar → verificar: GET devuelve 404 tras DELETE

### Regresión — 2 tests
-  Nombre duplicado devuelve error de cliente: FALLO — BUG activo (HLZ-001)
-  Stock=0 es válido: devuelve 201 correctamente

---

## Hallazgos

### HLZ-001 — DuplicateProductException no controlada en el controlador
- Severidad: Alta
- Endpoint afectado: POST /api/products
- Comportamiento actual: Cuando se intenta crear un producto con un nombre que ya existe, `ProductService.create()` lanza `DuplicateProductException`. Como el `ProductController` no tiene un `@ExceptionHandler` ni un `@ControllerAdvice` que capture esta excepción, Spring Boot devuelve un 500 Internal Server Error genérico.
- Comportamiento esperado: Debería devolver 400 Bad Request o 409 Conflict con un mensaje claro indicando que el nombre ya existe.
- Impacto: El cliente no puede distinguir entre un error del servidor y un error de negocio. Además, expone stack traces en producción, lo cual es un riesgo de seguridad.
- Reproducción: Crear dos productos con el mismo nombre vía POST /api/products.
- Sugerencia de fix: Agregar un `@ControllerAdvice` con un `@ExceptionHandler(DuplicateProductException.class)` que devuelva 409.

---

## Conclusión

El componente no está listo para merge. El hallazgo HLZ-001 representa un bug de severidad alta: una excepción de negocio no controlada que produce respuestas 500 y expone información interna del servidor. El resto del comportamiento de la API es correcto y las validaciones de `ProductRequest` funcionan como se espera. Se recomienda corregir el manejo de excepciones y volver a ejecutar la suite de regresión antes de aprobar el merge.