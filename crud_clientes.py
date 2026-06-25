from database import get_connection
from modelos.clientes import Cliente, ClienteCrear

def obtener_clientes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def obtener_cliente_por_id(cliente_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes WHERE id = %s", (cliente_id,))
    cliente = cursor.fetchone()
    conn.close()
    return cliente

def crear_cliente(datos: ClienteCrear):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO clientes (nombre, email, descripcion) VALUES (%s, %s, %s)",
        (datos.nombre, datos.email, datos.descripcion)
    )
    conn.commit()
    nuevo_id = cursor.lastrowid
    conn.close()
    return obtener_cliente_por_id(nuevo_id)

def actualizar_cliente(cliente_id: int, datos: ClienteCrear):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE clientes SET nombre = %s, email = %s, descripcion = %s WHERE id = %s",
        (datos.nombre, datos.email, datos.descripcion, cliente_id)
    )
    conn.commit()
    conn.close()
    return obtener_cliente_por_id(cliente_id)

def eliminar_cliente(cliente_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
    conn.commit()
    conn.close()
    return {"mensaje": "Cliente eliminado"}