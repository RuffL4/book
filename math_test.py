import random

def main():
    zahl1 = random.randint(100, 1000)
    zahl2 = random.randint(100, 1000)
    summe = zahl1 + zahl2
    answer = int(input(f"Was ist die Losung zu {zahl1} + {zahl2}? "))
    if answer == summe:
        print("Nice!")
    else:
        print(f"Falsch. Ergebnis: {summe}")


if __name__ == "__main__":
    main()