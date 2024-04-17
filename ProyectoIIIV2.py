class Persona:
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula

class Usuario(Persona):
    def __init__(self, nombre, apellido, cedula, username, password):
        super().__init__(nombre, apellido, cedula)
        self.username = username
        self.password = password
        self.cuentas = []

class Cuenta:
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print("Deposito exitoso.")
        else:
            print("Error: La cantidad a depositar debe ser mayor a 0.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print("Retiro exitoso.")
            else:
                print("Error: Fondos insuficientes.")
        else:
            print("Error: La cantidad a retirar debe ser positiva.")

class SistemaBancario:
    def __init__(self):
        self.usuarios = []
        self.sesion = None

    def menu_inicio_sesion(self):
        print("Bienvenido al sistema bancario.")
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        # Verificar credenciales
        for usuario in self.usuarios:
            if usuario.username == username and usuario.password == password:
                self.sesion = usuario
                self.menu_usuario()
                return
        print("Usuario o contraseña incorrectos.")

    def menu_usuario(self):
        while True:
            print("\nMenu de usuario:")
            print("1. Crear cuenta bancaria")
            print("2. Depositar")
            print("3. Retirar")
            print("4. Transferir")
            print("5. Ver Saldo")
            print("6. Salir")
            opcion = input("Seleccione una opcion: ")
            if opcion == "1":
                self.crear_cuenta_bancaria()
            elif opcion == "2":
                self.depositar()
            elif opcion == "3":
                self.retirar()
            elif opcion == "4":
                self.transferir()
            elif opcion == "5":
                self.ver_saldo()
            elif opcion == "6":
                self.cerrar_sesion()
                return
            else:
                print("Opcion no valida.")

    def crear_cuenta_bancaria(self):
        if len(self.sesion.cuentas) == 0:
            numero_cuenta = input("Ingrese el numero de cuenta (12 digitos): ")
            if len(numero_cuenta) == 12 and numero_cuenta.isdigit():
                saldo_inicial = float(input("Ingrese el saldo inicial: "))
                cuenta = Cuenta(numero_cuenta, saldo_inicial)
                self.sesion.cuentas.append(cuenta)
                print("Cuenta bancaria creada exitosamente.")
            else:
                print("El numero de cuenta debe tener exactamente 12 digitos.")
        else:
            print("Ya posee una cuenta bancaria.")

    def depositar(self):
        cuenta = self.seleccionar_cuenta()
        if cuenta:
            while True:
                cantidad = input("Ingrese la cantidad a depositar: ")
                try:
                    cantidad = float(cantidad)
                    if cantidad > 0:
                        cuenta.depositar(cantidad)
                        break
                    else:
                        print("Error: Ingrese solo valores numericos positivos.")
                except ValueError:
                    print("Error: Ingrese solo valores numericos positivos.")
                    
    def retirar(self):
        cuenta = self.seleccionar_cuenta()
        if cuenta:
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)

    def transferir(self):
        cuenta_origen = self.seleccionar_cuenta()
        if cuenta_origen:
            cedula_destino = input("Ingrese la cedula del destinatario: ")
            cuenta_destino = self.buscar_cuenta_por_cedula(cedula_destino)
            if cuenta_destino:
                cantidad = float(input("Ingrese la cantidad a transferir: "))
                if cantidad > 0:
                    if cantidad <= cuenta_origen.saldo:
                        cuenta_origen.retirar(cantidad)
                        cuenta_destino.depositar(cantidad)
                        print("Transferencia realizada exitosamente.")
                    else:
                        print("Error: Fondos insuficientes.")
                else:
                    print("Error: La cantidad a transferir debe ser positiva.")
            else:
                print("No se encontró ninguna cuenta asociada a la cedula proporcionada.")

    def seleccionar_cuenta(self):
     if len(self.sesion.cuentas) == 0:
        print("No tiene ninguna cuenta bancaria asociada.")
        return None
     else:
        print("Cuentas disponibles:")
        for i, cuenta in enumerate(self.sesion.cuentas):
            print(f"{i+1}. Numero de cuenta: {cuenta.numero_cuenta}, Saldo: {cuenta.saldo}")
        while True:
            seleccion = input("Seleccione una cuenta: ")
            try:
                seleccion = int(seleccion)
                if 1 <= seleccion <= len(self.sesion.cuentas):
                    return self.sesion.cuentas[seleccion - 1]
                else:
                    print("Error: Opcion no valida. Intente de nuevo.")
            except ValueError:
                print("Error: Opcion no valida. Intente de nuevo.")

    def ver_saldo(self):
        
        if self.sesion:
            if self.sesion.cuentas:
                saldo = self.sesion.cuentas[0].saldo 
                print(f"Saldo actual de la cuenta: {saldo}")
            else:
                print("El usuario no tiene cuentas bancarias asociadas.")
        else:
            print("Debe iniciar sesión para ver el saldo.")

    def buscar_cuenta_por_cedula(self, cedula):
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                if usuario.cuentas:
                    return usuario.cuentas[0]  
                else:
                    return None
        return None

    def cerrar_sesion(self):
        self.sesion = None
        print("Sesion cerrada.")

def main():
    sistema = SistemaBancario()
    usuario1 = Usuario("John", "Doe", "26275576", "johndoe", "123456")
    usuario2 = Usuario("Ryan", "Smith", "25645888", "ryansmith", "123456")
    usuario3 = Usuario("Angel", "Fernandez", "20861484", "aafsuareZ", "20861484")
    sistema.usuarios.extend([usuario1, usuario2,usuario3])
    while True:
        sistema.menu_inicio_sesion()

if __name__ == "__main__":
    main()
