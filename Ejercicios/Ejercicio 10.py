if __name__ == "__main__":
    def factorial(number):
        if number < 0:
            return None
        if number == 0:
            return 1
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result


    number = 5
    factorial_of_number = factorial(number)
    if factorial_of_number is None:
        print("the factorial is not defined for negative numbers ")
    else:
        print(f"the factorial of{number}, is {factorial_of_number}")

