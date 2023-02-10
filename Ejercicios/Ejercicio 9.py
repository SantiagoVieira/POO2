if __name__ == "__main__":
    import random
    def generate_matrix(n):
        matrix = []
        for i in range(n):
            x = []
            for j in range(n):
                x.append(random.randint(0, 100))
            matrix.append(x)
        return matrix
    def print_matrix(matrix):
        for x in matrix:
            print(x)
    n = 4
    matrix = generate_matrix(n)
    print_matrix(matrix)