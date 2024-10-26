from abc import ABC, abstractmethod 

class Prenda(ABC):
    
    def __init__(self,nombre,precio,cantidad,talla) -> None:
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
        self.talla=talla
        super().__init__()
        
    @abstractmethod
    
    def mostrar_info(self):
        pass
    
    def mostrar_precio(self):
        
        return self.precio
    

        
class Camisa(Prenda):
    def __init__(self, nombre, precio, cantidad,talla,manga) -> None:
        super().__init__(nombre, precio, cantidad,talla)
        self.manga=manga
    
        
    def mostrar_info(self):
    
        return f"Camisa: {self.nombre}, Precio: ${self.precio},Cantidad:{self.cantidad},Talla: {self.talla},Manga:{self.manga}"
class Pantalon(Prenda):
    def __init__(self, nombre, precio, talla,cantidad,largor):
        super().__init__(nombre, precio,cantidad,talla)
        self.largor = largor

    def mostrar_info(self):
        return f"Pantalon: {self.nombre}, Precio: ${self.precio},Cantidad:{self.cantidad}, Talla: {self.talla}, Largor: {self.largor}"
    
class Vestido(Prenda):
    def __init__(self, nombre, precio, talla,cantidad,estilo):
        super().__init__(nombre, precio,talla,cantidad)
        self.estilo = estilo

    def mostrar_info(self):
        return f"Vestido: {self.nombre}, Precio: ${self.precio},Cantidad:{self.cantidad}, Talla: {self.talla}, Estilo: {self.estilo}"
        

class Tienda:
    def __init__(self):
        self.inventario = []

    def agregar_producto(self, producto):
        self.inventario.append(producto)

    def mostrar_inventario(self):
        for producto in self.inventario:
            print(producto.mostrar_info())

    def procesar_compra(self, nombre_producto):
        for producto in self.inventario:
            if producto.nombre == nombre_producto:
                print(f"Compraste {nombre_producto} por ${producto.mostrar_precio()}")
                self.inventario.remove(producto)
                return
        print("Producto no encontrado.")
        
#Implementacion
tienda = Tienda()
camisa = Camisa("Camisa Blanca", 20,2, "M", "Corta")
pantalon = Pantalon("Pantalón Azul", 30, "L",2, "Medio")
vestido=Vestido("Vestido Rosa",50,2,"M","Elegante")
tienda.agregar_producto(camisa)
tienda.agregar_producto(pantalon)
tienda.agregar_producto(vestido)

print("Inventario:")
tienda.mostrar_inventario()


