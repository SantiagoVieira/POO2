if __name__ == "__main__":
    def sum_of_numbers(numbers):
        result = 0
        for i in numbers:
            result +=i
        return result
    lista = [0,1,2,3,7,8,9,11,21]
    print(f"the sum pf the numbers in the list is: ",sum_of_numbers(lista))