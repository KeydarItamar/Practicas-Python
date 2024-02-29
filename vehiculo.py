class Vehiculo:
    def __init__(self, nombre, color, marca, año, nuevo, puertas):
        self.nombre = nombre
        self.color = color
        self.marca = marca
        self.año = año
        self.nuevo= nuevo
        self.puertas = puertas
    
    def get_nombre(self):
        return self.nombre

    def get_color(self):
        return self.color

    def get_marca(self):
        return self.marca

    def get_año(self):
        return self.año

    def es_nuevo(self):
        return self.nuevo

    def get_puertas(self):
        return self.puertas

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_color(self, nuevo_color):
        self.color = nuevo_color

    def set_marca(self, nueva_marca):
        self.marca = nueva_marca

    def set_año(self, nuevo_año):
        self.año = nuevo_año

    def set_nuevo(self, nuevo_estado):
        self.nuevo = nuevo_estado

    def set_puertas(self, nuevas_puertas):
        self.puertas = nuevas_puertas

    def nom_parts(self):
        return f'''Datos del coche: 
                Nombre: {self.nombre}, Color: {self.color} 
                Marca: {self.marca}, Año: {self.año} 
                Nuevo: {self.nuevo}, Puertas: {self.puertas} '''

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "color": self.color,
            "marca": self.marca,
            "año": self.año,
            "nuevo": self.nuevo,
            "puertas": self.puertas
        }
         
coche1 = Vehiculo("Civic", "Rojo", "Honda", 2020, True, 4)

print(coche1.nom_parts())
print(coche1.to_dict())