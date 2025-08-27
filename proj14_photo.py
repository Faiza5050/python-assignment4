from PIL import Image
import matplotlib.pyplot as plt

try:
    img = Image.open("traveller.jpg")

    print("Filename:", img.filename)
    print("Format:", img.format)
    print("Mode:", img.mode)
    print("Size:", img.size)
    print("Height:", img.height)
    print("Width:", img.width)

    original = img.copy()

    bigger_original = original.resize((original.width * 2, original.height * 2))
    bigger_original.save(r'bigger_traveller.jpg')
    print("Bigger Size:", bigger_original.size)

    smaller = original.resize((200, 200))
    smaller.save(r'traveller1.jpg')
    print("Smaller Size:", smaller.size)

    r,g,b = smaller.split()

    changed = Image.merge("RGB", (g, b, r))
    changed.save(r'changed_image.jpg')

    new_img = Image.new("RGB", (2*smaller.width, 2*smaller.height), "white")
    new_img.paste(smaller, (0, 0))
    new_img.save(r'new_image.jpg')

    plt.figure(figsize=(15, 10))

    plt.subplot(1, 2, 1)
    plt.imshow(bigger_original)
    plt.title("Original")
    plt.axis("Off")

    plt.subplot(1, 3, 3)
    plt.imshow(changed)
    plt.title("Size & Color Changed")
    plt.axis("Off")

    plt.show()
    
except Exception as e:
    print(f"An Error Occurred: {e}")
