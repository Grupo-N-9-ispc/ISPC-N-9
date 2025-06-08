# main.py

# "from getpass" permite que el usuario escriba una contraseña sin que se vea en la consola.

from getpass import getpass 

# Datos simulados (luego se conectarán con base de datos)
usuarios = []

# Clase Usuario
class Usuario:
    def __init__(self, nombre, email, contraseña, rol="usuario"):
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña
        self.rol = rol

    def es_admin(self):
        return self.rol == "admin"

    def ver_datos(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Rol: {self.rol}\n")

# Función para validar contraseña
def validar_contraseña(clave):
    return len(clave) >= 6 and any(c.isdigit() for c in clave) and any(c.isalpha() for c in clave)
  

# Registro de usuario
def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    nombre = input("Nombre de usuario: ")
    email = input("Email: ")
    contraseña = getpass("Contraseña: ")

    if not validar_contraseña(contraseña):
        print("La contraseña debe tener al menos 6 caracteres, letras y números.")
        return

    nuevo_usuario = Usuario(nombre, email, contraseña)
    usuarios.append(nuevo_usuario)
    print("Usuario registrado con éxito.\n")
  

# Inicio de sesión
def iniciar_sesion():
    print("\n--- Inicio de Sesión ---")
    email = input("Email: ")
    contraseña = getpass("Contraseña: ")

    for usuario in usuarios:
        if usuario.email == email and usuario.contraseña == contraseña:
            print(f"\n¡Bienvenido, {usuario.nombre}!")
            if usuario.es_admin():
                menu_admin(usuario)
            else:
                menu_usuario(usuario)
            return

    print("Credenciales incorrectas.\n")

# Menú para usuario estándar
def menu_usuario(usuario):
    while True:
        print("\n--- Menú Usuario ---")
        print("1. Ver mis datos")
        print("2. Cerrar sesión")
        opcion = input("Opción: ")

        if opcion == "1":
            usuario.ver_datos()
        elif opcion == "2":
            print("Sesión cerrada.")
            break
        else:
            print("Opción no válida.")

# Menú para administrador
def menu_admin(usuario):
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Ver todos los usuarios")
        print("2. Cambiar rol de usuario")
        print("3. Eliminar usuario")
        print("4. Cerrar sesión")
        opcion = input("Opción: ")

        if opcion == "1":
            for u in usuarios:
                u.ver_datos()
        elif opcion == "2":
            email = input("Email del usuario a modificar: ")
            for u in usuarios:
                if u.email == email:
                    nuevo_rol = input("Nuevo rol (admin/usuario): ")
                    u.rol = nuevo_rol
                    print("Rol actualizado.")
                    break
            else:
                print("Usuario no encontrado.")
        elif opcion == "3":
            email = input("Email del usuario a eliminar: ")
            for u in usuarios:
                if u.email == email:
                    usuarios.remove(u)
                    print("Usuario eliminado.")
                    break
            else:
                print("Usuario no encontrado.")
        elif opcion == "4":
            print("Sesión cerrada.")
            break
        else:
            print("Opción no válida.")

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
