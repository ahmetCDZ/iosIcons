from PIL import Image
import os

sourcePath = "/Users/ahmetzincir/Desktop/talkingcars.jpeg"
resultPath = "/Users/ahmetzincir/Desktop/appIcons"

icons = {
    "iPhoneApp_20x20@1x": (20, 20),
    "iPhoneApp_20x20@2x": (40, 40),
    "iPhoneApp_20x20@3x": (60, 60),
    "iPhoneApp_29x29@1x": (29, 29),
    "iPhoneApp_29x29@2x": (58, 58),
    "iPhoneApp_29x29@3x": (87, 87),
    "iPhoneApp_40x40@1x": (40, 40),
    "iPhoneApp_40x40@2x": (80, 80),
    "iPhoneApp_40x40@3x": (120, 120),
    "iPhoneApp_60x60@2x": (120, 120),
    "iPhoneApp_60x60@3x": (180, 180),
    "iPhoneApp_76x76@1x": (76, 76),
    "iPhoneApp_76x76@2x": (152, 152),
    "iPhoneApp_83.5x83.5@2x": (167, 167),
    "iPhoneApp_1024x1024@1x": (1024, 1024),
}

os.makedirs(resultPath, exist_ok=True)

image = Image.open(sourcePath)

for iconName, size in icons.items():
    for kat in range(1, 4):
        resizedImage = image.resize((size[0] * kat, size[1] * kat), Image.LANCZOS)
        resultFolder = os.path.join(resultPath, f"{iconName}@{kat}x.png")
        resizedImage.save(resultFolder, format="PNG")

print("Succes")