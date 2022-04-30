import tkinter as tk
from client import Client


class GUI:
    def __init__(self, bg, size) -> None:
        self.bg = bg
        self.size = size
        self.client = Client('192.168.1.68', 65432)

    def gui(self):
        self.main = MainWindow(self.size, self.bg)
        self.forward_button = ForwardButton(self.main.window, (400, 50))

        self.main.window.mainloop()


class MainWindow:
    def __init__(self, size:tuple, bg):
        self.window = tk.Tk()
        self.window.geometry(f'{size[0]}x{size[1]}')
        self.window.config(bg=bg)


class ForwardButton:
    def __init__(self, master, pos:tuple):
        self.button = tk.Button(master, text='Forwards', font=('default', 20), bg='#00ADBB', fg='white')
        self.button.place(x=pos[0], y=pos[1], anchor=tk.CENTER)
