from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @abstractmethod
    def mostrar_info(self):
        pass

    # Getter y Setter para nombre
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    # Getter y Setter para precio
    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        if precio > 0:
            self._precio = precio
        else:
            raise ValueError("El precio debe ser mayor a cero.")


class Ropa(Producto):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio)
        self._talla = talla
        self._tipo_tela = tipo_tela

    def get_talla(self):
        return self._talla

    def set_talla(self, talla):
        self._talla = talla

    def get_tipo_tela(self):
        return self._tipo_tela

    def set_tipo_tela(self, tipo_tela):
        self._tipo_tela = tipo_tela

    @abstractmethod
    def mostrar_info(self):
        pass

class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_manga):
        super().__init__(nombre, precio, talla, tipo_tela)
        self._tipo_manga = tipo_manga

    def get_tipo_manga(self):
        return self._tipo_manga

    def set_tipo_manga(self, tipo_manga):
        self._tipo_manga = tipo_manga

    def mostrar_info(self):
        return f"Camisa: {self.get_nombre()}, Precio: {self.get_precio()} Gs, Talla: {self.get_talla()}, Tela: {self.get_tipo_tela()}, Manga: {self.get_tipo_manga()}"

class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, estilo):
        super().__init__(nombre, precio, talla, tipo_tela)
        self._estilo = estilo


    def get_estilo(self):
        return self._estilo

    def set_estilo(self, estilo):
        self._estilo = estilo

    def mostrar_info(self):
        return f"Pantalón: {self.get_nombre()}, Precio:{self.get_precio()} Gs, Talla: {self.get_talla()}, Tela: {self.get_tipo_tela()}, Estilo: {self.get_estilo()}"

class Zapato(Ropa):
    def __init__(self, nombre, precio, talla, estilo):
        super().__init__(nombre, precio, talla, tipo_tela="N/A")
        self._estilo = estilo
    def get_estilo(self):
        return self._estilo

    def set_estilo(self, estilo):
        self._estilo = estilo

    def mostrar_info(self):
        return f"Zapato: {self.get_nombre()}, Precio:{self.get_precio()} Gs, Talla: {self.get_talla()}, Estilo: {self.get_estilo()}"


class Carrito:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def mostrar_resumen(self):
        total = 0
        print("Resumen de la compra:")
        for producto in self._productos:
            print(producto.mostrar_info())
            total += producto.get_precio()
        print(f"Total a pagar: {total} Gs")

class Tienda:
    def __init__(self):
        self.inventario = []
        self.carrito = Carrito()

    def agregar_producto_inventario(self, producto):
        self.inventario.append(producto)

    def mostrar_inventario(self):
        print("Inventario:")
        for id, producto in enumerate(self.inventario, 1):
            print(f"{id}. {producto.mostrar_info()}")

    def seleccionar_producto(self, indice):
        if 0 <= indice < len(self.inventario):
            producto = self.inventario[indice]
            self.carrito.agregar_producto(producto)
            print(f"{producto.get_nombre()} añadido al carrito.")
        else:
            print("Índice de producto no válido.")

    def procesar_compra(self):
        self.carrito.mostrar_resumen()


def main():
    tienda = Tienda()

    # Agregar productos al inventario
    tienda.agregar_producto_inventario(Camisa("Camisa Blanca", 200000, "M", "Algodón", "Corta"))
    tienda.agregar_producto_inventario(Pantalon("Pantalón Jeans", 350000, "L", "Jeans", "Casual"))
    tienda.agregar_producto_inventario(Zapato("Zapato Formal", 56000, "42", "Formal"))

    while True:
        print("\nOpciones:")
        print("1. Mostrar Inventario")
        print("2. Añadir Producto al Carrito")
        print("3. Finalizar Compra y Ver Resumen")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tienda.mostrar_inventario()
        elif opcion == "2":
            indice = int(input("Selecciona el número del producto: ")) - 1
            tienda.seleccionar_producto(indice)
        elif opcion == "3":
            tienda.procesar_compra()
        elif opcion == "4":
            print("Gracias por su compra.")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
