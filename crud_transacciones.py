from database import get_connection
from modelos.transacciones import Transaccion, TransaccionCrear

def obtener_transacciones():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM transacciones")
    transacciones = cursor.fetchall()
    conn.close()
    return transacciones

def obtener_transaccion_por_id(transaccion_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM transacciones WHERE id = %s", (transaccion_id,))
    transaccion = cursor.fetchone()
    conn.close()
    return transaccion

def crear_transaccion(datos: TransaccionCrear):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transacciones (factura_id, monto, fecha, tipo) VALUES (%s, %s, %s, %s)",
        (datos.factura_id, datos.monto, datos.fecha, datos.tipo)
    )
    conn.commit()
    nuevo_id = cursor.lastrowid
    conn.close()
    return obtener_transaccion_por_id(nuevo_id)

def actualizar_transaccion(transaccion_id: int, datos: TransaccionCrear):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE transacciones SET factura_id = %s, monto = %s, fecha = %s, tipo = %s WHERE id = %s",
        (datos.factura_id, datos.monto, datos.fecha, datos.tipo, transaccion_id)
    )
    conn.commit()
    conn.close()
    return obtener_transaccion_por_id(transaccion_id)

def eliminar_transaccion(transaccion_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transacciones WHERE id = %s", (transaccion_id,))
    conn.commit()
    conn.close()
    return {"mensaje": "Transaccion eliminada"}