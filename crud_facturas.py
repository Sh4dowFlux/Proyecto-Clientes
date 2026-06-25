from app.database import get_connection
from app.modelos.facturas import Factura, FacturaCrear

def obtener_facturas():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM facturas")
    facturas = cursor.fetchall()
    conn.close()
    return facturas

def obtener_factura_por_id(factura_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM facturas WHERE id = %s", (factura_id,))
    factura = cursor.fetchone()
    conn.close()
    return factura

def crear_factura(datos: FacturaCrear):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO facturas (cliente_id, fecha, total) VALUES (%s, %s, %s)",
        (datos.cliente_id, datos.fecha, datos.total)
    )
    conn.commit()
    nuevo_id = cursor.lastrowid
    conn.close()
    return obtener_factura_por_id(nuevo_id)

def actualizar_factura(factura_id: int, datos: FacturaCrear):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE facturas SET cliente_id = %s, fecha = %s, total = %s WHERE id = %s",
        (datos.cliente_id, datos.fecha, datos.total, factura_id)
    )
    conn.commit()
    conn.close()
    return obtener_factura_por_id(factura_id)

def eliminar_factura(factura_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM facturas WHERE id = %s", (factura_id,))
    conn.commit()
    conn.close()
    return {"mensaje": "Factura eliminada"}