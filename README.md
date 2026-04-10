# Vibe Coder Guide 🚀

> Curso práctico: Cómo explotar al máximo GitHub Copilot para desarrollo de software

Este repositorio es el material de un curso diseñado para personas que se están incorporando al mundo del desarrollo de software utilizando herramientas de IA como GitHub Copilot. Aprenderás a **estandarizar tu código**, hacer que la IA **siga tus reglas**, y tener **acciones predefinidas** que aceleren tu trabajo.

## ¿Qué Vamos a Construir?

Una **API REST con FastAPI y PostgreSQL** completamente estandarizada, donde cada nuevo módulo CRUD se genera siguiendo patrones consistentes gracias a la configuración de Copilot.

### Tecnologías

| Herramienta | Uso |
|---|---|
| Python 3.11+ | Lenguaje principal |
| FastAPI | Framework web async |
| SQLAlchemy 2.0 | ORM (async) |
| PostgreSQL | Base de datos |
| Pydantic v2 | Validación de datos |
| Docker Compose | Despliegue |
| pytest | Testing |

---

## Estructura del Proyecto

```
vibe-coder-guide/
├── .github/
│   ├── copilot-instructions.md          # ⭐ Instrucciones globales
│   ├── instructions/
│   │   ├── python-api.instructions.md   # 📄 Reglas para archivos Python
│   │   └── testing.instructions.md      # 📄 Reglas para archivos de test
│   ├── prompts/
│   │   ├── new-crud.prompt.md           # 💬 Generar nuevo CRUD
│   │   ├── generate-tests.prompt.md     # 💬 Generar tests
│   │   ├── run-tests.prompt.md          # 💬 Ejecutar tests
│   │   └── deploy.prompt.md             # 💬 Desplegar con Docker
│   ├── agents/
│   │   ├── api-developer.agent.md       # 🤖 Agente desarrollador API
│   │   └── tester.agent.md              # 🤖 Agente de testing
│   └── skills/
│       └── crud-generator/
│           ├── SKILL.md                 # 🛠️ Skill: generador de CRUDs
│           └── references/
│               ├── templates.md         # Plantillas de código
│               └── test-patterns.md     # Patrones de tests
├── app/
│   ├── main.py                          # Punto de entrada
│   ├── database.py                      # Configuración de BD
│   ├── config.py                        # Variables de entorno
│   ├── users/                           # Módulo Users (ejemplo)
│   ├── products/                        # Módulo Products (ejemplo)
│   └── orders/                          # Módulo Orders (ejemplo)
├── tests/                               # Tests automatizados
├── Dockerfile
├── docker-compose.yml
└── presentacion/                        # Slides del curso (LaTeX)
```

---

## Conceptos Clave del Curso

### 1. Instrucciones Globales (`copilot-instructions.md`)

Este archivo en `.github/copilot-instructions.md` le dice a Copilot cómo debe comportarse **siempre** en tu proyecto. Es como un manual de estilo que el agente sigue automáticamente.

**¿Qué define?**
- La arquitectura del proyecto (modular, por entidad)
- Convenciones de código (async/await, tipo de ORM, estilo de Pydantic)
- Patrones de error (excepciones custom, nunca HTTPException directo)
- Comandos de build y test

**Ejemplo:** Si le pides a Copilot "crea un endpoint para categorías", automáticamente seguirá la estructura modular porque las instrucciones globales se lo indican.

📁 Ver: [`.github/copilot-instructions.md`](.github/copilot-instructions.md)

---

### 2. Instrucciones por Archivo (`.instructions.md`)

Se activan automáticamente cuando trabajas en archivos que coinciden con un patrón `applyTo`, o bajo demanda cuando el agente detecta que son relevantes.

| Archivo | Se activa con | Qué hace |
|---|---|---|
| `python-api.instructions.md` | `**/*.py` | Enforce tipo de hints, imports, async patterns |
| `testing.instructions.md` | `tests/**/*.py` | Enforce patrones de test, fixtures, naming |

📁 Ver: [`.github/instructions/`](.github/instructions/)

---

### 3. Prompts (`.prompt.md`)

Son **plantillas reutilizables** que aparecen como comandos `/` en el chat de Copilot. Piensa en ellos como recetas que puedes ejecutar con un clic.

| Prompt | Qué hace |
|---|---|
| `/new-crud` | Genera un módulo CRUD completo (7 archivos + registro en main.py) |
| `/generate-tests` | Crea tests para un módulo existente |
| `/run-tests` | Ejecuta pytest y reporta resultados |
| `/deploy` | Despliega con Docker Compose |

