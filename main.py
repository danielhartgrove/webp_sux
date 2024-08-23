from PIL import Image
import os

webp_path = input("Enter the path of the .webp: ").replace("\"", "").replace("\'", "")
# remove any quotes from the input

output_format = input("Enter the new image format: ").replace(".", "")
# remove any dots, this will be deprecated when I build a gui

print(webp_path, output_format)

if not os.path.exists(webp_path):
    print("File " + webp_path + " does not exist")
    exit(1)

image = Image.open(webp_path)
image = image.convert('RGB')

if output_format == "png" or output_format == "jpg" or output_format == "jpeg":
    image.save((webp_path.replace(".webp", "." + output_format)), output_format)
else:
    print("Invalid file format requested")
    exit(2)
