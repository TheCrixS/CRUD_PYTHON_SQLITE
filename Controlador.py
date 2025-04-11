import sqlite3 as db
from prettytable import PrettyTable

def crearProducto():
    id = int(input("Digite el ID: "))
    nombre = str(input("Digite el nombre: "))
    categoria = str(input("Digite la categoría: "))
    precio = float(input("Digite el precio: "))
    stock = int(input("Digite la cantidad de stock: "))

    if(id>0 and len(nombre)>0 and len(categoria)>0 and precio>0 and stock>0):
        conn = db.connect("Productos.db")
        cursor = conn.cursor()
        query = """
                    INSERT INTO T_Productos(
                        ID, nombre, categoria, precio, stock
                    ) VALUES (
                        ?,?,?,?,?
                    )
                """
        cursor.execute(query, (id, nombre, categoria, precio, stock))
        conn.commit()
        print("El producto se agregó correctamente.")

def mostrarProductos():
    conn = db.connect("Productos.db")
    query = "SELECT * FROM T_Productos"
    cursor = conn.cursor()
    respuesta = cursor.execute(query)
    for registro in respuesta:
        print("""
    ID: {}
    Nombre: {}
    Categoría: {}
    Precio: {}
    Stock: {}
            """.format(registro[0],registro[1],registro[2],registro[3],registro[4]))
        
def actualizarProducto():
    id = int(input("Digite el ID: "))
    if(id>0):
        conn = db.connect("Productos.db")
        cursor = conn.cursor()
        nombre = str(input("Digite el nuevo nombre: "))
        categoria = str(input("Digite el nuevo nombre: "))
        precio = float(input("Digite el nuevo precio: "))
        stock = int(input("Digite la nueva cantidad de stock: "))
        query = """
                   UPDATE T_Productos SET nombre = ?, categoria = ?, precio = ?, stock = ?
                   WHERE ID = ?
               """
        cursor.execute(query, (nombre, categoria, precio, stock, id))
        conn.commit()
        conn.close()
        print("El producto se actualizó correctamente.")
