from collections import Counter
from functools import reduce

def get_most_common_char_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read().split()
        chars = content[1::2]
        most_common_char = reduce(lambda x, y: Counter(x) + Counter(y), chars).most_common(1)
        return most_common_char[0][0] if most_common_char else None


def main():
    res = get_most_common_char_from_file("text.txt")
    print(res)


if __name__ == "__main__":
    main()