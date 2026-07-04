from fastapi import APIRouter, HTTPException, status
from app.modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from app.modelos.facturas import Factura
from app.database import SesionDependencia
from sqlmodel import select

router = APIRouter(tags=["transacciones"])

# Listar todas las transacciones
@router.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones(session: SesionDependencia):
    transacciones = session.exec(select(Transaccion)).all()
    return transacciones

# Listar una transacción por ID
@router.get("/transacciones/{transaccion_id}", response_model=Transaccion)
async def listar_transaccion(transaccion_id: int, session: SesionDependencia):
    transaccion = session.get(Transaccion, transaccion_id)
    if transaccion is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Transaccion con ID {transaccion_id} no existe")
    return transaccion

# Crear una transacción
@router.post("/transacciones", response_model=Transaccion)
async def crear_transaccion(datos: TransaccionCrear, session: SesionDependencia):
    # Verificar que la factura existe
    factura = session.get(Factura, datos.factura_id)
    if factura is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Factura con ID {datos.factura_id} no existe")
    
    # Crear la transacción
    transaccion = Transaccion(**datos.dict())
    session.add(transaccion)
    session.commit()
    session.refresh(transaccion)
    return transaccion

# Editar una transacción
@router.patch("/transacciones/{transaccion_id}", response_model=Transaccion)
async def editar_transaccion(transaccion_id: int, datos: TransaccionEditar, session: SesionDependencia):
    transaccion = session.get(Transaccion, transaccion_id)
    if transaccion is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Transaccion con ID {transaccion_id} no existe")
    
    # Actualizar solo los campos que vienen en la petición
    transaccion_dict = datos.dict(exclude_unset=True)
    for key, value in transaccion_dict.items():
        setattr(transaccion, key, value)
    
    session.add(transaccion)
    session.commit()
    session.refresh(transaccion)
    return transaccion

# Eliminar una transacción
@router.delete("/transacciones/{transaccion_id}")
async def eliminar_transaccion(transaccion_id: int, session: SesionDependencia):
    transaccion = session.get(Transaccion, transaccion_id)
    if transaccion is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Transaccion con ID {transaccion_id} no existe")
    
    session.delete(transaccion)
    session.commit()
    return {"mensaje": "Transaccion eliminada correctamente"}