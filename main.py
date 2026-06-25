from fastapi import FastAPI, HTTPException, status
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from modelos.facturas import Factura, FacturaCrear, FacturaEditar
from modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar

# Importar funciones CRUD desde MySQL
from crud_clientes import (
    obtener_clientes,
    obtener_cliente_por_id,
    crear_cliente,
    actualizar_cliente,
    eliminar_cliente
)
from crud_facturas import (
    obtener_facturas,
    obtener_factura_por_id,
    crear_factura,
    actualizar_factura,
    eliminar_factura
)
from crud_transacciones import (
    obtener_transacciones,
    obtener_transaccion_por_id,
    crear_transaccion,
    actualizar_transaccion,
    eliminar_transaccion
)

app = FastAPI()

# ============ ENDPOINTS DE CLIENTES ============

@app.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return obtener_clientes()

@app.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):
    cliente = obtener_cliente_por_id(cliente_id)
    if cliente:
        return cliente
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"El cliente con ID {cliente_id} no existe")

@app.post("/clientes", response_model=Cliente)
async def crear_cliente_endpoint(datos: ClienteCrear):
    return crear_cliente(datos)

@app.patch("/clientes/{cliente_id}", response_model=Cliente)
async def actualizar_cliente_endpoint(cliente_id: int, datos: ClienteEditar):
    return actualizar_cliente(cliente_id, datos)

@app.delete("/clientes/{cliente_id}")
async def eliminar_cliente_endpoint(cliente_id: int):
    return eliminar_cliente(cliente_id)

# ============ ENDPOINTS DE FACTURAS ============

@app.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return obtener_facturas()

@app.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):
    factura = obtener_factura_por_id(factura_id)
    if factura:
        return factura
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La factura con ID {factura_id} no existe")

@app.post("/facturas", response_model=Factura)
async def crear_factura_endpoint(datos: FacturaCrear):
    return crear_factura(datos)

@app.patch("/facturas/{factura_id}", response_model=Factura)
async def actualizar_factura_endpoint(factura_id: int, datos: FacturaEditar):
    return actualizar_factura(factura_id, datos)

@app.delete("/facturas/{factura_id}")
async def eliminar_factura_endpoint(factura_id: int):
    return eliminar_factura(factura_id)

# ============ ENDPOINTS DE TRANSACCIONES ============

@app.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return obtener_transacciones()

@app.get("/transacciones/{transaccion_id}", response_model=Transaccion)
async def listar_transaccion(transaccion_id: int):
    transaccion = obtener_transaccion_por_id(transaccion_id)
    if transaccion:
        return transaccion
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La transaccion con ID {transaccion_id} no existe")

@app.post("/transacciones", response_model=Transaccion)
async def crear_transaccion_endpoint(datos: TransaccionCrear):
    # Validar que la factura existe
    factura_encontrada = None
    for factura in lista_facturas:
        if factura["id"] == datos.factura_id:
            factura_encontrada = factura
            break

    if factura_encontrada is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La factura con ID {datos.factura_id} no existe"
        )

    # Generar ID automático
    nuevo_id = len(lista_transacciones) + 1

    # Crear transacción validada
    transaccion_validada = Transaccion(**datos.dict())
    transaccion_validada.id = nuevo_id
    transaccion_validada.factura_id = datos.factura_id

    # Guardar en lista
    lista_transacciones.append(transaccion_validada.dict())

    # Agregar transacción a la factura
    factura_encontrada["transacciones"].append(transaccion_validada.dict())

    return transaccion_validada

@app.patch("/transacciones/{transaccion_id}", response_model=Transaccion)
async def actualizar_transaccion_endpoint(transaccion_id: int, datos: TransaccionEditar):
    return actualizar_transaccion(transaccion_id, datos)

@app.delete("/transacciones/{transaccion_id}")
async def eliminar_transaccion_endpoint(transaccion_id: int):
    return eliminar_transaccion(transaccion_id)