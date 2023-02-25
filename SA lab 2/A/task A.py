
def read_2d_array(path):
    count = -1
    with open(path) as file:
        lines = file.readlines()

        array = []
        for line in lines:
            if count == -1:
                count = int(line.strip())
                continue
            row = line.strip().split(' ')
            row = [float(x) for x in row]
            array.append(row)

        return count, array


def max_nod(first_number, second_number):
    if first_number == 0:
        return second_number
    elif second_number == 0:
        return first_number
    elif first_number == second_number:
        return first_number
    elif first_number > second_number:
        return max_nod(first_number - second_number, second_number)
    else:
        return max_nod(first_number, second_number - first_number)


def is_all_prime(first_number, second_number):
    if max_nod(round(first_number), round(second_number)) == 1:
        print("all numbers is prime")
    else:
        print("numbers is not prime")


def diagonal_sum(array, size):
    if size == 1:
        return array[0][0], array[0][0]  # the only element is both on the main and secondary diagonal

    sub_array = [row[1:] for row in array[1:]]  # sub-array without the first column
    sub_size = size - 1

    main_diagonal_sum, sec_diagonal_sum = diagonal_sum(sub_array, sub_size)

    main_diagonal_sum += array[0][0]  # add the top-left element to the main diagonal sum
    sec_diagonal_sum += array[0][-1]  # add the top-right element to the secondary diagonal sum

    return main_diagonal_sum, sec_diagonal_sum


def main():
    count, array = read_2d_array("2DArray.txt")
    write_2d_array = lambda array: print(array)
    main_sum, sec_sum = diagonal_sum(array, count)
    write_2d_array(array)
    is_all_prime(main_sum, sec_sum)


if __name__ == "__main__":
    main()