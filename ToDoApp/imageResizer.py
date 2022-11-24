from PIL import Image

# def resize_image(img,percent):
#     resize_width = 

# How to open the image using pillow
img = Image.open("img.jpg")
resize_img = img.resize((500,300))
resize_img.save("resize_img.png")
