from fastapi import FastAPI
from app.routers.clientes import router as clientes_router
from app.routers.facturas import router as facturas_router
from app.routers.transacciones import router as transacciones_router
from app.database import crear_tablas

app = FastAPI()

# Crear tablas al iniciar
@app.on_event("startup")
async def startup():
    await crear_tablas()

# Incluir routers
app.include_router(clientes_router)
app.include_router(facturas_router)
app.include_router(transacciones_router)