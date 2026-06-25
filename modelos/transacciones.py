from pydantic import BaseModel

# Modelo base (sin ID)
class TransaccionBase(BaseModel):
    factura_id: int
    monto: float
    fecha: str
    tipo: str  # "pago" o "cobro"

# Modelo para CREAR
class TransaccionCrear(TransaccionBase):
    pass

# Modelo para RESPONDER (con ID opcional)
class Transaccion(TransaccionBase):
    id: int | None = None