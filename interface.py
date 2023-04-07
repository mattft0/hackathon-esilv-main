import tkinter as tk
from PIL import Image, ImageTk

# Définir les dimensions de la grille
GRID_WIDTH = 16
GRID_HEIGHT = 20

# Définir les dimensions des images de bâtiments
BUILDING_WIDTH = 50
BUILDING_HEIGHT = 50

# Définir les couleurs pour les cases de la grille
GRID_COLORS = ["white", "light gray", "gray"]

# Créer une fenêtre Tkinter
root = tk.Tk()

# Charger les images de bâtiments à partir des fichiers PNG
building_images = {
    "commerce": ImageTk.PhotoImage(Image.open("commerce.png").resize((BUILDING_WIDTH, BUILDING_HEIGHT))),
    "entreprise": ImageTk.PhotoImage(Image.open("entreprise.png").resize((BUILDING_WIDTH, BUILDING_HEIGHT))),
    "loisir": ImageTk.PhotoImage(Image.open("loisir.png").resize((BUILDING_WIDTH, BUILDING_HEIGHT))),
    "rue": ImageTk.PhotoImage(Image.open("rue.png").resize((BUILDING_WIDTH, BUILDING_HEIGHT))),
    "maison": ImageTk.PhotoImage(Image.open("maison.png").resize((BUILDING_WIDTH, BUILDING_HEIGHT)))
}

# Créer un canevas Tkinter pour afficher la grille
canvas = tk.Canvas(root, width=GRID_WIDTH*BUILDING_WIDTH, height=GRID_HEIGHT*BUILDING_HEIGHT)
canvas.pack()

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


# Démarrer la boucle Tkinter
root.mainloop()