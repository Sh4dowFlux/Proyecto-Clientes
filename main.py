from fastapi import FastAPI
from modelos.clientes import Cliente, ClienteCrear

app = FastAPI()

# Lista de clientes (estática)
lista_clientes: list[Cliente] = [
    {"id": 1, "nombre": "Ana", "email": "ana@gmail.com", "descripcion": "Cliente frecuente"},
    {"id": 2, "nombre": "Luis", "email": "luis@gmail.com", "descripcion": "Cliente nuevo"},
    {"id": 3, "nombre": "Maria", "email": "maria@gmail.com", "descripcion": "Cliente VIP"}
]

# Endpoint para listar TODOS los clientes
@app.get("/clientes", response_model=list[Cliente])
def listar_clientes():
    return lista_clientes

# Endpoint para listar UN cliente por ID
@app.get("/clientes/{cliente_id}", response_model=Cliente)
def listar_cliente(cliente_id: int):
    for cliente in lista_clientes:
        if cliente["id"] == cliente_id:
            return cliente
    return {"mensaje": "Cliente no encontrado"}

# Endpoint para CREAR un cliente
@app.post("/clientes", response_model=Cliente)
def crear_cliente(datos: ClienteCrear):
    cliente_validado = Cliente(**datos.dict())
    lista_clientes.append(cliente_validado.dict())
    return cliente_validado

# Endpoint para ACTUALIZAR un cliente
@app.put("/clientes/{cliente_id}", response_model=Cliente)
def actualizar_cliente(cliente_id: int, datos: ClienteCrear):
    for i, cliente in enumerate(lista_clientes):
        if cliente["id"] == cliente_id:
            cliente_actualizado = Cliente(**datos.dict(), id=cliente_id)
            lista_clientes[i] = cliente_actualizado.dict()
            return cliente_actualizado
    return {"mensaje": "Cliente no encontrado"}

# Endpoint para ELIMINAR un cliente
@app.delete("/clientes/{cliente_id}")
def eliminar_cliente(cliente_id: int):
    for i, cliente in enumerate(lista_clientes):
        if cliente["id"] == cliente_id:
            lista_clientes.pop(i)
            return {"mensaje": "Cliente eliminado"}
    return {"mensaje": "Cliente no encontrado"}

from modelos.facturas import Factura, FacturaCrear

# Lista de facturas (estática)
lista_facturas: list[Factura] = [
    {"id": 1, "cliente_id": 1, "fecha": "2026-06-25", "total": 150.50},
    {"id": 2, "cliente_id": 2, "fecha": "2026-06-26", "total": 200.00}
]

# Endpoint para listar TODAS las facturas
@app.get("/facturas", response_model=list[Factura])
def listar_facturas():
    return lista_facturas

# Endpoint para listar UNA factura por ID
@app.get("/facturas/{factura_id}", response_model=Factura)
def listar_factura(factura_id: int):
    for factura in lista_facturas:
        if factura["id"] == factura_id:
            return factura
    return {"mensaje": "Factura no encontrada"}

# Endpoint para CREAR una factura
@app.post("/facturas", response_model=Factura)
def crear_factura(datos: FacturaCrear):
    factura_validada = Factura(**datos.dict())
    lista_facturas.append(factura_validada.dict())
    return factura_validada

# Endpoint para ACTUALIZAR una factura
@app.put("/facturas/{factura_id}", response_model=Factura)
def actualizar_factura(factura_id: int, datos: FacturaCrear):
    for i, factura in enumerate(lista_facturas):
        if factura["id"] == factura_id:
            factura_actualizada = Factura(**datos.dict(), id=factura_id)
            lista_facturas[i] = factura_actualizada.dict()
            return factura_actualizada
    return {"mensaje": "Factura no encontrada"}

# Endpoint para ELIMINAR una factura
@app.delete("/facturas/{factura_id}")
def eliminar_factura(factura_id: int):
    for i, factura in enumerate(lista_facturas):
        if factura["id"] == factura_id:
            lista_facturas.pop(i)
            return {"mensaje": "Factura eliminada"}
    return {"mensaje": "Factura no encontrada"}