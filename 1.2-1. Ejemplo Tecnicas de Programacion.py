class Persona:

    def __init__(self, nombre, edad, peso, estatura, ocupación):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.estatura = estatura
        self.ocupación = ocupación

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Edad:", self.edad)
        print("·Peso:", self.peso)
        print("·Estatura:", self.estatura)
        print("·Ocupación:", self.ocupación)

    def subir_nivel(self, edad, peso, estatura):
        self.edad = self.edad + edad
        self.peso = self.peso + peso
        self.estatura = self.estatura + estatura

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "no")

    def año(self, datos):
        return self.edad - datos.estatura

    def masa_corporal(self, datos):
        año = self.año(datos)
        datos.vida = datos.vida - año
        print(self.nombre, "ha realizado", año, "puntos de año a", datos.nombre)
        if datos.esta_vivo():
            print("Vida de", datos.nombre, "es", datos.vida)
        else:
            datos.morir()


class Maria(Persona):

    def __init__(self, nombre, edad, peso, estatura, ocupación):
        super().__init__(nombre, edad, peso, estatura, ocupación)
        self.educadora = educadora

    def cambiar_ocupación(self):
        opcion = int(input("Elige una ocupación: (1) Educadora, año 8. (2) Comunicadora, año 10"))
        if opcion == 1:
            self.educadora = 8
        elif opcion == 2:
            self.educadora = 10
        else:
            print("Número de ocupación incorrecta")

    def atributos(self):
        super().atributos()
        print("·Educadora:", self.educadora)

    def año(self, datos):
        return self.edad * self.peso - datos.estatura


def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno = turno + 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")


personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

personaje_1.atributos()
personaje_2.atributos()

combate(personaje_1, personaje_2)
