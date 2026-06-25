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