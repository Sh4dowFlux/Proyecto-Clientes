from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from app.database import SesionDependencia
from app.modelos.facturas import (
    Factura,
    FacturaCrear,
    FacturaEditar,
    FacturaLeer,
)
from app.modelos.clientes import Cliente

router = APIRouter(tags=["facturas"])


# Listar todas las facturas
@router.get("/facturas", response_model=list[FacturaLeer])
async def listar_facturas(session: SesionDependencia):
    facturas = session.exec(select(Factura)).all()
    return facturas


# Listar una factura por ID
@router.get("/facturas/{factura_id}", response_model=FacturaLeer)
async def listar_factura(factura_id: int, session: SesionDependencia):
    factura = session.get(Factura, factura_id)

    if factura is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Factura con ID {factura_id} no existe",
        )

    return factura


# Crear una factura
@router.post("/facturas", response_model=FacturaLeer, status_code=status.HTTP_201_CREATED)
async def crear_factura(datos: FacturaCrear, session: SesionDependencia):

    cliente = session.get(Cliente, datos.cliente_id)

    if cliente is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente con ID {datos.cliente_id} no existe",
        )

    factura = Factura(**datos.model_dump())

    session.add(factura)
    session.commit()
    session.refresh(factura)

    return factura


# Editar una factura
@router.patch("/facturas/{factura_id}", response_model=FacturaLeer)
async def editar_factura(
    factura_id: int,
    datos: FacturaEditar,
    session: SesionDependencia,
):

    factura = session.get(Factura, factura_id)

    if factura is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Factura con ID {factura_id} no existe",
        )

    datos_actualizados = datos.model_dump(exclude_unset=True)

    for campo, valor in datos_actualizados.items():
        setattr(factura, campo, valor)

    session.add(factura)
    session.commit()
    session.refresh(factura)

    return factura


# Eliminar una factura
@router.delete("/facturas/{factura_id}")
async def eliminar_factura(factura_id: int, session: SesionDependencia):

    factura = session.get(Factura, factura_id)

    if factura is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Factura con ID {factura_id} no existe",
        )

    session.delete(factura)
    session.commit()

    return {"mensaje": "Factura eliminada correctamente"}