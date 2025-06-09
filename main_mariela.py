
  

# Definimos función para el registro de usuario.

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
  

# Definimos función para el inicio de sesión.

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
    
