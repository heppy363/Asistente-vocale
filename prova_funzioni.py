import sys
import pyttsx3
import speech_recognition as sr
import subprocess
import pyttsx3 as tts
import time
import random
import PyPDF2


recognizizer = sr.Recognizer()
speker = tts.init()
speker.setProperty('rate',150)



#funzione per creare le note in maniera automatica
def crea_note():
    global recognizizer

    speker.say("Cosa vuoi scrivere nella tua nota ?")
    speker.runAndWait()

    done = False

    while not done:
        try:
            with sr.Microphone() as mic:
                recognizizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizizer.listen(mic)

                note = recognizizer.recognize_google(audio,language="it-IT")
                note = note.lower()

                speker.say("Dai un nome al file")
                speker.runAndWait()

                recognizizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizizer.listen(mic)

                filename = recognizizer.recognize_google(audio,language="it-IT")
                filename = filename.lower()

            with open(f"{filename}.txt", 'w') as f:
                f.write(note)
                done = True
                speker.say(f"File creato con sucesso !!!{filename}")
                speker.runAndWait()
        except Exception as e:
            print("c'è stato un errore",e)
            speker.say("ERRORE file non creato")
            speker.runAndWait()


#funzione per leggere i file pdf funzionante ma non completa voglio fare inserire il nome del file creato dal utente
def leggi_pdf():

    speker.say("Che PDF vuoi leggere, dimi il nome")
    speker.runAndWait()

    with sr.Microphone() as mic:
        recognizizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizizer.listen(mic)

        PDF = recognizizer.recognize_google(audio,language="it-IT")
        PDF = PDF.lower()

    with open(f"{PDF}.pdf", 'rb') as book:# Apre il PDF in modalità lettura.
        ful_text = ""

        read = PyPDF2.PdfFileReader(book)

        audio_read = pyttsx3.init()
        audio_read.setProperty("rate",100)

        for page in range(read.numPages):
            next_page = read.getPage(page)
            content = next_page.extractText()
            ful_text += content

        audio_read.save_to_file(ful_text,"prova.mp3") #@Salva il PDF COME "prova.mp3"
        audio_read.runAndWait()

        speker.say("PDF letto con sucesso file creato")
        speker.runAndWait()


def check_password(passwd): #metodo privato
    #controlla la presenza o meno della password
    check = False
    with open('database.txt') as temp_f:
        datafile = temp_f.readlines()
        for line in datafile:
            if passwd in line:
                check = True    #la parola è stata trova
        return check            #non è stata trovata


#funzione per l'autenticazione del utente valore buleano
def login():
    passwor = ""

    if check_password(passwor):
        #la password esiste non deve reinserirla, ma confermarla
        speker.say("Conferma la password")
        speker.runAndWait()

        with sr.Microphone() as mic: #prendo in imput la password la verificare
            recognizizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizizer.listen(mic)

            passwor = recognizizer.recognize_google(audio, language="it-IT")
            passwor = passwor.lower()

        return check_password(passwor)
    else:
        #la password non c'e deve inserirla

        speker.say("Ben venuto che password vuoi impostare")
        speker.runAndWait()

        with sr.Microphone() as mic:
            recognizizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizizer.listen(mic)

            passwor = recognizizer.recognize_google(audio,language="it-IT")
            passwor = passwor.lower()

        file = open("database.txt","w")
        file.write(passwor)#mettimo la password che seglie l'utente nel file
        file.close()

        return True

#funzione che risponde alla domanda come va
def saluto():
    saluti = ["Ciao stò bene","Tutto bene, grazzie","Mi sento un pò giù","Io sto bene te come stai"]
    speker.say(random.choice(saluti))
    speker.runAndWait()


#apre il CMD
def CMD():
    speker.say("Stò aprendo il CMD")
    speker.runAndWait()
    subprocess.call('start', shell=True)

#funzione che elenca a che versione è l'assistente vocale
def chi_sei():
    speker.say("Ciao Sono Emilia l'asistente personale di Heppy363 al momento sono nella versione 0.1.16")
    speker.runAndWait()


#dice che ore sono
def tempo():
    ora = time.strftime("%H")
    minuti = time.strftime("%M")
    speker.say("Sone le"+ora+"e"+minuti+"minuti")
    speker.runAndWait()


#termina il processo del assistente uscendo dal programma
def exit():
    speker.say("Ciao, arrivederci")
    speker.runAndWait()
    sys.exit(0)
