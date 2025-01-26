class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        print(f"Cuenta creada para {self.titular} con saldo inicial de {self.saldo}")

    def __del__(self):
        print(f"Cuenta de {self.titular} cerrada")

# Crear una instancia de la clase CuentaBancaria
cuenta1 = CuentaBancaria("Lams1474", 1000)

# Eliminar la instancia
del cuenta1