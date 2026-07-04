from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .facturas import Factura

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
    facturas: List["Factura"] = Relationship(back_populates="cliente")

# Modelo de lectura
class ClienteLeer(ClienteBase):
    id: int