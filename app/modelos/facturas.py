from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, List
from .clientes import Cliente

class FacturaBase(SQLModel):
    cliente_id: int = Field(foreign_key="cliente.id")
    fecha: str = Field(default=datetime.now().isoformat())
    total: float = Field(default=0.0)

class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cliente: Optional[Cliente] = Relationship()
    transacciones: List["Transaccion"] = Relationship()
    
    @property
    def valor_total(self) -> float:
        total = 0.0
        for transaccion in self.transacciones:
            total += transaccion.cantidad * transaccion.valor_unitario
        return total