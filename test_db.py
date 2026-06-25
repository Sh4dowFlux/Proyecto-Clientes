from database import get_connection

try:
    conn = get_connection()
    print("Conexión exitosa a MySQL")
    conn.close()
except Exception as e:
    print(f"Error: {e}")