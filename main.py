import tkinter as tk
import heapq

class N_Puzzle:
    def __init__(self, root, size):
        self.size = size
        self.root = root
        self.buttons = []
        self.values = []
        for i in range(self.size ** 2):
            self.values.append(i)
        self.frame = tk.Frame(self.root)
        self.frame.pack()

    def create_board(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                button = tk.Button(self.frame, width=10, height=5)
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def create_buttons(self):
            k = 0
            for i in range(self.size):
                for j in range(self.size):
                    self.buttons[i][j].config(text=str(self.values[k]))
                    k += 1

    def swap(self, i1, j1, i2, j2):
        temp = self.values[i1 * self.size + j1]
        self.values[i1 * self.size + j1] = self.values[i2 * self.size + j2]
        self.values[i2 * self.size + j2] = temp
        self.create_buttons()
