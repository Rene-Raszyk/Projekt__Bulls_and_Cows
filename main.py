from random import randint
#import math
from time import time


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


print("Hi there!\n" \
"-----------------------------------------------\n" \
"I've generated a random 4 digit number for you.\n" \
"Let's play a bulls and cows game.\n" \
"-----------------------------------------------\n" \
"Enter a number:\n" \
"-----------------------------------------------")

pocet_pokusu = 1
hadaci_cislo = tvoreni_nahodneho_cisla()


while pocet_pokusu < 11:
    cislo_hrace = kontrola_cisla_hrace(input(">>> "))
    if pocet_pokusu == 1:
        pocatecni_cas = time()
    
    bulls, cows = kontrola_sparvnosti_cisla(cislo_hrace, hadaci_cislo)
    if bulls == 4:
        break
    print(f"bulls: {bulls} | cows: {cows}")
    pocet_pokusu += 1
else:
    print("You loose")
    print("Run out of tries")
    exit()

print("Correct, you've guessed the right number")
koncovy_cas = time()
tvuj_cas = round(koncovy_cas - pocatecni_cas)
print(f"Your time is: {tvuj_cas} seconds")


# ++ pridat
# nejmene odhadu
# prumer odhadu
# nejelpsi cas
# prumer casovy