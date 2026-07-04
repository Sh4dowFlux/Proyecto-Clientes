
## Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- MySQL Server 5.7 o superior
- Git

### Pasos de Instalación

1. Clonar el repositorio
2. Crear un entorno virtual
3. Instalar dependencias
4. Configurar la base de datos MySQL
5. Configurar variables de entorno
6. Ejecutar la aplicación
7. Acceder a la documentación

## Endpoints de la API

### Clientes (/api/clientes)

- GET / - Listar todos los clientes
- GET /{id} - Obtener un cliente por ID
- POST / - Crear un nuevo cliente
- PUT /{id} - Actualizar un cliente existente
- DELETE /{id} - Eliminar un cliente

### Facturas (/api/facturas)

- GET / - Listar todas las facturas
- GET /{id} - Obtener una factura por ID
- POST / - Crear una nueva factura
- PUT /{id} - Actualizar una factura
- DELETE /{id} - Eliminar una factura

### Transacciones (/api/transacciones)

- GET / - Listar todas las transacciones
- GET /{id} - Obtener una transacción por ID
- POST / - Crear una nueva transacción
- PUT /{id} - Actualizar una transacción
- DELETE /{id} - Eliminar una transacción

## Modelos de Datos

### Cliente
- id: Optional[int] primary_key=True
- nombre: str
- email: str
- telefono: str
- direccion: str
- facturas: List[Factura] Relationship

### Factura
- id: Optional[int] primary_key=True
- cliente_id: int foreign_key
- fecha: str
- descripcion: str
- total: float default=0.0
- cliente: Cliente Relationship
- transacciones: List[Transaccion] Relationship

### Transacción
- id: Optional[int] primary_key=True
- factura_id: int foreign_key
- descripcion: str
- monto: float
- factura: Factura Relationship

## Historial de Commits

### Fase 1: Inicio del Proyecto
- primer commit: proyecto iniciado
- agregar gitignore y requirements

### Fase 2: Desarrollo de Clientes
- crear modelo clientes y endpoints listar y crear
- agregar endpoints actualizar y eliminar clientes
- separar modelos y crear cliente sin ID

### Fase 3: Desarrollo de Facturas y Transacciones
- crear modelo y CRUD de facturas
- crear modelo y CRUD de transacciones
- pasar facturas y transacciones a MySQL

### Fase 4: Integración con MySQL
- proyecto funcionando con MySQL
- conectar clientes con MySQL

### Fase 5: Documentación y Mejoras
- agregar README con documentacion del proyecto
- agregar documentacion sobre navegacion entre commits
- agregar endpoint editar y manejo de errores

### Fase 6: Refactorización y Estructura
- crear estructura de endpoints para facturas y transacciones
- agregar manejo de excepciones a facturas y clientes
- validar cliente al crear factura y agregar campos calculados

### Fase 7: Conexión Completa a MySQL
- conectar facturas y transacciones a MySQL
- calcular valor total de facturas con transacciones

### Fase 8: Arquitectura Modular
- reorganizar proyecto en estructura app/
- separar endpoints de clientes en router
- separar endpoints de facturas y transacciones en routers

### Fase 9: Integración con SQLModel
- crear listas globales y corregir importaciones en routers
- conectar base de datos con SQLModel
- configurar modelos SQLModel y crear base de datos

### Fase 10: CRUD Final con SQLModel
- completar CRUD clientes con SQLModel
- crear tablas facturas y transacciones con llaves foraneas
- adaptar CRUD facturas a SQLModel
- adaptar CRUD transacciones a SQLModel

### Fase 11: Relaciones y Cálculos Finales
- agregar modelos de lectura para facturas con relaciones
- completar relaciones y valor total en facturas

## Guía de Navegación entre Commits

### Ver todos los commits
git log --oneline

### Navegar a un commit específico
git checkout <hash-del-commit>

### Volver al estado más reciente
git checkout main

### Ver diferencias entre commits
git diff <commit1> <commit2>

### Ver cambios de un commit específico
git show <hash-del-commit>

### Ver el historial de cambios de un archivo
git log -p app/main.py

### Fases importantes para revisar:
1. Inicio del proyecto: primer commit: proyecto iniciado
2. Primera versión funcional: proyecto funcionando con MySQL
3. Documentación añadida: agregar README con documentacion del proyecto
4. Refactorización a módulos: reorganizar proyecto en estructura app/
5. Integración SQLModel: conectar base de datos con SQLModel
6. Versión final: completar relaciones y valor total en facturas

## Manejo de Errores

### Excepciones manejadas:
- 404 Not Found: Cuando no se encuentra un recurso solicitado
- 400 Bad Request: Para datos inválidos o de formato incorrecto
- 422 Unprocessable Entity: Para validaciones de Pydantic
- 409 Conflict: Para duplicados o conflictos de datos
- 500 Internal Server Error: Para errores internos del servidor

### Validaciones implementadas:
1. Clientes:
   - Email único y formato válido
   - Campos obligatorios completos
   - Longitud de campos

2. Facturas:
   - Cliente debe existir en la base de datos
   - Fechas en formato válido
   - Total calculado automáticamente

3. Transacciones:
   - Factura debe existir
   - Montos positivos
   - Descripción no vacía

## Contribución

1. Fork el repositorio
2. Crea tu rama de características: git checkout -b feature/nueva-caracteristica
3. Realiza tus cambios y commits: git commit -am 'Agregar nueva característica'
4. Push a la rama: git push origin feature/nueva-caracteristica
5. Crea un Pull Request

### Buenas prácticas de commits:
- Usar el formato: [Tipo] Descripción breve
- Tipos: feat, fix, docs, style, refactor, test, chore
- Descripción clara y concisa

## Licencia

Este proyecto está bajo la Licencia MIT.

## Contacto y Soporte

Para preguntas o soporte:
- Crear un issue en el repositorio
- Contactar al equipo de desarrollo

## Estadísticas del Proyecto

- Total de commits: 34
- Líneas de código: ~800
- Endpoints: 15
- Modelos: 3 principales + 6 de lectura
- Cobertura de pruebas: En desarrollo

## Próximos Pasos

- [ ] Implementar autenticación JWT
- [ ] Agregar pruebas unitarias
- [ ] Implementar paginación en listados
- [ ] Añadir logging avanzado
- [ ] Crear dashboard de administración
- [ ] Implementar caché para consultas frecuentes
- [ ] Agregar documentación en OpenAPI completa