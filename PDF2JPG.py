import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF
from PIL import Image
import os

def compress_image():
    input_file = filedialog.askopenfilename(title="Select file", filetypes=[("PDF and PNG files", "*.pdf *.png")])
    if not input_file:
        return

    input_dir = os.path.dirname(input_file)
    base_name = os.path.basename(input_file).rsplit('.', 1)[0]
    file_extension = input_file.rsplit('.', 1)[1].lower()

    try:
        quality = int(compression_entry.get())
        if not (10 <= quality <= 100):
            raise ValueError("Compression quality must be between 10 and 100")
    except ValueError as e:
        print(f"Invalid compression quality: {e}")
        return

    if file_extension == 'pdf':
        pdf_document = fitz.open(input_file)
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Increase resolution for better quality
            pix = fitz.Pixmap(pix, 0) if pix.alpha else pix
            png_file = os.path.join(input_dir, f"{base_name}-{page_num + 1:02d}.png")
            pix.save(png_file)

            # Compress the image using Pillow
            image = Image.open(png_file)
            output_file = os.path.join(input_dir, f"{base_name}-{page_num + 1:02d}.jpg")
            image.save(output_file, "JPEG", quality=quality)

        pdf_document.close()
    elif file_extension == 'png':
        image = Image.open(input_file)
        output_file = os.path.join(input_dir, f"{base_name}.jpg")
        image.save(output_file, "JPEG", quality=quality)

# Create the main window
root = tk.Tk()
root.title("Image Compressor")

# Create and place the file selection button
select_file_button = tk.Button(root, text="Select PDF or PNG File", command=compress_image)
select_file_button.pack(pady=10)

# Create and place the compression level label and entry
compression_label = tk.Label(root, text="Compression Level (10-100):")
compression_label.pack(pady=5)

compression_entry = tk.Entry(root)
compression_entry.insert(0, "80")  # Default compression quality
compression_entry.pack(pady=5)

# Run the application
root.mainloop()