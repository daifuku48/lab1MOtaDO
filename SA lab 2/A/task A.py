def read_2d_array(path):
    try:
        with open(path) as file:
            lines = file.readlines()
            array = []
            for line in lines:
                array.append([float(x) for x in line.strip().split(' ')])
            return array
    except IOError:
        print("Error: File not found or could not be read.")
        return None, None


def is_mutually_prime_numbers(path):
    return calculate_is_mutually_prime(diagonal_main_sum(read_2d_array(path)), diagonal_sec_sum(read_2d_array(path)))


def calculate_is_mutually_prime(first_number, second_number):
    if second_number == 0:
        return first_number == 1
    else:
        return calculate_is_mutually_prime(second_number, first_number % second_number)


def diagonal_main_sum(matrix, index=0, total=0):
    if index >= len(matrix):
        return total
    return diagonal_main_sum(matrix, index + 1, sum_2_numbers(total, matrix[index][index]))


def diagonal_sec_sum(matrix, index=0, total=0):
    if index >= len(matrix):
        return total
    return diagonal_sec_sum(matrix, index + 1, sum_2_numbers(total,  matrix[index][len(matrix) - 1 - index]))


def sum_2_numbers(first_number, second_number):
    return first_number + second_number


def main():
    print(is_mutually_prime_numbers("2DArray.txt"))


if __name__ == "__main__":
    main()
