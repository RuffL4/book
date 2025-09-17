def main():
    stars(8)
    #alt_stars(8)


def stars(number):
    umkehr = False
    for i in range(number*2):
        if i == number and umkehr == False:
            umkehr = True
            continue
        if umkehr == True:
            for j in range(i - number + 1):
                print("*", end="")
        else:
            for j in range(number - i):
                print("*", end="")
        print()


def alt_stars(number):
    for i in range(number*2-1):
        for j in range(1 + abs(i - (number - 1))):
            print("*", end ="")
        print()


if __name__ == "__main__":
    main()