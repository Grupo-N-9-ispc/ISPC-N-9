# Menú principal
def menu_principal():
    while True:
        print("\n--- Bienvenido al Sistema ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

# Ejecutar el programa
if __name__ == "__main__":
    # Cargar un admin por defecto
    usuarios.append(Usuario("admin", "admin@email.com", "admin123", "admin"))
    menu_principal()
