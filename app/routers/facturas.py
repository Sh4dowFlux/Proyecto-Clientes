from fastapi import APIRouter, HTTPException, status
from app.modelos.facturas import Factura, FacturaCrear, FacturaEditar, FacturaLeer
from app.modelos.clientes import Cliente
from app.database import SesionDependencia
from sqlmodel import select

router = APIRouter(tags=["facturas"])

# Listar todas las facturas (con datos relacionados)
@router.get("/facturas", response_model=list[FacturaLeer])
async def listar_facturas(session: SesionDependencia):
    facturas = session.exec(select(Factura)).all()
    return facturas

# Listar una factura por ID (con datos relacionados)
@router.get("/facturas/{factura_id}", response_model=FacturaLeer)
async def listar_factura(factura_id: int, session: SesionDependencia):
    factura = session.get(Factura, factura_id)
    if factura is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Factura con ID {factura_id} no existe")
    return factura

# Crear una factura
@router.post("/facturas", response_model=FacturaLeer)
async def crear_factura(datos: FacturaCrear, session: SesionDependencia):
    # Verificar que el cliente existe
    cliente = session.get(Cliente, datos.cliente_id)
    if cliente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cliente con ID {datos.cliente_id} no existe")
    
    # Crear la factura
    factura = Factura(**datos.dict())
    session.add(factura)
    session.commit()
    session.refresh(factura)
    return factura

# Editar una factura
@router.patch("/facturas/{factura_id}", response_model=FacturaLeer)
async def editar_factura(factura_id: int, datos: FacturaEditar, session: SesionDependencia):
    factura = session.get(Factura, factura_id)
    if factura is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Factura con ID {factura_id} no existe")
    
    factura_dict = datos.dict(exclude_unset=True)
    for key, value in factura_dict.items():
        setattr(factura, key, value)
    
    session.add(factura)
    session.commit()
    session.refresh(factura)
    return factura

# Eliminar una factura
@router.delete("/facturas/{factura_id}")
async def eliminar_factura(factura_id: int, session: SesionDependencia):
    factura = session.get(Factura, factura_id)
    if factura is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Factura con ID {factura_id} no existe")
    
    session.delete(factura)
    session.commit()
    return {"mensaje": "Factura eliminada correctamente"}