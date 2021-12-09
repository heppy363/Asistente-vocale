import speech_recognition as sr
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import prova_funzioni # file che contiene le funzioni che esegue l'assistente vocale

"""

Asistenet Vocale di Matteo Rossi Verione 0.5.20
in opero.File che contiene il codice sorgente del programma spezzato 
due parti questo contiene Il codice che avvia il programmna il resto si può trovare in funzioni.py, l'intelligenza
vocale è contenuta nel file intents.json 

descrizzioni funzioni ==>

Tempo = molstra il l'orario.
chi_sei = dice a che versione è l'assitente. 
CMD = apre il CMD.
Saluto = saluta l'interlicutore.
Leggi_PDF = trasforma un PDF in un file audio.
Crea_note = chrea un file txt che contiene una nota fattaq dal utente.
login = autentica la persona che sta usando l'asistente vocale.

"""

recognizizer = sr.Recognizer()
speker = tts.init()
speker.setProperty('rate',150)

mapping = {#mapping delle funzioni del assistente
    "saluto":prova_funzioni.saluto,
    "CMD":prova_funzioni.CMD,
    "tempo":prova_funzioni.tempo,
    "chi_sei":prova_funzioni.chi_sei,
    "leggi_pdf":prova_funzioni.leggi_pdf,
    "crea_nota":prova_funzioni.crea_note,
    "exit":prova_funzioni.exit
}


asistent = GenericAssistant('intents.json',intent_methods=mapping)
asistent.train_model()

if prova_funzioni.login():#controllo login per accedere al assistente
    speker.say("Ben venuto creatore, cosa posso fare per te")
    speker.runAndWait()

    while True:

        try:

            with sr.Microphone() as source:

                recognizizer.adjust_for_ambient_noise(source)
                print("Parla ti sto ascoltando")

                audio = recognizizer.listen(source)

                print("Sto elaborando")

                text = recognizizer.recognize_google(audio,language="it-IT")
                text = text.lower()

                print(f"frase ==> {text}")

            asistent.request(text)

        except  speech_recognition.UnknownValueError:
            recognizizer = speech_recognition.Recognizer()