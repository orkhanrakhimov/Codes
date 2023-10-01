from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import tempfile

def images_to_pdf(image_folder, output_pdf):
    image_files = [f for f in os.listdir(image_folder) if f.endswith(".jpg")]
    image_files.sort()

    c = canvas.Canvas(output_pdf, pagesize=letter)

    for image_file in image_files:
        img_path = os.path.join(image_folder, image_file)
        img = Image.open(img_path)

        img_width, img_height = img.size
        pdf_width, pdf_height = letter

        if img_width > pdf_width or img_height > pdf_height:
            img.thumbnail((pdf_width, pdf_height))

        
        with tempfile.NamedTemporaryFile(delete=False) as temp_img:
            img.save(temp_img, format="JPEG")

        
        c.drawImage(temp_img.name, 0, 0, width=img.width, height=img.height)
        c.showPage()

        
        os.remove(temp_img.name)

    c.save()

if __name__ == "__main__":
    image_folder = "C:/Users/PC/Desktop/cars"
    output_pdf = "C:/Users/PC/Desktop/carscode.pdf" 
    images_to_pdf(image_folder, output_pdf)




