if __name__ == "__main__":

    print("hi! eneter 2 numbers to do basic operations")

    number_1 = eval(input("Enter number 1: "))
    number_2 = eval(input("Enter number 2: "))

def sum():
    operation_1 = number_1 + number_2

    return operation_1

def substraction():
    operation_2 = number_1 - number_2

    return operation_2

def multiplication():
    operation_3 = number_1 * number_2

    return operation_3

def division():
    operation_4 = number_1 / number_2

    return operation_4


print("the result of the sum is: ",sum())
print("the result of the substraction is: ",substraction())
print("the result of the multiplication is: ",multiplication())
print("the result of the division is: ",division())