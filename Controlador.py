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
        categoria = str(input("Digite la nueva categoría: "))
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

def eliminarProducto():
    id = int(input("Digite el ID del producto a eliminar: "))
    if id > 0:
        conn = db.connect("Productos.db")
        cursor = conn.cursor()
        query = "DELETE FROM T_Productos WHERE ID = ?"
        cursor.execute(query, (id,))
        conn.commit()
        conn.close()
        print("El producto se eliminó correctamente.")

def buscar_productos_por_categoria():
    categoria = input("Ingrese la categoría del producto: ")
    conn = db.connect("Productos.db")
    cursor = conn.cursor()
    query = "SELECT * FROM T_Productos WHERE categoria = ?"
    resultados = cursor.execute(query, (categoria,))

    print("Resultados de" , categoria )
    if resultados:
        tabla = PrettyTable(["ID", "Nombre", "Categoría", "Precio (COP)", "Stock"])
        for producto in resultados:
            tabla.add_row(producto)
        print(tabla)
    else:
        print("No se encontraron productos con esa categoria.")

def productos_con_poco_stock():
    stock_minimo = int(input("Ingrese el stock mínimo: "))
    conn = db.connect("Productos.db")
    cursor = conn.cursor()
    query = "SELECT * FROM T_Productos WHERE stock <= ?"
    resultados = cursor.execute(query, (stock_minimo,))
    print(f"Productos con stock menor o igual a {stock_minimo}")
    if resultados:
        tabla = PrettyTable(["ID", "Nombre", "Categoría", "Precio (COP)", "Stock"])
        for producto in resultados:
            tabla.add_row(producto)
        print(tabla)
    else:
        print("No se encontraron productos con poco stock.")

def buscar_productos_por_precio():
    precio_min = int(input("Ingrese el precio mínimo: "))
    precio_max = int(input("Ingrese el precio máximo: "))
    conn = db.connect("Productos.db")
    cursor = conn.cursor()
    query = "SELECT * FROM T_Productos WHERE precio BETWEEN ? AND ?"
    resultados =cursor.execute(query, (precio_min, precio_max))
    
    print("Productos con precio entre " , precio_min , " y " , precio_max)
    if resultados:
        tabla = PrettyTable(["ID", "Nombre", "Categoría", "Precio (COP)", "Stock"])
        for producto in resultados:
            tabla.add_row(producto)
        print(tabla)
    else:
        print("No se encontraron productos en ese rango de precios.")

def buscar_productos_por_nombre():
    nombre_parcial = input("Ingrese el nombre (o parte del nombre) del producto: ")
    conn = db.connect("Productos.db")
    cursor = conn.cursor()
    query = "SELECT * FROM T_Productos WHERE nombre LIKE ?"
    resultados = cursor.execute(query, ('%' + nombre_parcial + '%',))
    
    print("Resultados de" , nombre_parcial )
    if resultados:
        tabla = PrettyTable(["ID", "Nombre", "Categoría", "Precio (COP)", "Stock"])
        for producto in resultados:
            tabla.add_row(producto)
        print(tabla)
    else:
        print("No se encontraron productos con ese nombre.")