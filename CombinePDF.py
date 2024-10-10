import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger

def install_dependency(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def select_files():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    return file_paths

def combine_pdfs(file_paths, output_path):
    merger = PdfMerger()
    for pdf in file_paths:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

def main():
    try:
        import PyPDF2
    except ImportError:
        print("PyPDF2 is not installed. Installing now...")
        install_dependency("PyPDF2")
        import PyPDF2

    file_paths = select_files()
    if file_paths:
        output_path = "combine.pdf"
        combine_pdfs(file_paths, output_path)
        print(f"PDFs combined successfully into {output_path}")
    else:
        print("No files selected.")

if __name__ == "__main__":
    main()
