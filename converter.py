def main():
    distance = float(input("Wie viel km: "))
    miles = convert_to_miles(distance)
    print(f"{distance:.2f} km sind {miles:.2f} Meilen")


def convert_to_miles(km):
    return km * 0.6214


if __name__ == "__main__":
    main()