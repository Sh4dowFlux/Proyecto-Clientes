from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .facturas import Factura

class TransaccionBase(SQLModel):
    factura_id: int
    cantidad: int
    valor_unitario: float

class TransaccionCrear(TransaccionBase):
    pass

class TransaccionEditar(TransaccionBase):
    pass

class Transaccion(TransaccionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    factura: Optional[Factura] = Relationship()