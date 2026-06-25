from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo de cliente
class Cliente(BaseModel):
    id: int
    nombre: str
    email: str
    descripcion: str

# Lista de clientes (estática)
lista_clientes: list[Cliente] = [
    {"id": 1, "nombre": "Ana", "email": "ana@gmail.com", "descripcion": "Cliente frecuente"},
    {"id": 2, "nombre": "Luis", "email": "luis@gmail.com", "descripcion": "Cliente nuevo"},
    {"id": 3, "nombre": "Maria", "email": "maria@gmail.com", "descripcion": "Cliente VIP"}
]

# Endpoint para listar TODOS los clientes
@app.get("/clientes")
def listar_clientes():
    return lista_clientes

# Endpoint para listar UN cliente por ID
@app.get("/clientes/{cliente_id}")
def listar_cliente(cliente_id: int):
    for cliente in lista_clientes:
        if cliente["id"] == cliente_id:
            return cliente
    return {"mensaje": "Cliente no encontrado"}

# Endpoint para CREAR un cliente
@app.post("/clientes")
def crear_cliente(datos: Cliente):
    lista_clientes.append(datos.dict())
    return datos

@app.put("/clientes/{cliente_id}")
def actualizar_cliente(cliente_id: int, datos: Cliente):
    for i, cliente in enumerate(lista_clientes):
        if cliente["id"] == cliente_id:
            lista_clientes[i] = datos.dict()
            return datos
    return {"mensaje": "Cliente no encontrado"}

@app.delete("/clientes/{cliente_id}")
def eliminar_cliente(cliente_id: int):
    for i, cliente in enumerate(lista_clientes):
        if cliente["id"] == cliente_id:
            lista_clientes.pop(i)
            return {"mensaje": "Cliente eliminado"}
    return {"mensaje": "Cliente no encontrado"}