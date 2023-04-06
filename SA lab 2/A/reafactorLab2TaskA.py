def read_2d_array(path):
    try:
        with open(path) as file:
            lines = file.readlines()
            array = [[float(num) for num in line.strip().split()] for _, line in enumerate(lines[1:])]
            return int(lines[0]), array
    except IOError:
        print("Error: File not found or could not be read.")
        return None, None


def is_mutually_prime(a, b):
    return a == 1 if b == 0 else is_mutually_prime(b, a % b)


def diagonal_main_sum(matrix, index=0, total=0):
    if index >= len(matrix):
        return total
    total += matrix[index][index]
    return diagonal_main_sum(matrix, index + 1, total)


def diagonal_sec_sum(matrix, index=0, total=0):
    if index >= len(matrix):
        return total
    total += matrix[index][len(matrix) - 1 - index]
    return diagonal_sec_sum(matrix, index + 1, total)


def main():
    count, array = read_2d_array("2DArray.txt")
    if count is None or array is None:
        return
    write_2d_array = lambda array: print(array)
    main_sum = diagonal_main_sum(array)
    sec_sum = diagonal_sec_sum(array)
    write_2d_array(array)
    print(main_sum, sec_sum)
    print(is_mutually_prime(main_sum, sec_sum))


if __name__ == "__main__":
    main()