import time
import Modelo as mod
import Controlador as con

while True:
    print("Sistema de Gestión de Productos Electrónicos.")
    print("______________________________________")
    print("Seleccione una opción para iniciar:")
    print("1. Crear base de datos y tabla.")
    print("2. Agregar nuevo producto.")
    print("3. Mostrar lista de productos.")
    print("4. Actualizar producto.")
    print("5. Eliminar un producto.")
    print("6. Buscar productos por categoría.")
    print("7. Buscar productos con poco stock.")
    print("8. Buscar productos por un rango de precios.")
    print("9. Buscar productos por nombre (o parte del nombre)")
    print("0. Salir.")
    print("______________________________________")

    try:
        op = int(input("Ingrese una opción: "))
        if op == 1:
            mod.crearBaseDeDatos()
            mod.crearTabla()
            time.sleep(1)
        elif op == 2:
            con.crearProducto()
            time.sleep(1)
        elif op == 3:
            con.mostrarProductos()
            time.sleep(1)
        elif op == 4:
            print("WIP...") 
            time.sleep(1)
        elif op == 5:
            print("WIP...")
            time.sleep(1)
        elif op == 6:
            print("WIP...")
            time.sleep(1)
        elif op == 7:
            print("WIP...")
            time.sleep(1)
        elif op == 8:
            print("WIP...")
            time.sleep(1)
        elif op == 9:
            print("WIP...")
            time.sleep(1)
        elif op == 0:
            exit()
        else:
            print("Digite una opción válida.")
            time.sleep(1)
    except ValueError as e:
        if e:
            print("Digite un valor numérico.")
            time.sleep(1)
        else:
            print("Error de conexión con la base de datos.")
            time.sleep(1)