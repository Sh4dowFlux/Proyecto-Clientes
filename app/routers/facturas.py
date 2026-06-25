from fastapi import APIRouter, HTTPException, status
from app.modelos.facturas import Factura, FacturaCrear, FacturaEditar
from app.modelos.transacciones import Transaccion
from app.listas import lista_clientes, lista_facturas  # ← Importar listas globales

router = APIRouter(tags=["facturas"])

# ============ ENDPOINTS DE FACTURAS ============

@router.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas

@router.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):
    for factura in lista_facturas:
        if factura["id"] == factura_id:
            return factura
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La factura con ID {factura_id} no existe")

@router.post("/facturas", response_model=Factura)
async def crear_factura(datos: FacturaCrear):
    # Validar que el cliente existe
    cliente_encontrado = None
    for cliente in lista_clientes:
        if cliente["id"] == datos.cliente_id:
            cliente_encontrado = cliente
            break

    if cliente_encontrado is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"El cliente con ID {datos.cliente_id} no existe")

    nuevo_id = len(lista_facturas) + 1
    factura_validada = Factura(**datos.dict())
    factura_validada.id = nuevo_id
    factura_validada.cliente = cliente_encontrado
    factura_validada.transacciones = []
    lista_facturas.append(factura_validada.dict())
    return factura_validada

@router.patch("/facturas/{factura_id}", response_model=Factura)
async def editar_factura(factura_id: int, datos: FacturaEditar):
    for i, factura in enumerate(lista_facturas):
        if factura["id"] == factura_id:
            factura_validada = Factura(**datos.dict())
            factura_validada.id = factura_id
            lista_facturas[i] = factura_validada.dict()
            return factura_validada
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La factura con ID {factura_id} no existe")

@router.delete("/facturas/{factura_id}")
async def eliminar_factura(factura_id: int):
    for i, factura in enumerate(lista_facturas):
        if factura["id"] == factura_id:
            lista_facturas.pop(i)
            return {"mensaje": "Factura eliminada correctamente"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La factura con ID {factura_id} no existe")