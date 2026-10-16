# Eduardo Covarrubias Martinez, christopher Herrera, Terence Keating
# Equipo 5
# 13/10/26

class PersonajeMinecraft():
    def __init__(self, nombre= "Steve", vida=10, nivel=15):
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel

    def atacar(self, objetivo, danio):
        print(f"El jugador ha blandido su espada a la {objetivo} para {danio} danio")

    def toString(self):
        return f"Nombre: {self.nombre} Vida: {self.vida} Nivel: {self.nivel}"

class Guerrero(PersonajeMinecraft):
    def __init__(self, nombre= "Steve", vida=10, nivel=15, tipoEspada="Diamante"):
        super().__init__(nombre, vida, nivel)
        
        self.tipoEspada = tipoEspada

    def golpeEspecial(self):
        texto = self.toString()
        print(f"{texto} realizar una Golpe Especial con su espada")

class Constructor(PersonajeMinecraft):
    def __init__(self, nombre= "Steve", vida=10, nivel=15, materialFavorito="maderaDePino"):
        super().__init__(nombre, vida, nivel)

        self.materialFavorito = materialFavorito

    def construir(self):
        texto = self.toString()
        print(f"{texto} esta construyendo con {self.materialFavorito}")


j1 = Guerrero("Steve", 9, 14, "Oro")
j1.atacar("Creeper", 3.5)
j1.atacar("Creeper", 3.5)
j1.golpeEspecial()

j2 = Constructor("Alex", 8, 7, "Adoquín")
j2.atacar("Zombi", 2)

j2.construir()

