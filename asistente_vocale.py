from neuralintents import GenericAssistant
import speech_recognition
import sys
import pyttsx3 as tts
import subprocess
import webbrowser
import prova_funzioni

prova_funzioni.login()
#tutte le librerie funzionano
#Assistente vocale versione 0.0.1
#creazzione_note(nel file json) va associata alla funziuone crea note nel file pytohn e cosi via
#versione 0.1.1
recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)

todo_list = ["Vai a fare shopping", "Pulisci la stanza", "Registra un video"]

def crea_note():
    global recognizer

    speaker.say("Cosa vuoi scrivere nella tua nota ?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("Dai un nome al file")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say(f"File creato con sucesso !!!{filename}") 
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Mi dispiace ma non o capito, prova di nuovo")
            speaker.runAndWait()


def CMD():#apre un cmd  che posso usare
    pass


def uscita():
    speaker.say("A rivederci creatore")
    speaker.runAndWait()
    sys.exit(0)



#in futuro funzione per il web broser (apre una schermata di google)    
def internet():
    pass
    



assistent = GenericAssistant('intents.json')
assistent.train_model()

