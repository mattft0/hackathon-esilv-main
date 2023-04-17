import tkinter as tk
from PIL import Image, ImageTk
import random
import time

from matplotlib.pyplot import grid
import robot

# Définir les dimensions de la grille
GRID_WIDTH = 16
GRID_HEIGHT = 20

# Définir les dimensions des images de bâtiments
BUILDING_WIDTH = 50
BUILDING_HEIGHT = 50

# Définir les couleurs pour les cases de la grille
GRID_COLORS = ["white", "light gray", "gray"]


def on_button_click():
    print("Button clicked")


# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Robot City")

# Charger les images de bâtiments à partir des fichiers PNG
building_images = {
    "commerce": ImageTk.PhotoImage(Image.open("commerce.png").resize((BUILDING_WIDTH, BUILDING_HEIGHT))),
    "entreprise": ImageTk.PhotoImage(Image.open("entreprise.png").resize((BUILDING_WIDTH, BUILDING_HEIGHT))),
    "loisir": ImageTk.PhotoImage(Image.open("loisir.png").resize((BUILDING_WIDTH, BUILDING_HEIGHT))),
    "rue": ImageTk.PhotoImage(Image.open("rue.png").resize((BUILDING_WIDTH, BUILDING_HEIGHT))),
    "maison": ImageTk.PhotoImage(Image.open("maison.png").resize((BUILDING_WIDTH, BUILDING_HEIGHT))),
    "robot": ImageTk.PhotoImage(Image.open("tes2.png").resize((BUILDING_WIDTH, BUILDING_HEIGHT)))
}


# Définir la position initiale du robot
robot_position = (2 * BUILDING_WIDTH, 2 * BUILDING_HEIGHT)


# Dessiner l'image du robot à sa position actuelle sur la grille
def draw_robot():
    global robot_position
    x, y = robot_position
    if x < 0 or x >= GRID_WIDTH*BUILDING_WIDTH or y < 0 or y >= GRID_HEIGHT*BUILDING_HEIGHT:
        # Le robot est sorti de la grille
        return
    i = y // BUILDING_HEIGHT
    j = x // BUILDING_WIDTH
    if grid[i][j] != "R":
        # Le robot est sur une case qui n'est pas une rue
        return
    canvas.create_image(x, y, anchor="nw", image=building_images["robot"])


button = tk.Button(root, text="Click me!", command=on_button_click)
button.pack()
# Créer un canevas Tkinter pour afficher la grille
canvas = tk.Canvas(root, width=GRID_WIDTH*BUILDING_WIDTH, height=GRID_HEIGHT*BUILDING_HEIGHT)
canvas.pack()

# Dessiner l'image du robot à sa position actuelle sur la grille
def draw_robot():
    global robot_position
    x, y = robot_position
    canvas.create_image(x, y, anchor="nw", image=building_images["robot"])


# Lire le fichier texte mapcity.txt pour placer les bâtiments sur la grille
with open("mapcity.txt", "r") as f:
    for i in range(GRID_HEIGHT):
        line = f.readline().strip().ljust(GRID_WIDTH, "0")
        for j in range(GRID_WIDTH):
            building_type = line[j]
            if building_type == "M":
                color_index = 2
            elif building_type == "C":
                color_index = 0
            elif building_type == "E":
                color_index = 1
            elif building_type == "R":
                color_index = 0
            elif building_type == "D":
                color_index = 2
            else:
                color_index = 0

            color = GRID_COLORS[color_index]
            x = j * BUILDING_WIDTH
            y = i * BUILDING_HEIGHT
            canvas.create_rectangle(x, y, x+BUILDING_WIDTH, y+BUILDING_HEIGHT, fill=color)

            if building_type != "0":
                building_image = building_images[{"M": "maison", "R": "rue", "C": "commerce", "E": "entreprise", "D": "loisir"}[building_type]]
                canvas.create_image(x, y, anchor="nw", image=building_image)

ROBOT_SPEED = 500

def move_robot():
    global robot_position
    x, y = robot_position
    
    # Liste des directions possibles
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Choisir une direction aléatoire
    dx, dy = random.choice(directions)
    
    # Calculer la nouvelle position
    new_x = x + dx * BUILDING_WIDTH
    new_y = y + dy * BUILDING_HEIGHT
    
    # Vérifier si la nouvelle position est valide
    if new_x < 0 or new_x >= GRID_WIDTH * BUILDING_WIDTH or new_y < 0 or new_y >= GRID_HEIGHT * BUILDING_HEIGHT:
        return
    if building_type != "R":
        return
    
    # Effacer l'image du robot à sa position actuelle sur la grille
    canvas.delete("robot")
    
    # Mettre à jour la position du robot
    robot_position = (new_x, new_y)
    
    # Dessiner l'image du robot à sa nouvelle position sur la grille
    draw_robot()


# Boucle principale pour déplacer le robot
while True:
    draw_robot()  # dessiner le robot à sa position actuelle
    root.update()  # mettre à jour la fenêtre Tkinter
    time.sleep(ROBOT_SPEED / 1000)  # attendre un certain temps
    move_robot()  # déplacer le robot aléatoireme

# Démarrer la boucle Tkinter
root.mainloop()