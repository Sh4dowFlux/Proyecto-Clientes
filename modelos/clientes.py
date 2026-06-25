from pydantic import BaseModel

# Modelo base (sin ID)
class ClienteBase(BaseModel):
    nombre: str
    email: str
    descripcion: str

# Modelo para CREAR (hereda de ClienteBase)
class ClienteCrear(ClienteBase):
    pass

# Modelo para RESPONDER (con ID opcional)
class Cliente(ClienteBase):
    id: int | None = None