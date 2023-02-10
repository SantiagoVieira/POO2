if __name__ == "__main__":
    def temperature():
        temper = int(input("enter temperature in fahrenheit:  "))
        convert = (temper - 32) * 5/9

        return convert

    print("the temperature in degrees celcius is.",temperature())