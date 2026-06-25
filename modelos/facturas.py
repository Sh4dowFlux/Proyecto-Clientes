from pydantic import BaseModel
from .clientes import Cliente

# Modelo base (sin ID)
class FacturaBase(BaseModel):
    cliente_id: int
    fecha: str
    total: float

# Modelo para CREAR
class FacturaCrear(FacturaBase):
    pass

# Modelo para EDITAR
class FacturaEditar(FacturaBase):
    pass

# Modelo para RESPONDER (con ID opcional)
class Factura(FacturaBase):
    id: int | None = None