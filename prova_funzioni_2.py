import webbrowser
import random

"""
Prova delle funzioni da aggiungere al assistente in futuro con il debag
per ora non è stato fatto
"""


long = input("quanto deve essere lunga la password ?")

def password(long): #genera la passworde in maniera casuale
    cont = 0
    max = 127
    min = 65
    paswor = []
    while(cont<int(long)):
        n2 = random.randint(min,max)
        n1 = chr(n2)
        paswor.append(n1)
        cont = cont + 1
    print(paswor)



def login():
    file = opne("database.txt","w")





lib = input("Cosa vuoi cercare nel web ?")

def cercaBrowser(lib): #cerca qualcosa nel web in caso di non corisposta nelle funzioni(funzionantre)
    url = "https://www.google.co.in/search?q=" +(str(lib))+ "&oq="+(str(lib))+\
      "&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
    webbrowser.open_new(url)

if __name__ == "__main__":
    password(long)
    cercaBrowser(lib)
