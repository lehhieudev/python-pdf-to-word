from pdf2docx import Converter
from pdf2image import convert_from_path
import pytesseract
from docx import Document
import os

def convert_pdf_to_word(pdf_path, word_path):
    try:
        cv = Converter(pdf_path)
        cv.convert(word_path, start=0, end=None)
        cv.close()
        print(f"Converted {pdf_path} to {word_path} successfully!")
    except Exception as e:
        print(f"Error converting {pdf_path}: {e}")

# Convert PDF to Word with formatting
convert_pdf_to_word("How to Think Like a Computer Scientist--Learinig with Python.pdf", "How to Think Like a Computer Scientist--Learinig with Python.docx")