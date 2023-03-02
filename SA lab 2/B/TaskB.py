from functools import reduce


def get_most_common_words_from_file(file_path):
    try:
        with open(file_path) as f:
            words = f.read().strip().split()
            second_words = words[1::2]
            print(second_words)
            letters = ''.join(set(''.join(second_words)))
            letter_counts = list(
                map(lambda letter: (letter, sum(map(lambda word: word.count(letter), words))), letters))
            print(letter_counts)
            most_frequent_letter = reduce(lambda a, b: max(a, b, key=lambda x: x[1]), letter_counts)
            print(
                f"The most frequent letter is '{most_frequent_letter[0]}' with {most_frequent_letter[1]} occurrences.")
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except:
        print("An error occurred while processing the file.")


def main():
    get_most_common_words_from_file("text.txt")


if __name__ == "__main__":
    main()
