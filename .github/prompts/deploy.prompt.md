---
description: "Deploy the application using Docker Compose. Builds and starts the API and PostgreSQL database."
agent: "agent"
tools: [execute]
---
Deploy the application with Docker Compose:

1. Verify [docker-compose.yml](docker-compose.yml) exists and is valid
2. Run `docker compose up --build -d`
3. Wait for health checks to pass
4. Test the health endpoint: `curl http://localhost:8000/`
5. Show running containers with `docker compose ps`

Report the status of each service.
