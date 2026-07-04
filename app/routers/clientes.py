from fastapi import APIRouter, HTTPException, status
from app.modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from app.database import SesionDependencia
from sqlmodel import select

router = APIRouter(tags=["clientes"])

# Listar todos los clientes
@router.get("/clientes", response_model=list[Cliente])
async def listar_clientes(session: SesionDependencia):
    clientes = session.exec(select(Cliente)).all()
    return clientes

# Listar un cliente por ID
@router.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int, session: SesionDependencia):
    cliente = session.get(Cliente, cliente_id)
    if cliente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cliente con ID {cliente_id} no existe")
    return cliente

# Crear un cliente
@router.post("/clientes", response_model=Cliente)
async def crear_cliente(datos: ClienteCrear, session: SesionDependencia):
    cliente = Cliente(**datos.dict())
    session.add(cliente)
    session.commit()
    session.refresh(cliente)
    return cliente

# Editar un cliente
@router.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos: ClienteEditar, session: SesionDependencia):
    cliente = session.get(Cliente, cliente_id)
    if cliente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cliente con ID {cliente_id} no existe")
    
    # Actualizar solo los campos que vienen en la petición
    cliente_dict = datos.dict(exclude_unset=True)
    for key, value in cliente_dict.items():
        setattr(cliente, key, value)
    
    session.add(cliente)
    session.commit()
    session.refresh(cliente)
    return cliente

# Eliminar un cliente
@router.delete("/clientes/{cliente_id}")
async def eliminar_cliente(cliente_id: int, session: SesionDependencia):
    cliente = session.get(Cliente, cliente_id)
    if cliente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cliente con ID {cliente_id} no existe")
    
    session.delete(cliente)
    session.commit()
    return {"mensaje": "Cliente eliminado correctamente"}