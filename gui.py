import tkinter as tk
from client import Client
import threading
from PIL import ImageTk, Image
from Vision.vision import Vision
import time


class GUI:
    def __init__(self, bg, size) -> None:
        self.bg = bg
        self.size = size


    def gui(self):
        self.main = MainWindow(self.size, self.bg)
        self.main.window.protocol('WM_DELETE_WINDOW', lambda: self.on_close())
        
        self.forward_button = ForwardButton(self.main.window, (400, 50))
        self.forward_button.button.config(command=lambda: threading.Thread(target=self.client.send_request, args=(b'Forward',)).start())

        self.stop_button = StopButton(self.main.window, (400, 120))
        self.stop_button.button.config(command=lambda: threading.Thread(target=self.client.send_request, args=(b'Stop',)).start())

        self.right_button = RightButton(self.main.window, (550, 120))
        self.right_button.button.config(command=lambda: threading.Thread(target=self.client.send_request, args=(b'Right',)).start())

        self.left_button = LeftButton(self.main.window, (250, 120))
        self.left_button.button.config(command=lambda: threading.Thread(target=self.client.send_request, args=(b'Left',)).start())

        self.footage_display = FootageDisplay(self.main.window, (400, 300))

        self.main.window.mainloop()
    
    def on_close(self):
        try:
            self.client.send_request(b'Stop')
        except:
            self.main.window.destroy()
        else:
            self.main.window.destroy()


class MainWindow:
    def __init__(self, size:tuple, bg):
        self.window = tk.Tk()
        self.window.geometry(f'{size[0]}x{size[1]}')
        self.window.config(bg=bg)


class ForwardButton:
    def __init__(self, master, pos:tuple):
        self.button = tk.Button(master, text='Forward', font=('default', 20), bg='#00ADBB', fg='white', width=8)
        self.button.place(x=pos[0], y=pos[1], anchor=tk.CENTER)


class StopButton:
    def __init__(self, master, pos:tuple):
        self.button = tk.Button(master, text='Stop', font=('default', 20), bg='#BB0000', fg='white', width=8)
        self.button.place(x=pos[0], y=pos[1], anchor=tk.CENTER)


class RightButton:
    def __init__(self, master, pos:tuple):
        self.button = tk.Button(master, text='Right', font=('default', 20), bg='#00ADBB', fg='white', width=8)
        self.button.place(x=pos[0], y=pos[1], anchor=tk.CENTER)


class LeftButton:
    def __init__(self, master, pos:tuple):
        self.button = tk.Button(master, text='Left', font=('default', 20), bg='#00ADBB', fg='white', width=8)
        self.button.place(x=pos[0], y=pos[1], anchor=tk.CENTER)


class FootageDisplay(Vision):
    def __init__(self, master, pos:tuple):
        super().__init__()

        self.quit = False
        self.master = master
        self.pos = pos

        self.image = Image.open('./Vision/vision.jpg')
        self.image = self.image.resize((350, 250), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.image)

        self.label = tk.Label(master, image=self.image)
        self.label.place(x=pos[0], y=pos[1], anchor=tk.CENTER)

        threading.Thread(target=self.update_image).start()

    def update_image(self):
        while True:
            try:
                self.get_footage()

                self.image = Image.open('./Vision/vision.jpg')
                self.image = self.image.resize((350, 250), Image.ANTIALIAS)
                self.image = ImageTk.PhotoImage(self.image)

                self.label = tk.Label(self.master, image=self.image)
                self.label.place(x=self.pos[0], y=self.pos[1], anchor=tk.CENTER)
            
            except:
                break

            if self.quit == True:
                break