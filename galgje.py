import random
import json

def laad_woorden_bestand():
    with open("woorden.json", "r") as bestand:
        data = json.load(bestand)
    return data['woorden']

def willekeurig_woord(woorden):
    return random.choice(woorden)

def speel_galgje():
    woorden = laad_woorden_bestand()
    te_raden_woord = willekeurig_woord(woorden).lower()
    
    naam = input("Wat is je naam? ")
    
    while True:
        try:
            pogingen = int(input("Hoeveel keer wil je raden? (max 10): "))
            if pogingen > 10 or pogingen <= 0:
                print("Voer een getal tussen 1 en 10 in.")
            else:
                break
        except ValueError:
            print("Voer een getal in.")
    
    geraden_letters = []
    fouten = 0
    
    while fouten < pogingen and set(te_raden_woord) != set(geraden_letters):
        print(f"Je hebt {pogingen - fouten} pogingen over.")
        
        woord_status = [letter if letter in geraden_letters else '_' for letter in te_raden_woord]
        print("Woord: ", ' '.join(woord_status))
        
        gok = input("Raad een letter: ").lower()
        while len(gok) != 1 or not gok.isalpha():
            print("Voer precies één letter in.")
            gok = input("Raad een letter: ").lower()
        
        if gok in geraden_letters:
            print("Je hebt deze letter al geraden.")
        elif gok in te_raden_woord:
            print("Goed geraden!")
            geraden_letters.append(gok)
        else:
            print("Fout! Deze letter zit niet in het woord.")
            fouten += 1
    
    if set(te_raden_woord) == set(geraden_letters):
        print(f"Gefeliciteerd {naam}, je hebt het woord geraden: {te_raden_woord}!")
    else:
        print(f"Helaas {naam}, je hebt geen pogingen meer. Het juiste woord was: {te_raden_woord}.")

if __name__ == "__main__":
    speel_galgje()