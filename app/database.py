from sqlmodel import SQLModel, create_engine, Session
from typing import Annotated
from fastapi import Depends

nombre_base_datos = "clientes.db"
url_base_datos = f"sqlite:///{nombre_base_datos}"

motor_base_datos = create_engine(url_base_datos)


def crear_tablas():
    SQLModel.metadata.create_all(motor_base_datos)


def obtener_sesion():
    with Session(motor_base_datos) as mi_sesion:
        yield mi_sesion


SesionDependencia = Annotated[Session, Depends(obtener_sesion)]