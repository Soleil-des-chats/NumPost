import sys
from PIL import Image

def image_to_numworks_script(image_path, output_path):
    palette = [
        (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0),
        (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255),
        (128, 0, 0), (128, 128, 0), (0, 128, 0), (128, 0, 128),
        (0, 128, 128), (192, 192, 192), (128, 128, 128), (0, 0, 128)
    ]

    def closest_color(color):
        return min(range(len(palette)), key=lambda i: sum((x-y)**2 for x, y in zip(palette[i], color)))

    img = Image.open(image_path).convert('RGB').resize((80, 60))

    data = ""
    for y in range(60):
        for x in range(80):
            color = img.getpixel((x, y))
            data += hex(closest_color(color))[2:].upper()

    script = f"""
from kandinsky import *

pal = {palette}
im = "{data}"

def rect(x, y, c):
    for i in range(16):
        set_pixel(4*x + i % 4, 4*y + i // 4, c)

def draw():
    for i in range(80*60):
        c = pal[int("0x" + im[i])]
        rect(i % 80, i // 80, color(c[0], c[1], c[2]))

draw()
"""

    with open(output_path, 'w') as file:
        file.write(script)

def main():
    if len(sys.argv) != 3:
        print("Usage: python generate_script.py <image_path> <output_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    output_path = sys.argv[2]
    
    image_to_numworks_script(image_path, output_path)
    print(f"Successfully generated : {output_path}")

if __name__ == "__main__":
    main()
