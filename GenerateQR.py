import subprocess
import sys

# Function to install a package
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required packages
required_packages = [
    "tkinter",  # This is part of the standard library, no need to install usually
    "qrcode[pil]", 
    "Pillow"
]

# Attempt to import each package, install if not found
for package in required_packages:
    try:
        if package == "tkinter":
            import tkinter as tk
        elif package == "qrcode[pil]":
            import qrcode
        elif package == "Pillow":
            from PIL import Image
    except ImportError:
        print(f"Package {package} not found. Installing...")
        install_package(package)

# Import packages after ensuring they are installed
import tkinter as tk
from tkinter import simpledialog
import qrcode
from PIL import Image

# Function to generate QR code
def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    # Save as PNG
    img.save(f"{filename}.png")

    # Convert to JPG and save
    img = img.convert("RGB")
    img.save(f"{filename}.jpg")

# Function to open the input dialog and get the URL
def get_url():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    url = simpledialog.askstring("Input", "Enter the URL:")
    if url:
        generate_qr_code(url, "qrcode")
        print(f"QR code generated and saved as 'qrcode.png' and 'qrcode.jpg'")
    else:
        print("No URL entered. QR code not generated.")

# Main function
if __name__ == "__main__":
    get_url()
