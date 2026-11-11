# Gestor de tareas personales
# Proyecto basico de Python para practicar Git y GitHub.

tareas = []

def mostrar_menu():
    print("\nGESTOR DE TAREAS PERSONALES")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Salir")
    print("4. Contar tareas")
    print("5. Eliminar todas las tareas")

def agregar_tarea():
    descripcion = input("Escribe la nueva tarea: ").strip()

    if descripcion == "":
        print("La tarea no puede estar vacia.")
    else:
        tareas.append(descripcion)
        print("Tarea agregada correctamente.")
    else:
        tareas.append(descripcion)
        print("Tarea agregada correctamente.")

def contar_tareas():
    print("Total de tareas registradas", len(tareas))

    if len(tareas) == 0:
        print("Todavia no tienes tareas registradas.")
    else:
        for numero, tarea in enumerate(tareas, start=1):
            print(str(numero) + ". " + tarea)

def iniciar_programa():
    opcion = ""

    while opcion != "5":
        mostrar_menu()
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            print()
        elif opcion == "4":
            print()
        elif opcion == "5":
            print("Gracias por utilizar el programa.")        
        else:
            print("Opcion no valida. Intenta nuevamente.")

iniciar_programa()
