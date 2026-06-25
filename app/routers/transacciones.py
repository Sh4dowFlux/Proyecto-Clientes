from fastapi import APIRouter, HTTPException, status
from app.modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar

router = APIRouter()

# Lista temporal en memoria
lista_transacciones: list[Transaccion] = []

# ============ ENDPOINTS DE TRANSACCIONES ============

@router.get("/transacciones", response_model=list[Transaccion], tags=["transacciones"])
async def listar_transacciones():
    return lista_transacciones

@router.get("/transacciones/{transaccion_id}", response_model=Transaccion, tags=["transacciones"])
async def listar_transaccion(transaccion_id: int):
    for transaccion in lista_transacciones:
        if transaccion["id"] == transaccion_id:
            return transaccion
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La transaccion con ID {transaccion_id} no existe")

@router.post("/transacciones", response_model=Transaccion, tags=["transacciones"])
async def crear_transaccion(datos: TransaccionCrear):
    nuevo_id = len(lista_transacciones) + 1
    transaccion_validada = Transaccion(**datos.dict())
    transaccion_validada.id = nuevo_id
    lista_transacciones.append(transaccion_validada.dict())
    return transaccion_validada

@router.patch("/transacciones/{transaccion_id}", response_model=Transaccion, tags=["transacciones"])
async def editar_transaccion(transaccion_id: int, datos: TransaccionEditar):
    for i, transaccion in enumerate(lista_transacciones):
        if transaccion["id"] == transaccion_id:
            transaccion_validada = Transaccion(**datos.dict())
            transaccion_validada.id = transaccion_id
            lista_transacciones[i] = transaccion_validada.dict()
            return transaccion_validada
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La transaccion con ID {transaccion_id} no existe")

@router.delete("/transacciones/{transaccion_id}", tags=["transacciones"])
async def eliminar_transaccion(transaccion_id: int):
    for i, transaccion in enumerate(lista_transacciones):
        if transaccion["id"] == transaccion_id:
            lista_transacciones.pop(i)
            return {"mensaje": "Transaccion eliminada correctamente"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La transaccion con ID {transaccion_id} no existe")