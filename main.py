from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar

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
    raise HTTPException(status_code=404, detail=f"El cliente con ID {cliente_id} no existe")

# Crear un cliente (con ID automático)
@app.post("/clientes", response_model=Cliente)
async def crear_cliente(datos: ClienteCrear):
    # Generar ID automático
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
    raise HTTPException(status_code=404, detail=f"El cliente con ID {cliente_id} no existe")

# Eliminar un cliente (DELETE)
@app.delete("/clientes/{cliente_id}")
async def eliminar_cliente(cliente_id: int):
    for i, cliente in enumerate(lista_clientes):
        if cliente["id"] == cliente_id:
            lista_clientes.pop(i)
            return {"mensaje": "Cliente eliminado correctamente"}
    raise HTTPException(status_code=404, detail=f"El cliente con ID {cliente_id} no existe")