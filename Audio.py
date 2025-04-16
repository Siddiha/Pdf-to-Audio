import pyttsx3
import PyPDF2
from tkinter.filedialog import *


book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book);
pages = pdfreader.numPages