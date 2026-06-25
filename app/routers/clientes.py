from fastapi import APIRouter, HTTPException, status
from app.modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from app.database import SesionDependencia
from sqlmodel import select

router = APIRouter(tags=["clientes"])

@router.get("/clientes", response_model=list[Cliente])
async def listar_clientes(session: SesionDependencia):
    clientes = session.exec(select(Cliente)).all()
    return clientes

@router.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int, session: SesionDependencia):
    cliente = session.get(Cliente, cliente_id)
    if cliente is None:
        raise HTTPException(status_code=404, detail=f"Cliente {cliente_id} no existe")
    return cliente

@router.post("/clientes", response_model=Cliente)
async def crear_cliente(datos: ClienteCrear, session: SesionDependencia):
    cliente = Cliente(**datos.dict())
    session.add(cliente)
    session.commit()
    session.refresh(cliente)
    return cliente

@router.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos: ClienteEditar, session: SesionDependencia):
    cliente = session.get(Cliente, cliente_id)
    if cliente is None:
        raise HTTPException(status_code=404, detail=f"Cliente {cliente_id} no existe")
    for key, value in datos.dict().items():
        setattr(cliente, key, value)
    session.commit()
    session.refresh(cliente)
    return cliente

@router.delete("/clientes/{cliente_id}")
async def eliminar_cliente(cliente_id: int, session: SesionDependencia):
    cliente = session.get(Cliente, cliente_id)
    if cliente is None:
        raise HTTPException(status_code=404, detail=f"Cliente {cliente_id} no existe")
    session.delete(cliente)
    session.commit()
    return {"mensaje": "Cliente eliminado correctamente"}