from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.database import init_db
from app.users.routes import router as users_router
from app.products.routes import router as products_router
from app.orders.routes import router as orders_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

app.include_router(users_router)
app.include_router(products_router)
app.include_router(orders_router)


@app.get("/")
async def health_check() -> dict:
    return {"status": "ok", "app": settings.APP_NAME}
