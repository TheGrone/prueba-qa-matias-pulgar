# prueba-qa-matias-pulgar

Prueba técnica QA Junior Automatizador. Automatización de tests para una API REST de gestión de productos desarrollada en Java Spring Boot, usando Python con pytest y requests.

## Instalación

```bash
pip install pytest requests
```

## Variables de entorno

```bash
export API_BASE_URL=http://localhost:8080
```

En Windows:
```powershell
$env:API_BASE_URL = "http://localhost:8080"
```

## Ejecución

```bash
pytest tests/ -v
```

Para ejecutar solo un tipo:
```bash
pytest tests/functional/ -v
pytest tests/integration/ -v
pytest tests/regression/ -v
```

## Preguntas de cierre

1. **¿Qué caso de prueba te pareció más importante y por qué?**  
   El caso de nombre duplicado (POST con nombre ya existente). El código de `ProductService` lanza una `DuplicateProductException` que el controlador no captura, lo que produce un error 500 en vez de un 400 o 409. Ese tipo de bug llega a producción silenciosamente y afecta la experiencia del usuario.

2. **¿Encontraste algo en el código que te generó dudas?**  
   Sí. `DuplicateProductException` no tiene un `@ExceptionHandler` ni un `@ControllerAdvice` en el controlador. Esto significa que Spring devuelve un 500 genérico. Lo probaría con mayor profundidad si tuviera más tiempo: cubrir edge cases como nombres con solo espacios, precios con muchos decimales, y stock en exactamente 0.

3. **¿Cómo organizarías los tests si hubiera 10 endpoints?**  
   Mantendría la separación por tipo (functional/integration/regression) pero dentro de cada carpeta crearía un archivo por recurso: `test_products.py`, `test_orders.py`, `test_users.py`. También agregaría una carpeta `utils/` con helpers comunes y un `conftest.py` global con fixtures reutilizables.