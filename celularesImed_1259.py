class Imed1259:
    def diccionario1259(self):
        proveedor1259 = {
            "Id proveedor": 22308051281259,
            "Nombre": "Nicolas",
            "Apellido": "Medina",
            "Telefono": 6571014236,
            "correo": "a.22308051281259@cbtis128.edu.mx",
            "Edad": 45,
            "Direccion": "Calle Garambullo 1259"
        }
        print(proveedor1259)
        for Pro,ved in proveedor1259.items():
            print(f"Datos: {Pro} : {ved}")

    def Stock1259(self):
        Inventario1259 = {
        "Id Inventario": 1259,
        "Marca": "Iphone y samsung",
        "Modelo": "Pro max y Galaxy",
        "Cantidad": 1000,
        "Año": 2019 - 2023,
        "id Proveedor": 22308051281259,
        "Sucursal": "Calle Ajonjoli 1259"
    }
        print(Inventario1259)
        for Pro,ved in Inventario1259.items():
            print(f"Datos {Pro} : {ved}")

    def Celulares1259(self):
        Celular1259 = {
        "Id Celulares": 1259,
        "Marca": "Iphone y samsung",
        "Modelo": "Pro max y Galaxy",
        "Gama": "Media y alta",
        "Precios": "Arribla de 2000 dolares",
        "id Proveedor": 22308051281259,
        "id Inventario": 1259
    }
        print(Celular1259)
        for cel,ular in Celular1259.items():
            print(f"Datos {cel} : {ular}")

    def Clientes1259(self):
        clientes1259 = {
        "Id Clientes": 1259,
        "Nombres": "nombre del cliente",
        "Apellidos": "Apellidos del cliente",
        "correo": "Electronico",
        "Telefono": "Telefono del cliente",
        "direccion": "direccion oficial del cliente",
        "Historial": "Historial de compras del cliente",
        "id Inventario": 1259
    }
        print(clientes1259)
        for cel,ular in clientes1259.items():
            print(f"Datos {cel} : {ular}")

obj1259 =  Imed1259()

print("")
print("-Proveedor-")
print("")
obj1259.diccionario1259()
print("")
print("-Stock-")
print("")
obj1259.Stock1259()
print("")
print("-Celulares-")
print("")
obj1259.Celulares1259()
print("")
print("-Clientes-")
print("")
obj1259.Clientes1259()

