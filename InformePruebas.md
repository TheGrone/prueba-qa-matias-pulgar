# Informe de Pruebas y Hallazgos

## 1. Resumen de Ejecución
- **Total de tests automatizados:** 2 (Mockeados para la evaluación)
- **Tests exitosos (Passed):** 1
- **Tests fallidos (Failed / Comportamiento anómalo):** 1

## 2. Detalle de Fallos Críticos
- **Test:** `test_crear_producto_nombre_duplicado`
- **Resultado Esperado:** Ante la duplicidad de un nombre, la API debería retornar un código `400 Bad Request` indicando la falla de validación de negocio al cliente.
- **Resultado Real:** La API retorna un código `500 Internal Server Error`.
- **Análisis de Causa Raíz:** Al auditar el código fuente provisto, se constata que en `ProductService.java` se arroja una `DuplicateProductException`. Sin embargo, esta excepción no está siendo capturada ni manejada en `ProductController.java` mediante un `@ExceptionHandler`.

## 3. Conclusión y Recomendación
**El componente NO está listo para hacer merge a la rama principal.** El error 500 expone vulnerabilidades en la estabilidad del servidor ante errores operativos comunes. Se recomienda bloquear el pase a producción hasta que el equipo de desarrollo implemente un controlador global de excepciones (GlobalExceptionHandler) que formatee correctamente el error.