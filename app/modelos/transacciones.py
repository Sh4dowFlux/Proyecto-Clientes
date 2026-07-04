from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from .facturas import Factura

class TransaccionBase(SQLModel):
    cantidad: int = Field(default=0)
    valor_unitario: float = Field(default=0.0)
    descripcion: Optional[str] = Field(default=None)
    factura_id: int = Field(foreign_key="factura.id")

class TransaccionCrear(TransaccionBase):
    pass

class TransaccionEditar(TransaccionBase):
    pass

class Transaccion(TransaccionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    factura: Optional[Factura] = Relationship()