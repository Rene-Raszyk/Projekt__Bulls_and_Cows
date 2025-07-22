# Bulls & Cows

Druhý projekt do Engeto Online Python Akademie  
Autor: Rene Raszyk 
Email: 2004reno2004@gmail.com

## Popis

Tento program simuluje známou logickou hru "Bulls and Cows".  
Cílem hry je uhodnout tajné čtyřmístné číslo, kde se žádná číslice neopakuje a číslo nezačíná nulou. Po každém tipu hráče program vypíše, kolik "bulls" (správná číslice na správném místě) a "cows" (správná číslice na špatném místě) tip obsahuje.
Program také ukládá tvoje statistiky do textového souboru (stats.txt).

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
def making_random_number ():
    number = sample(range(10), 4)
    while number[0] == 0:
        number = sample(range(10), 4)

    return "".join(map(str, number))
```
**Popis:**

***Pravidla pro generované číslo***
- Musí mít 4 číslice
- Nesmí začínat nulou
- Číslo musí být unikátní (každá číslice v číslu se musí lišit)

***Fungování funkce***
1. Pomocí "sample(range(10), 4)" se náhodně vyberou 4 různé číslice (od 0 do 9).

2. Pokud první číslice je nula, číslo se zahodí a losuje se znovu "(while number[0] == 0:)".

3. Po splnění podmínek se číslice převedou na řetězec pomocí "map(str, number)" a spojí se dohromady pomocí " "".join(...) ".

4. Výsledkem je řetězec s unikátním 4 ciferným číslem, které nezačíná nulou.

---

### Kontrola vstupu od hráče

```python
def checking_player_number(number: str):
    def duplicity_check(duplicid_number:list):
        j = 0
        while j != 3:
            if duplicid_number[j] in duplicid_number[j+1:]:
                return True
            j+=1
        return False
    while (not number.isnumeric()) or (len(number) != 4) or (int(number) < 1000) or (duplicity_check(number)):
        print("Wrong number. Try again")
        number = input(">>> ")
    return number
```
**Popis:**

***Pravidla pro vstup:***
- Musí se jednat o přesné 4 místné číslo
- Nesmí obsahovat písmena ani zanky
- Nesmí začínat nulou
- Číslo musí být unikátní 

***Fungování funkce***
1. Vnořená funkce "duplicity_check(duplicid_number)"
- Projde všechny číslice a ověřuje, zda se některá neopakuje.
- Pokud najde duplicitu, vrací True, jinak False.
- Funguje i se stringem, protože ten lze iterovat jako seznam znaků.

2. Hlavní smyčka while
- Funkce stále opakuje výzvu k zadání, dokud vstup:
    - neobsahuje pouze čísla (not number.isnumeric())
    - nemá přesně 4 znaky (len(number) != 4)
    - nezačíná nulou (int(number) < 1000)
    - nemá opakující se číslice (duplicity_check(number))
- Pokud některá z těchto podmínek není splněna, zobrazí se hláška "Wrong number. Try again" a funkce čeká na nový vstup.

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
def checking_the_correctness_of_the_number(number: list, pc_number: list):
    cows = 0
    bull = 0

    for i in range(0,4):
        if number[i] == pc_number[i]:
            bull +=1
        elif number[i] in pc_number:
            cows += 1

    return bull, cows
```
**Popis:**  
Funkce porovnává hráčovo číslo s tajným číslem a vrací počet bulls (správná číslice na správné pozici) a počet cows (správná číslice na špatné pozici).

***Fungování funkce***
1. Vstupní parametry "number:list, pc_number:list"
- První parametr je hráčské číslo, které převádím do typu list.
- Druhý parametr je vegenerované číslo, které je taktéž převedeno do typu list, aby se následně lépe porovnávaly číslice.

2. Inicializace počítadel "cows, bull"
- "cows" počítá počet správných číslic, ale na špatném místě.
- "bull" počítá počet správných číslic na správném místě.

3. Hlavní cyklus
- Smyčka prochází každou číslici na indexech 0 až 3. "for i in range(0, 4):"
- Pokud se číslice i-tého indexu v obou číslech shodují → bull. " if number[i] == pc_number[i]:"
- Pokud je číslice obsažena v tajném čísle, ale na jiném místě → cow. "elif number[i] in pc_number:"

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

