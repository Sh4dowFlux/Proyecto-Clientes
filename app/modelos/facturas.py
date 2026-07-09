from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .clientes import Cliente
    from .transacciones import Transaccion


class FacturaBase(SQLModel):
    fecha: str = Field(default=datetime.now().isoformat())
    total: float = Field(default=0.0)
    cliente_id: int = Field(foreign_key="cliente.id")


class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(FacturaBase):
    pass


class Factura(FacturaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cliente: Optional["Cliente"] = Relationship(back_populates="facturas")
    transacciones: List["Transaccion"] = Relationship(back_populates="factura")


class FacturaLeer(FacturaBase):
    id: int