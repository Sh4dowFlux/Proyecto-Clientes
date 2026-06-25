from pydantic import BaseModel, computed_field
from datetime import datetime
from .clientes import Cliente
from .transacciones import Transaccion

# Modelo base (sin ID)
class FacturaBase(BaseModel):
    cliente_id: int
    fecha: str = datetime.now().isoformat()
    total: float = 0.0

# Modelo para CREAR
class FacturaCrear(FacturaBase):
    pass

# Modelo para EDITAR
class FacturaEditar(FacturaBase):
    pass

# Modelo para RESPONDER (con ID opcional, cliente anidado y transacciones)
class Factura(FacturaBase):
    id: int | None = None
    cliente: Cliente | None = None
    transacciones: list[Transaccion] = []

    @computed_field
    @property
    def valor_total(self) -> float:
        # Por ahora retorna 0, luego se calculará con las transacciones
        return 0.0