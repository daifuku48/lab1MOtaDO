from collections import Counter
from functools import reduce

def get_most_common_char_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().split()
            even_words = content[1::2]
            most_common_word = reduce(lambda x, y: Counter(x) + Counter(y), even_words).most_common(1)
            return most_common_word[0][0] if most_common_word else None
    except FileNotFoundError:
        print("File not found. Please check if the file name and path are correct.")


def main():
    res = get_most_common_char_from_file("text.txt")
    print(res)


if __name__ == "__main__":
    main()