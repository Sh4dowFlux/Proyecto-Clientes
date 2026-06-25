from fastapi import FastAPI, HTTPException, status
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from modelos.facturas import Factura, FacturaCrear, FacturaEditar
from modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar 

app = FastAPI()

# Lista de clientes (estática)
lista_clientes: list[Cliente] = []

# ============ ENDPOINTS DE CLIENTES ============

# Listar todos los clientes
@app.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return lista_clientes

# Listar un cliente por ID
@app.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):
    for cliente in lista_clientes:
        if cliente["id"] == cliente_id:
            return cliente
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"El cliente con ID {cliente_id} no existe")

# Crear un cliente (con ID automático)
@app.post("/clientes", response_model=Cliente)
async def crear_cliente(datos: ClienteCrear):
    nuevo_id = len(lista_clientes) + 1
    cliente_validado = Cliente(**datos.dict())
    cliente_validado.id = nuevo_id
    lista_clientes.append(cliente_validado.dict())
    return cliente_validado

# Editar un cliente (PATCH)
@app.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos: ClienteEditar):
    for i, cliente in enumerate(lista_clientes):
        if cliente["id"] == cliente_id:
            cliente_validado = Cliente(**datos.dict())
            cliente_validado.id = cliente_id
            lista_clientes[i] = cliente_validado.dict()
            return cliente_validado
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"El cliente con ID {cliente_id} no existe")

# Eliminar un cliente
@app.delete("/clientes/{cliente_id}")
async def eliminar_cliente(cliente_id: int):
    for i, cliente in enumerate(lista_clientes):
        if cliente["id"] == cliente_id:
            lista_clientes.pop(i)
            return {"mensaje": "Cliente eliminado correctamente"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"El cliente con ID {cliente_id} no existe")

# ============ LISTAS DE FACTURAS Y TRANSACCIONES ============
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []

# ============ ENDPOINTS DE FACTURAS ============

# Listar todas las facturas
@app.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas

# Listar una factura por ID
@app.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):
    for factura in lista_facturas:
        if factura["id"] == factura_id:
            return factura
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La factura con ID {factura_id} no existe")

# Crear una factura
@app.post("/facturas", response_model=Factura)
async def crear_factura(datos: FacturaCrear):
    nuevo_id = len(lista_facturas) + 1
    factura_validada = Factura(**datos.dict())
    factura_validada.id = nuevo_id
    lista_facturas.append(factura_validada.dict())
    return factura_validada

# Editar una factura
@app.patch("/facturas/{factura_id}", response_model=Factura)
async def editar_factura(factura_id: int, datos: FacturaEditar):
    for i, factura in enumerate(lista_facturas):
        if factura["id"] == factura_id:
            factura_validada = Factura(**datos.dict())
            factura_validada.id = factura_id
            lista_facturas[i] = factura_validada.dict()
            return factura_validada
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La factura con ID {factura_id} no existe")

# Eliminar una factura
@app.delete("/facturas/{factura_id}")
async def eliminar_factura(factura_id: int):
    for i, factura in enumerate(lista_facturas):
        if factura["id"] == factura_id:
            lista_facturas.pop(i)
            return {"mensaje": "Factura eliminada correctamente"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La factura con ID {factura_id} no existe")

# ============ ENDPOINTS DE TRANSACCIONES ============

# Listar todas las transacciones
@app.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transacciones

# Listar una transacción por ID
@app.get("/transacciones/{transaccion_id}", response_model=Transaccion)
async def listar_transaccion(transaccion_id: int):
    for transaccion in lista_transacciones:
        if transaccion["id"] == transaccion_id:
            return transaccion
    raise HTTPException(status_code=404, detail=f"La transaccion con ID {transaccion_id} no existe")

# Crear una transacción
@app.post("/transacciones", response_model=Transaccion)
async def crear_transaccion(datos: TransaccionCrear):
    nuevo_id = len(lista_transacciones) + 1
    transaccion_validada = Transaccion(**datos.dict())
    transaccion_validada.id = nuevo_id
    lista_transacciones.append(transaccion_validada.dict())
    return transaccion_validada

# Editar una transacción
@app.patch("/transacciones/{transaccion_id}", response_model=Transaccion)
async def editar_transaccion(transaccion_id: int, datos: TransaccionEditar):
    for i, transaccion in enumerate(lista_transacciones):
        if transaccion["id"] == transaccion_id:
            transaccion_validada = Transaccion(**datos.dict())
            transaccion_validada.id = transaccion_id
            lista_transacciones[i] = transaccion_validada.dict()
            return transaccion_validada
    raise HTTPException(status_code=404, detail=f"La transaccion con ID {transaccion_id} no existe")

# Eliminar una transacción
@app.delete("/transacciones/{transaccion_id}")
async def eliminar_transaccion(transaccion_id: int):
    for i, transaccion in enumerate(lista_transacciones):
        if transaccion["id"] == transaccion_id:
            lista_transacciones.pop(i)
            return {"mensaje": "Transaccion eliminada correctamente"}
    raise HTTPException(status_code=404, detail=f"La transaccion con ID {transaccion_id} no existe")