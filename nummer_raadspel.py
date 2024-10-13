import random

def nummer_raadspel():
    te_raden_getal = random.randint(1, 100)
    
    while True:
        try:
            aantal_pogingen = int(input("Hoeveel keer wil je raden? (max 10): "))
            if aantal_pogingen > 10 or aantal_pogingen <= 0:
                print("Voer een getal tussen 1 en 10 in.")
            else:
                break
        except ValueError:
            print("Voer een geldig getal in.")
    
    print(f"Je hebt {aantal_pogingen} pogingen om het getal te raden!")
    
    for poging in range(1, aantal_pogingen + 1):
        while True:
            try:
                gok = int(input(f"Poging {poging}: Raad een getal tussen 1 en 100: "))
                if gok < 1 or gok > 100:
                    print("Voer een getal tussen 1 en 100 in.")
                else:
                    break  # Als het een geldig getal is, verlaat de loop
            except ValueError:
                print("Voer een geldig getal in.")
        
        if gok < te_raden_getal:
            print("Hoger!")
        elif gok > te_raden_getal:
            print("Lager!")
        else:
            print(f"Gefeliciteerd! Je hebt het juiste getal geraden in {poging} pogingen.")
            break
    else:
        print(f"Helaas, je hebt het niet geraden. Het juiste getal was {te_raden_getal}.")

if __name__ == "__main__":
    nummer_raadspel()