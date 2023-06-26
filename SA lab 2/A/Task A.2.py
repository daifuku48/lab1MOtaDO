from math import gcd


def read_2d_array(path):
    try:
        with open(path, 'r') as f:
            return [list(map(int, line.split())) for line in f.readlines()]
    except IOError:
        return None


def calculate_mutually_prime_sum(path):
    return is_mutually_prime(diagonal_main_sum(read_2d_array(path)), diagonal_sec_sum(read_2d_array(path)))


def is_mutually_prime(first_number, second_number):
    return gcd(first_number, second_number) == 1


def diagonal_main_sum(matrix):
    return sum(map(lambda i: matrix[i][i], range(len(matrix))))


def diagonal_sec_sum(matrix):
    return sum(map(lambda i: matrix[i][len(matrix) - i - 1], range(len(matrix))))


def main():
    print(calculate_mutually_prime_sum("2DArray.txt"))


if __name__ == "__main__":
    main()