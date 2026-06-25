from pydantic import BaseModel, computed_field
from datetime import datetime
from .clientes import Cliente
from .transacciones import Transaccion

class FacturaBase(BaseModel):
    cliente_id: int
    fecha: str = datetime.now().isoformat()

class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None
    cliente: Cliente | None = None
    transacciones: list[Transaccion] = []

    @computed_field
    @property
    def valor_total(self) -> float:
        total = 0.0
        for transaccion in self.transacciones:
            total += transaccion.cantidad * transaccion.valor_unitario
        return total