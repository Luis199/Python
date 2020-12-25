from datetime import datetime


def main():
    now = datetime.now()
    print(now.strftime("The current year is: %Y"))


    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale dat: %x"))
    print(now.strftime("Locale time: %X"))






if __name__ == "__main__":
    main()