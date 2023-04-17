import random

class Robot:
    def __init__(self, city):
        self.city = city
        self.x = 0
        self.y = 0
        self.directions = ["N", "S", "W", "E"]


    def move(self):
        # Choisir une direction aléatoire
        direction = random.choice(self.directions)


        # Calculer la nouvelle position en fonction de la direction choisie
        new_x, new_y = self.x, self.y
        if direction == "N":
            new_y -= 1
        elif direction == "S":
            new_y += 1
        elif direction == "W":
            new_x -= 1
        elif direction == "E":
            new_x += 1


        # Vérifier que la nouvelle position est sur une case rue de la ville
        if self.city.get_building_type(new_x, new_y) == "R":
            self.x, self.y = new_x, new_y


    def get_position(self):
        return self.x, self.y
