class Voiture:
    def __init__(self, couleur, marque, puissanceMoteur) -> None:
        self.couleur = couleur
        self.marque = marque
        self.puissance = puissanceMoteur

    def __str__(self) -> str:
        return f"{self.marque} de couleur {self.couleur} avec une puissance de {self.puissance}"
    
voiture1 = Voiture("blue", "toyota", 700)
print(voiture1)