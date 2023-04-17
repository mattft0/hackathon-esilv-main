import tkinter as tk
import random

class Grid:
    def __init__(self, master):
        self.master = master
        self.width = 20
        self.height = 16
        self.grid = [[0 for j in range(self.width)] for i in range(self.height)]
        self.robot_pos = (0, 0)  # initial robot position
        self.draw_grid()

    def draw_grid(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == 0:
                    color = "white"  # empty space
                else:
                    color = "gray"  # obstacle
                # create rectangle for each cell
                x0, y0 = j*30+5, i*30+5
                x1, y1 = j*30+35, i*30+35
                self.master.create_rectangle(x0, y0, x1, y1, fill=color)
    
    def move_robot(self, direction):
        # check if move is valid
        row, col = self.robot_pos
        if direction == "up" and row > 0 and self.grid[row-1][col] == 0:
            row -= 1
        elif direction == "down" and row < self.height-1 and self.grid[row+1][col] == 0:
            row += 1
        elif direction == "left" and col > 0 and self.grid[row][col-1] == 0:
            col -= 1
        elif direction == "right" and col < self.width-1 and self.grid[row][col+1] == 0:
            col += 1
        else:
            return
        # update robot position
        self.robot_pos = (row, col)
        # clear previous robot location and draw new one
        self.master.delete("robot")
        x0, y0 = col*30+10, row*30+10
        x1, y1 = col*30+30, row*30+30
        self.master.create_oval(x0, y0, x1, y1, fill="red", tags="robot")

def create_random_grid():
    # create grid with random obstacles and empty spaces
    grid = [[0 for j in range(20)] for i in range(16)]
    for i in range(16):
        for j in range(20):
            if random.random() < 0.3:
                grid[i][j] = 1
    return grid

def main():
    root = tk.Tk()
    root.title("Robot Grid")
    canvas = tk.Canvas(root, width=620, height=500)
    canvas.pack()
    grid = Grid(canvas)
    grid.grid = create_random_grid()
    grid.draw_grid()
    root.bind("<Up>", lambda event: grid.move_robot("up"))
    root.bind("<Down>", lambda event: grid.move_robot("down"))
    root.bind("<Left>", lambda event: grid.move_robot("left"))
    root.bind("<Right>", lambda event: grid.move_robot("right"))
    root.mainloop()

if __name__ == "__main__":
    main()
