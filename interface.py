import tkinter as tk
from PIL import Image, ImageTk
import random
import time
from matplotlib.pyplot import grid
import robot

# Définir les dimensions de la grille
GRID_WIDTH = 20
GRID_HEIGHT = 16

# Définir les dimensions des images de bâtiments
BUILDING_WIDTH = 50
BUILDING_HEIGHT = 50

# Définir les couleurs pour les cases de la grille
GRID_COLORS = ["white", "light gray", "gray"]


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
    "robot": ImageTk.PhotoImage(Image.open("tes2.png").resize((BUILDING_WIDTH, BUILDING_HEIGHT))),
}

robot_position = (100,100)

robot_image = Image.open("tes2.png")
robot_image = robot_image.resize((50, 50)) # Redimensionner l'image
robot_photo = ImageTk.PhotoImage(robot_image)

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
    global image
    image = canvas.create_image(x, y, image=robot_photo, anchor="nw")
    
    
# Déplacer le robot d'une case dans la direction indiquée
def move_robot():
    canvas.delete(image)
    global robot_position
    x, y = robot_position
    # Choisir une direction aléatoire
    direction = random.choice(["up", "down", "left", "right"])

    # Déplacer le robot d'une case dans la direction choisie
    if direction == "up":
        y -= BUILDING_HEIGHT
    elif direction == "down":
        y += BUILDING_HEIGHT
    elif direction == "left":
        x -= BUILDING_WIDTH
    elif direction == "right":
        x += BUILDING_WIDTH

    robot_position = (x, y)

    # Supprimer l'image du robot de la grille et la redessiner à sa nouvelle position
    draw_robot()





button2 = tk.Button(root, text="Draw", command=draw_robot)
button2.pack()
button3 = tk.Button(root, text="Play", command=move_robot)
button3.pack()
button = tk.Button(root, text="Quit", command=root.destroy)
button.pack()
# Créer un canevas Tkinter pour afficher la grille
canvas = tk.Canvas(root, width=GRID_WIDTH*BUILDING_WIDTH, height=GRID_HEIGHT*BUILDING_HEIGHT)
canvas.pack()



# Lire le fichier texte mapcity.txt pour placer les bâtiments sur la grille
with open("mapcity.txt", "r") as f:
    grid = [[cell for cell in line.strip()] for line in f]
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            building_type = grid[i][j]
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


# Démarrer la boucle Tkinter
root.mainloop()