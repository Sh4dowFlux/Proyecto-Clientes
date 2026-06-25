from sqlmodel import SQLModel, Field
from typing import Optional

class ClienteBase(SQLModel):
    nombre: str = Field(nullable=False)
    email: str = Field(nullable=False)
    descripcion: Optional[str] = Field(default=None)

class ClienteCrear(ClienteBase):
    pass

class ClienteEditar(ClienteBase):
    pass

class Cliente(ClienteBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)