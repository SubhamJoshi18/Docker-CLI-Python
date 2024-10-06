import PyPDF2
from gtts import gTTS
from constant.FilePathConstant import container_audio
import os
import pyttsx3

def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path,'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text() + "\n"
    return text



def translate(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.setProperty('volume',1)
    engine.say(text)
    engine.runAndWait()






def text_to_speech(text, language='en'):
    custom_text = f'There are {len(text)} container in your docker engine'
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)

    engine.say(custom_text)
    engine.runAndWait()

