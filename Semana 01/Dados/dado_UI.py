import tkinter as tk
from PIL import Image, ImageTk
import random

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lanzador de Dados")
root.geometry("400x500")
root.config(bg="#e5e5e5")  # Fondo gris suave para la ventana

# Título dentro de la UI
title_label = tk.Label(root, text="Lanzador de Dados", font=("Helvetica", 28, "bold"), bg="#3e8e41", fg="white")
title_label.pack(pady=20, fill='x')  # Fondo verde para el título

# Cargar imágenes de los dados
dice_images = [
    ImageTk.PhotoImage(Image.open(f"Utils\\dice{i}.png").resize((150, 150))) for i in range(1, 7)
]

# Crear un marco para la imagen del dado y el valor
frame = tk.Frame(root, bg="#e5e5e5")
frame.pack(pady=30)

# Etiqueta para mostrar la imagen del dado
dice_label = tk.Label(frame, image=dice_images[0], bg="#e5e5e5")
dice_label.pack()

# Etiqueta para mostrar el valor del dado
value_label = tk.Label(frame, text="Valor: 1", font=("Helvetica", 24, "bold"), bg="#e5e5e5", fg="#333333")
value_label.pack(pady=10)

# Función para lanzar el dado
def roll_dice():
    dice_value = random.randint(1, 6)  # Genera un número aleatorio entre 1 y 6
    dice_label.config(image=dice_images[dice_value - 1])  # Actualiza la imagen según el valor del dado
    value_label.config(text=f"Valor: {dice_value}")  # Muestra el valor del dado

# Botón para lanzar el dado
roll_button = tk.Button(root, text="Lanzar Dado", command=roll_dice, font=("Helvetica", 18, "bold"), bg="#4CAF50", fg="white", relief="flat", width=15, height=2)
roll_button.pack(pady=20)

# Efecto visual al pasar el ratón sobre el botón
def on_enter(event):
    roll_button.config(bg="#45a049")

def on_leave(event):
    roll_button.config(bg="#4CAF50")

roll_button.bind("<Enter>", on_enter)
roll_button.bind("<Leave>", on_leave)

# Iniciar el loop de la ventana
root.mainloop()
