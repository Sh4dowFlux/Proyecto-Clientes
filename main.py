from fastapi import FastAPI
from modelos.clientes import Cliente, ClienteCrear
from modelos.facturas import Factura, FacturaCrear
from modelos.transacciones import Transaccion, TransaccionCrear
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
def listar_clientes():
    return obtener_clientes()

@app.get("/clientes/{cliente_id}", response_model=Cliente)
def listar_cliente(cliente_id: int):
    cliente = obtener_cliente_por_id(cliente_id)
    if cliente:
        return cliente
    return {"mensaje": "Cliente no encontrado"}

@app.post("/clientes", response_model=Cliente)
def crear_cliente_endpoint(datos: ClienteCrear):
    return crear_cliente(datos)

@app.put("/clientes/{cliente_id}", response_model=Cliente)
def actualizar_cliente_endpoint(cliente_id: int, datos: ClienteCrear):
    return actualizar_cliente(cliente_id, datos)

@app.delete("/clientes/{cliente_id}")
def eliminar_cliente_endpoint(cliente_id: int):
    return eliminar_cliente(cliente_id)

# ============ ENDPOINTS DE FACTURAS ============
@app.get("/facturas", response_model=list[Factura])
def listar_facturas():
    return obtener_facturas()

@app.get("/facturas/{factura_id}", response_model=Factura)
def listar_factura(factura_id: int):
    factura = obtener_factura_por_id(factura_id)
    if factura:
        return factura
    return {"mensaje": "Factura no encontrada"}

@app.post("/facturas", response_model=Factura)
def crear_factura_endpoint(datos: FacturaCrear):
    return crear_factura(datos)

@app.put("/facturas/{factura_id}", response_model=Factura)
def actualizar_factura_endpoint(factura_id: int, datos: FacturaCrear):
    return actualizar_factura(factura_id, datos)

@app.delete("/facturas/{factura_id}")
def eliminar_factura_endpoint(factura_id: int):
    return eliminar_factura(factura_id)

# ============ ENDPOINTS DE TRANSACCIONES ============
@app.get("/transacciones", response_model=list[Transaccion])
def listar_transacciones():
    return obtener_transacciones()

@app.get("/transacciones/{transaccion_id}", response_model=Transaccion)
def listar_transaccion(transaccion_id: int):
    transaccion = obtener_transaccion_por_id(transaccion_id)
    if transaccion:
        return transaccion
    return {"mensaje": "Transaccion no encontrada"}

@app.post("/transacciones", response_model=Transaccion)
def crear_transaccion_endpoint(datos: TransaccionCrear):
    return crear_transaccion(datos)

@app.put("/transacciones/{transaccion_id}", response_model=Transaccion)
def actualizar_transaccion_endpoint(transaccion_id: int, datos: TransaccionCrear):
    return actualizar_transaccion(transaccion_id, datos)

@app.delete("/transacciones/{transaccion_id}")
def eliminar_transaccion_endpoint(transaccion_id: int):
    return eliminar_transaccion(transaccion_id)