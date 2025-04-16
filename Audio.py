import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)  # Updated to PdfReader
pages = len(pdfreader.pages)  # Updated to get the number of pages

for num in range(0, pages):
    page = pdfreader.pages[num]  # Updated to access pages
    text = page.extract_text()  # Updated to extract text
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()