**Ejemplo de uso:** Escribe `/new-crud` en el chat y dile "Category con name:str y description:str|None". Copilot generará los 7 archivos siguiendo tus estándares.

📁 Ver: [`.github/prompts/`](.github/prompts/)

---

### 4. Agentes Custom (`.agent.md`)

Son **personalidades especializadas** con acceso limitado a herramientas. Cada agente tiene un rol específico y no se sale de él.

| Agente | Rol | Herramientas |
|---|---|---|
| `api-developer` | Construir endpoints y módulos | read, edit, search, execute |
| `tester` | Escribir y correr tests | read, search, execute (no edit app code) |

**¿Por qué importa?** El agente `tester` **no puede modificar código de la app**, solo archivos de test. Esto evita que arregle un test roto cambiando la app en vez del test.

📁 Ver: [`.github/agents/`](.github/agents/)

---

### 5. Skills (`SKILL.md`)

Son **flujos de trabajo complejos** con archivos de referencia. A diferencia de un prompt simple, un skill puede cargar plantillas, scripts y documentación adicional.

Nuestro skill `crud-generator`:
1. Recibe el nombre de la entidad y sus campos
2. Carga las plantillas de `references/templates.md`
3. Genera los 7 archivos del módulo
4. Registra el router en `main.py`
5. Genera tests siguiendo `references/test-patterns.md`

📁 Ver: [`.github/skills/crud-generator/`](.github/skills/crud-generator/)

---

## Flujo de Trabajo Completo

```
1. Defines tu entidad → "Necesito un CRUD de Categories"
2. Ejecutas /new-crud   → Copilot genera los 7 archivos + registro
3. Ejecutas /generate-tests → Copilot genera los tests
4. Ejecutas /run-tests  → Copilot corre pytest y reporta
5. Ejecutas /deploy     → Copilot construye y levanta con Docker
```

Todo esto **sin escribir una sola línea de código manualmente** y **siguiendo los estándares definidos** en las instrucciones.

---

## Cómo Ejecutar

### Desarrollo Local

```bash
# 1. Clonar el repo
git clone <repo-url>
cd vibe-coder-guide

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Copiar variables de entorno
cp .env.example .env

# 5. Levantar PostgreSQL (con Docker)
docker compose up db -d

# 6. Ejecutar la API
uvicorn app.main:app --reload

# 7. Ver documentación automática
# http://localhost:8000/docs
```

### Con Docker Compose (todo junto)

```bash
docker compose up --build
# API en http://localhost:8000
# Docs en http://localhost:8000/docs
```

### Tests

```bash
# Instalar dependencia extra para tests
pip install aiosqlite

# Ejecutar tests
pytest tests/ -v
```

---

## Arquitectura de un Módulo

Cada entidad sigue exactamente esta estructura:

```
app/users/
├── __init__.py      # Vacío
├── constants.py     # MESSAGES = {"not_found": "...", "created": "...", ...}
├── exceptions.py    # UserNotFoundException, UserAlreadyExistsException
├── models.py        # class User(Base) con Mapped + mapped_column
├── schemas.py       # UserCreate, UserUpdate, UserResponse
├── service.py       # get_all, get_by_id, create, update, delete
└── routes.py        # APIRouter con 5 endpoints CRUD
```

**La clave:** Todos los módulos son idénticos en estructura. Solo cambian los campos y el nombre. Por eso Copilot puede generarlos automáticamente.

---

## Para el Instructor

### Demostración Sugerida

1. **Mostrar el proyecto funcionando** — `docker compose up --build`, abrir `/docs`
2. **Mostrar las instrucciones globales** — Explicar qué hace cada sección
3. **Demo en vivo: `/new-crud`** — Crear un módulo de Categories en tiempo real
4. **Demo en vivo: agente tester** — Generar y correr tests
5. **Explicar la diferencia** entre instructions, prompts, agents y skills
6. **Ejercicio para estudiantes** — Que creen su propio módulo usando los prompts

### Puntos Clave para Enfatizar

- Las instrucciones NO son magia — son contexto que le das a la IA
- Mientras más específicas, mejores resultados
- El `description` es lo más importante — es cómo el agente descubre qué usar
- Separar responsabilidades: cada archivo de configuración hace UNA cosa

---

## Licencia

MIT
