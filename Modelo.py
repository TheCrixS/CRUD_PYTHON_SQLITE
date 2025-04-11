import sqlite3 as db

def crearBaseDeDatos():
    conn = db.connect("Productos.db")
    print("La base de datos se creó correctamente.")
    conn.commit()
    conn.close()

def crearTabla():
    conn = db.connect("Productos.db")
    query = """
            CREATE TABLE IF NOT EXISTS T_Productos(
                ID Integer primary key,
                nombre text,
                categoria text,
                precio real,
                stock integer
            )
        """
    conn.execute(query)
    conn.commit()
    print("La tabla se creó correctamente.")