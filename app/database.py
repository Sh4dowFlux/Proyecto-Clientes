from sqlmodel import SQLModel, create_engine, Session
from typing import Annotated
from fastapi import Depends

# Nombre del archivo SQLite
nombre_base_datos = "clientes.db"

# URL de conexión
url_base_datos = f"sqlite:///{nombre_base_datos}"

# Crear motor
motor_base_datos = create_engine(url_base_datos)

# Función para crear tablas
async def crear_tablas():
    SQLModel.metadata.create_all(motor_base_datos)

# Función para obtener sesión
def obtener_sesion():
    with Session(motor_base_datos) as mi_sesion:
        yield mi_sesion

# Dependencia para usar en endpoints
SesionDependencia = Annotated[Session, Depends(obtener_sesion)]