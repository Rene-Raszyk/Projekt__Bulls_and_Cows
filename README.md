# Bulls & Cows

Druhý projekt do Engeto Online Python Akademie  
Autor: Rene Raszyk 
Email: 2004reno2004@gmail.com

## Popis

Tento program simuluje známou logickou hru "Bulls and Cows".  
Cílem hry je uhodnout tajné čtyřmístné číslo, kde se žádná číslice neopakuje a číslo nezačíná nulou. Po každém tipu hráče program vypíše, kolik "bulls" (správná číslice na správném místě) a "cows" (správná číslice na špatném místě) tip obsahuje.

## Jak hrát

1. Spusť program příkazem:
    ```
    python main.py
    ```
2. Program ti vypíše úvodní text a vyzve tě k zadání čtyřmístného čísla.
3. Zadej svůj tip a stiskni Enter.
4. Program vyhodnotí tvůj tip a vypíše počet bulls a cows.
5. Pokračuj v tipování, dokud neuhodneš celé číslo.

## Pravidla

- Číslo je čtyřmístné, nezačíná nulou a všechny číslice jsou unikátní.
- Po každém tipu se dozvíš, kolik máš bulls a kolik cows.
- 1 bull = správná číslice na správném místě.
- 1 cow = správná číslice na špatném místě.

## Hlavní použité funkce

### Generování tajného čísla

```python
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
```
**Popis:**

***Pravidla pro generované číslo***
- Musí mít 4 číslice
- Nesmí začínat nulou
- Číslo musí být unikátní (každá číslice v číslu se musí lišit)

***Fungování funkce***
1. Vytvoření prázdného seznamu pro jednotlivé číslice "cislo[]"

2. Přidání první číslice "cislo.append(randint(1,9))"
- První číslice nesmí být nula, proto se losuje z čísel 1-9.

3. Generování následných číslic
- První cyklus while kontroluje zda je číslo 4 místné, pokud není smyčka pokračuje, pokud je cyklus se zastaví. "while len(cislo) != 4:"
- Následný while kontoluje zda nově vytvořené číslo, již je v seznamu, pokud není zapíše číslo do seznamu, pokud je cyklus pokračuje. "while nove in cislo:"
- Následně se vygeneruje náhodné číslo. "nove = randint(0,9)"
- Pokud číslo je unikátní přidá se do seznamu. "cislo.append(nove)"

4. Sloučení číslic do řetězce a následné vrácení hodnoty
- Pomocí "map(str, cislo)" převedeme každé číslo na řetězec
- Pomocí " "".join() " je spojí do jednoho čtyřciferného čísla ve formátu str.
- Následně vrací hodnotu pomocí "return"

---

### Kontrola vstupu od hráče

```python
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
```
**Popis:**

***Pravidla pro vstup:***
- Musí se jednat o přesné 4 místné číslo
- Nesmí obsahovat písmena ani zanky
- Nesmí začínat nulou
- Číslo musí být unikátní 

***Fungování funkce***
1. Fungování vnořené funkce
- Vnořená funkce "kontrola_duplicity" zjišťuje zda hráč zadal unikátní   číslo (vrací False) nebo ne (vrací True).
- Funguje správně i když je "cislod" string, protože string je iterovatelný jako seznam znaků.

2. Hlavní smyčka while
- Pokud hráč zadá špatný vstup (nečíslo, špatná délka, začínající 0, duplicita), vypíše se chybové hlášení a požádá se o nové číslo.
- Smyčka pokračuje, dokud není vstup správný.

3. Návratová hodnota
- Jakmile je vstup validní, funkce vrátí správné 4 místné číslo jako řetězec (string).

4. Příklady chování
Vstup hráče: "1224"
Má duplicity → znovu se zeptá.

Vstup hráče: "abc4"
Nečíselné znaky → znovu se zeptá.

Vstup hráče: "0123"
Začíná nulou → znovu se zeptá.

Vstup hráče: "1234"
V pořádku → funkce vrátí "1234"

---

### Vyhodnocení tipu (bulls & cows)

```python
def kontrola_sparvnosti_cisla(cislo:list, pc_cislo:list):
    cows = 0
    bull = 0
    for i in range(0,4):
        if cislo[i] == pc_cislo[i]:
            bull +=1
        elif cislo[i] in pc_cislo:
            cows += 1
    return bull, cows
```
**Popis:**  
Funkce spočítá, kolik číslic je správně na správné pozici (bulls) a kolik číslic je správně, ale na špatné pozici (cows).

***Fungování funkce***
1. Vstupní parametry "cislo:list, pc_cislo:list"
- První parametr je hráčské číslo, které převádím do typu list.
- Druhý parametr je vegenerované číslo, které je taktéž převedeno do typu list, aby se následně lépe porovnávaly číslice.

2. Inicializace počítadel "cows, bull"
- "cows" počítá počet správných číslic, ale na špatném místě.
- "bull" počítá počet správných číslic na správném místě.

3. Hlavní cyklus
- Smyčka prochází každou číslici na indexech 0 až 3. "for i in range(0, 4):"
- Pokud se číslice i-tého indexu v obou číslech shodují → bull. " if cislo[i] == pc_cislo[i]:"
- Pokud je číslice obsažena v tajném čísle, ale na jiném místě → cow. "elif cislo[i] in pc_cislo:"

4. Návrat hodnot
- Retur vrací dvojici hodnot: počet bull a počet cow. "return bull, cows"

---

Více najdeš přímo v kódu v souboru `main.py`.

---

## Požadavky

- Python 3
- Není potřeba instalovat žádné další knihovny.

---

## Autor

- **Jméno:** Rene Raszyk  
- **Email:** 2004reno2004@gmail.com 

