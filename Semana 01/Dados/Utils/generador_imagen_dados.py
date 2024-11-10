from PIL import Image, ImageDraw

# Configuración de los puntos en cada lado del dado
dice_faces = {
    1: [(1, 1)],
    2: [(0, 0), (2, 2)],
    3: [(0, 0), (1, 1), (2, 2)],
    4: [(0, 0), (0, 2), (2, 0), (2, 2)],
    5: [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
    6: [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)],
}

# Tamaño de la imagen y configuraciones de los puntos
img_size = 100
dot_radius = 10
dot_color = "black"
background_color = "white"
spacing = img_size // 3

# Función para crear cada cara del dado y guardarla como una imagen
for i in range(1, 7):
    img = Image.new("RGB", (img_size, img_size), background_color)
    draw = ImageDraw.Draw(img)

    # Dibujar cada punto según su posición en la cuadrícula
    for pos in dice_faces[i]:
        x = pos[0] * spacing + spacing // 2
        y = pos[1] * spacing + spacing // 2
        draw.ellipse((x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius), fill=dot_color)

    # Guardar la imagen con el nombre diceX.png, donde X es el número de la cara
    img.save(f"dice{i}.png")

print("Imágenes de dados generadas con éxito.")