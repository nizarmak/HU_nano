import nummer_raadspel
import galgje

def toon_menu():
    print("\nWelkom bij de Nano App Store!")
    print("1. Speel Nummer Raadspel")
    print("2. Speel Galgje")
    print("3. Afsluiten")

def main():
    while True:
        toon_menu()
        keuze = input("Maak een keuze (1-3): ")

        if keuze == '1':
            print("\nNummer Raadspel")
            nummer_raadspel.nummer_raadspel()
        elif keuze == '2':
            print("\nGalgje")
            galgje.speel_galgje()
        elif keuze == '3':
            print("Bedankt voor het spelen! Tot ziens!")
            break 
        else:
            print("Ongeldige keuze. Kies 1, 2 of 3.")

if __name__ == "__main__":
    main()
