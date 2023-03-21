from functools import reduce
from collections import Counter


def get_most_common_words_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
    even_words = filter(lambda i: i % 2 == 1, range(len(words)))
    filtered_words = list(map(lambda i: words[i], even_words))
    print(filtered_words)
    most_common_letter = reduce(lambda x, y: Counter(x) + Counter(y), filtered_words).most_common(1)
    return most_common_letter


def main():
    res = get_most_common_words_from_file("text.txt")
    print(res)


if __name__ == "__main__":
    main()
