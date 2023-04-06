import string
import sys
from collections import deque


def is_valid_neighbor(current_word, neighbor_word, dictionary, visited):
    return neighbor_word in dictionary and neighbor_word not in visited and neighbor_word != current_word


try:
    with open("dictionary.txt", "r") as f:
        dictionary = [word.strip() for word in f.readlines()]
except FileNotFoundError:
    print("Файл зі словником не знайдений")
    sys.exit()
except IOError:
    print("Помилка відкриття файлу зі словником")
    sys.exit()

print(dictionary)

while True:
    start_word = input("Введіть початкове слово: ")
    end_word = input("Введіть кінцеве слово: ")
    # перевірка щодо однакової довжини
    if len(start_word) != len(end_word):
        print("Початкове і кінцеве слова мають різну довжину")
    else:
        break

visited = set()

if not all(word in dictionary for word in (start_word, end_word)):
    print("Start or end word not found in dictionary.")
else:
    visited = {start_word}

queue = deque()
queue.append(start_word)

paths = {}
paths[start_word] = [start_word]

# алгоритм пошуку в ширину
while queue:
    # Взяти перший елемент черги
    current_word = queue.popleft()

    for i in range(len(current_word)):
        for letter in string.ascii_lowercase:
            if letter != current_word[i]:
                neighbor_word = current_word[:i] + letter + current_word[i + 1:]
                if is_valid_neighbor(current_word, neighbor_word, dictionary, visited):
                    visited.add(neighbor_word)
                    queue.append(neighbor_word)
                    paths[neighbor_word] = paths[current_word] + [neighbor_word]
                    if neighbor_word == end_word:
                        queue.clear()
                        break

if end_word not in paths:
    print("Неможливо знайти шлях:")
else:
    print("Найкоротший шлях:")
    for word in paths[end_word]:
        print(word)
