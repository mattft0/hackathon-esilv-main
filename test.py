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
        # draw robot
        self.move_robot("")

    def move_robot(self, direction):
        # move robot randomly in a valid direction
        valid_directions = []
        row, col = self.robot_pos
        if row > 0 and self.grid[row-1][col] == 0:
            valid_directions.append("up")
        if row < self.height-1 and self.grid[row+1][col] == 0:
            valid_directions.append("down")
        if col > 0 and self.grid[row][col-1] == 0:
            valid_directions.append("left")
        if col < self.width-1 and self.grid[row][col+1] == 0:
            valid_directions.append("right")
        if valid_directions:
            direction = random.choice(valid_directions)
        # clear previous robot location and draw new one
        self.master.delete("robot")
        x0, y0 = col*30+10, row*30+10
        x1, y1 = col*30+30, row*30+30
        self.master.create_oval(x0, y0, x1, y1, fill="red", tags="robot")
        # update robot position
        self.robot_pos = (row, col)

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
    root.mainloop()

if __name__ == "__main__":
    main()
