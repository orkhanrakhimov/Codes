from PIL import Image, ImageEnhance, ImageFilter
import os

# input and output directories (add your path)
input_directory = "C:/Users/PC/Desktop/unedited_Images"
output_directory = "C:/Users/PC/Desktop/edited_Images"

# adjustable parameters
enhancement_factor = 1.5
rotation_angle = 0

def process_image(input_path, output_path):
    try:
        # Check if the file is an image
        img = Image.open(input_path)
        
        # black and white effect
        img = img.convert('L')
        
        img = img.filter(ImageFilter.SHARPEN).rotate(rotation_angle)
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(enhancement_factor)
        img.save(output_path)
    except (IOError, OSError) as e:
        print(f"Error processing {input_path}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

for filename in os.listdir(input_directory):
    input_path = os.path.join(input_directory, filename)
    output_filename = f"{os.path.splitext(filename)[0]}_edited.jpg"
    output_path = os.path.join(output_directory, output_filename)
    process_image(input_path, output_path)


    