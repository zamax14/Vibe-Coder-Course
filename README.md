<div align="center">

<img src="ixti_logo.png" alt="IXTI Geoespacial" width="280"/>

# Vibe Engineer Guide

### Curso IXTI · Domina GitHub Copilot y multiplica tu productividad

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Copilot](https://img.shields.io/badge/GitHub%20Copilot-Powered-000?logo=githubcopilot&logoColor=white)](https://github.com/features/copilot)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)](https://docs.docker.com/compose/)

---

*Aprende a configurar GitHub Copilot para que genere código profesional,*
*consistente y listo para producción — sin escribir una sola línea manualmente.*

</div>

---

## 🎯 ¿De qué va este curso?

Este repositorio es el material práctico del curso **Vibe Engineer Guide** de **IXTI Geoespacial**. Contiene una API REST de ejemplo con FastAPI + PostgreSQL que usaremos para demostrar cómo personalizar GitHub Copilot con **instrucciones, prompts, agentes y skills**.

> **La idea:** No se trata de que la IA escriba código por ti. Se trata de que escriba código **con tus reglas**, siguiendo **tu arquitectura**, y generando **módulos completos** con un solo comando.

---

## ⚡ Setup rápido

### Opción 1 — Docker (recomendado)

```bash
git clone <repo-url>
cd vibe-coder-guide
cp .env.example .env
docker compose up --build
```

> La API queda en **http://localhost:8000** · Docs interactivos en **http://localhost:8000/docs**

### Opción 2 — Local con Conda

```bash
git clone <repo-url>
cd vibe-coder-guide

conda create -n vibe python=3.12 -y
conda activate vibe
pip install -r requirements.txt

cp .env.example .env
docker compose up db -d          # solo PostgreSQL
uvicorn app.main:app --reload
```

### Correr los tests

```bash
pip install aiosqlite    # solo la primera vez
pytest tests/ -v
```

---

## 🧪 ¿Qué puedes probar?

Estas son las acciones que puedes ejecutar desde el **chat de Copilot** en VS Code:

### Comandos `/` (Prompts)

| Comando | Qué hace | Ejemplo |
|:--------|:---------|:--------|
| `/new-crud` | Genera un módulo CRUD completo (7 archivos) | *"Category con name:str, description:str\|None"* |
| `/generate-tests` | Crea 6 tests para un módulo existente | *"categories"* |
| `/run-tests` | Ejecuta pytest y reporta resultados | — |
| `/deploy` | Levanta todo con Docker Compose | — |

### Agentes especializados

| Agente | Para qué usarlo |
|:-------|:----------------|
| `api-developer` | Crear endpoints, módulos, editar código de la app |
| `tester` | Escribir y correr tests (no puede tocar código de la app) |

### Ejercicio sugerido

1. Abre el chat de Copilot en VS Code
2. Ejecuta `/new-crud` → *"Category con name:str, description:str\|None, is_active:bool"*
3. Revisa los 7 archivos generados en `app/categories/`
4. Ejecuta `/generate-tests` → *"categories"*
5. Ejecuta `/run-tests` y verifica que todo pase en verde ✅
6. Abre `http://localhost:8000/docs` y prueba los endpoints

> **Bonus:** Agrega una regla nueva a `.github/copilot-instructions.md` y comprueba que Copilot la sigue en la siguiente generación.

---

## 📁 Estructura del proyecto

```
.github/
├── copilot-instructions.md        → Reglas globales (siempre activas)
├── instructions/                  → Reglas por tipo de archivo
├── prompts/                       → Comandos / reutilizables
├── agents/                        → Roles especializados
└── skills/crud-generator/         → Flujo completo con plantillas

app/
├── users/        → Módulo de ejemplo (7 archivos)
├── products/     → Módulo de ejemplo
├── orders/       → Módulo de ejemplo
├── main.py       → Punto de entrada
├── database.py   → Configuración async de BD
└── config.py     → Variables de entorno

tests/            → Tests automatizados (pytest + httpx)
```

Cada módulo CRUD tiene **exactamente la misma estructura** — eso es lo que permite que Copilot los replique perfectamente:

```
app/<modulo>/
├── constants.py     Mensajes de respuesta
├── exceptions.py    Errores HTTP custom
├── models.py        Tabla en la BD (SQLAlchemy 2.0)
├── schemas.py       Validación de datos (Pydantic v2)
├── service.py       Lógica de negocio
└── routes.py        Endpoints de la API
```

---

## 🗺️ Las 5 primitivas de Copilot

| Primitiva | Archivo | Se activa | Analogía |
|:----------|:--------|:----------|:---------|
| **Instructions** | `copilot-instructions.md` | Siempre | La constitución |
| **File Instructions** | `*.instructions.md` | Por patrón de archivo | Leyes específicas |
| **Prompts** | `*.prompt.md` | Comando `/` | Recetas de cocina |
| **Agents** | `*.agent.md` | Selector de agente | Empleados expertos |
| **Skills** | `SKILL.md` + `references/` | Comando `/` | Manuales de procedimiento |

---

<div align="center">

<img src="ixti_logo.png" alt="IXTI Geoespacial" width="140"/>

**IXTI Geoespacial** · IA · Ciencia de Datos · Geoespacial

*© 2026 IXTI Geoespacial. Todos los derechos reservados.*

</div>

---

## Licencia

MIT
