if __name__ == "__main__":
    def number_major_minor(numbers):
        major = numbers[0]
        minor = numbers[0]
        for i in numbers:
            if i > major:
                major = i
            if i < minor:
                minor = i
        return major, minor

    lista = [0,1,2,3,4,5]
    major, minor = number_major_minor(lista)

    print("the largest number is:",major)
    print("the short number is: ",minor)
