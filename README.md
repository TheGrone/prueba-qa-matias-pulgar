# prueba-qa-matias-pulgar
Prueba técnica QA Junior Automatizador.

## Descripción del Proyecto
Este repositorio contiene la estructura de pruebas funcionales, de integración y regresión para la API REST de gestión de productos. Dado que no se cuenta con un backend desplegado, los scripts de Python utilizan la librería `responses` para mockear las peticiones HTTP y evaluar la lógica de las pruebas bajo el patrón AAA.

## Instalación
```bash
pip install pytest requests responses
## Variables de entorno
Antes de ejecutar las pruebas, asegúrate de configurar la URL base de la API:
```bash
export API_BASE_URL=http://localhost:8080

##################################################################
1. ¿Qué caso de prueba te pareció más importante y por qué?
El caso CP-002 (Crear producto con nombre duplicado). Es el más crítico porque permitió descubrir una vulnerabilidad en el manejo de excepciones de la API. Al no estar controlada la DuplicateProductException en el controlador mediante un @ExceptionHandler, el servidor arroja un error 500 (Internal Server Error) en lugar del 400 (Bad Request) esperado. Esto afecta la estabilidad del servidor ante errores del usuario.

2. ¿Encontraste algo en el código que te generó dudas o que probarías diferente si tuvieras más tiempo?
Me generó dudas la falta de un manejo global de excepciones (por ejemplo, usando @ControllerAdvice). Además, si tuviera más tiempo, probaría inyección de datos concurrentes: enviar múltiples peticiones POST simultáneas con el mismo nombre de producto para ver si la base de datos o el servicio manejan correctamente las condiciones de carrera (Race Conditions) antes de lanzar la excepción.

3. ¿Cómo organizarías los tests si esta API tuviera 10 endpoints en vez de 5?
Aplicaría una arquitectura más modular, similar a la división por controladores que se utiliza en frameworks de desarrollo. Separaría la carpeta tests/ por dominios o entidades (ej. tests/products/, tests/users/, tests/orders/). Dentro de cada una mantendría la división por tipo de prueba (functional, integration). Además, agruparía las pruebas utilizando clases de Pytest (class TestProductCreation:, class TestProductRetrieval:) para compartir fixtures específicos y optimizar el setup/teardown de la base de datos sin sobrecargar el conftest.py global.
