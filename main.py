from random import randint
from time import time
import os
import re

def tvoreni_nahodneho_cisla ():
    cislo = []
    cislo.append(randint(1,9))
    nove = randint(0,9)

    while len(cislo) != 4:
        while nove in cislo:
            nove = randint(0,9)
        else:
            cislo.append(nove)

    return "".join(map(str, cislo))
    
def kontrola_cisla_hrace(cislo):
    def kontrola_duplicity(cislod:list):
        j = 0
        while j != 3:
            if cislod[j] in cislod[j+1:]:
                return True
            j+=1
        return False
    while (not cislo.isnumeric()) or (len(cislo) != 4) or (int(cislo) < 1000) or (kontrola_duplicity(cislo)):
        print("Wrong number. Try again")
        cislo = input(">>> ")
    return cislo

def kontrola_sparvnosti_cisla(cislo:list, pc_cislo:list):
    cows = 0
    bull = 0

    for i in range(0,4):
        if cislo[i] == pc_cislo[i]:
            bull +=1
        elif cislo[i] in pc_cislo:
            cows += 1

    return bull, cows

def zapis_cteni_soubor(cas, pokusy):
    cislo_hodnot = []
    if os.path.exists("stats.txt"):
        txt_soubor = open("stats.txt", "r+")
        obsah_txt = txt_soubor.read()
        oddeleny_text = re.split(r"[ \n]", obsah_txt)
        for i in range(len(oddeleny_text)):
            if oddeleny_text[i].isnumeric():
                cislo_hodnot.append(oddeleny_text[i])

        pocet_her = int(cislo_hodnot[0])
        prum_cas = float(cislo_hodnot[1])
        nej_cas = int(cislo_hodnot[2])
        prum_pokus = float(cislo_hodnot[3])
        nej_pokus = int(cislo_hodnot[4])

        pocet_her += 1
        prum_cas = round(((pocet_her - 1) * prum_cas + cas) / pocet_her)
        if nej_cas > cas:
            nej_cas = cas
        prum_pokus = round(((pocet_her - 1) * prum_pokus + pokusy) / pocet_her)
        if nej_pokus > pokusy:
            nej_pokus = pokusy

        txt_soubor.seek(0)
        txt_soubor.write(f"Number of games: {pocet_her}\n")
        txt_soubor.write(f"Average time in seconds: {prum_cas}\n")
        txt_soubor.write(f"Best time in seconds: {nej_cas}\n")
        txt_soubor.write(f"Average number of attempts: {prum_pokus}\n")
        txt_soubor.write(f"Least attempts: {nej_pokus}")
        txt_soubor.truncate()

        cislo = [pocet_her, prum_cas, nej_cas, prum_pokus, nej_pokus]

    else: 
        #vytvaření souboru + první zápis
        pocet_her = 1
        prumerny_cas = cas
        nejelpsi_cas = cas
        prumer_pokusu = pokusy
        nejmene_pokusu = pokusy
        cislo = [1, cas, cas, pokusy, pokusy]

        txt_soubor = open("stats.txt", "w")
        txt_soubor.write(f"Number of games: {pocet_her}\n")
        txt_soubor.write(f"Average time in seconds: {prumerny_cas}\n")
        txt_soubor.write(f"Best time in seconds: {nejelpsi_cas}\n")
        txt_soubor.write(f"Average number of attempts: {prumer_pokusu}\n")
        txt_soubor.write(f"Least attempts: {nejmene_pokusu}")

    return cislo

print("Hi there!\n" \
"-----------------------------------------------\n" \
"I've generated a random 4 digit number for you.\n" \
"Let's play a bulls and cows game.\n" \
"-----------------------------------------------\n" \
"Enter a number:\n" \
"-----------------------------------------------")

pocet_pokusu = 1
hadaci_cislo = tvoreni_nahodneho_cisla()
print(hadaci_cislo)
while pocet_pokusu < 30:
    cislo_hrace = kontrola_cisla_hrace(input(">>> "))
    if pocet_pokusu == 1:
        pocatecni_cas = time()
    
    bulls, cows = kontrola_sparvnosti_cisla(cislo_hrace, hadaci_cislo)
    if bulls == 4:
        break
    print(f"bulls: {bulls} | cows: {cows}")
    print("-----------------------------------------------")
    pocet_pokusu += 1
else:
    print("You loose")
    print("Run out of tries")
    exit()

print("Correct, you've guessed the right number")
print("-----------------------------------------------")
print("That's amazing!")
print("-----------------------------------------------")

koncovy_cas = time()
tvuj_cas = round(koncovy_cas - pocatecni_cas)
print(f"\nYour time is: {tvuj_cas} seconds")
print("-----------------------------------------------")
statistiky = zapis_cteni_soubor(tvuj_cas, pocet_pokusu)
print("Here are your stats:")
print(f"Number of games: {statistiky[0]}")
print(f"Average time in seconds: {statistiky[1]}")
print(f"Best time in seconds: {statistiky[2]}")
print(f"Average number of attempts: {statistiky[3]}")
print(f"Least attempts: {statistiky[4]}")

