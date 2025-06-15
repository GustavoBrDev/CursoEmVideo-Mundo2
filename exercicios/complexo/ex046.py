# Contador de Ano Novo com GIF online e som
import tkinter as tk
from PIL import Image, ImageTk
import threading
import time
import requests
from io import BytesIO
import pygame

class AnoNovoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador do Ano Novo")
        self.root.geometry("600x500")

        self.label = tk.Label(root, text="=== CONTADOR DO ANO NOVO ===", font=("Helvetica", 16), fg="black")
        self.label.pack(pady=10)

        self.contador_label = tk.Label(root, text="", font=("Helvetica", 48), fg="gold")
        self.contador_label.pack()

        self.gif_label = tk.Label(root)
        self.gif_label.pack()

        self.frames = []
        self.index = 0
        self.gif_url = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWdla2JtbTVhbXk1OHN5bTNwdzZ0c3o2d3pqcmtrMDdmejQ3OGFucSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Tjkn9PamfO69Z36kwN/giphy.gif"  # GIF online
        self.som_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3"  # Som online

        self.carregar_gif_online()
        self.iniciar_contagem()

    def carregar_gif_online(self):
        try:
            response = requests.get(self.gif_url)
            gif = Image.open(BytesIO(response.content))
            while True:
                frame = gif.copy().convert("RGBA")
                self.frames.append(ImageTk.PhotoImage(frame))
                gif.seek(len(self.frames))
        except EOFError:
            pass
        except Exception as e:
            print(f"Erro ao carregar o GIF: {e}")

    def tocar_som_online(self):
        try:
            response = requests.get(self.som_url)
            with open("temp_som.mp3", "wb") as f:
                f.write(response.content)
            pygame.mixer.init()
            pygame.mixer.music.load("temp_som.mp3")
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Erro ao tocar o som: {e}")

    def exibir_gif(self):
        if not self.frames:
            return
        self.gif_label.config(image=self.frames[self.index])
        self.index = (self.index + 1) % len(self.frames)
        self.root.after(100, self.exibir_gif)

    def iniciar_contagem(self):
        threading.Thread(target=self.contagem_regressiva).start()

    def contagem_regressiva(self):
        for i in range(10, -1, -1):
            self.contador_label.config(text=str(i))
            time.sleep(1)
        self.exibir_feliz_ano_novo()

    def exibir_feliz_ano_novo(self):
        self.contador_label.config(text="Feliz Ano Novo!!!", fg="blue")
        self.exibir_gif()
        threading.Thread(target=self.tocar_som_online).start()

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = AnoNovoApp(root)
    root.mainloop()
