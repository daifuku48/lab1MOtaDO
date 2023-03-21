import string
import sys
from collections import deque
# Зчитати словник з файлу та зберегти його у списку

try:
    with open("dictionary.txt", "r") as f:
        # strip видаляє пробіли в кінці та початку, аналог trim()
        dictionary = [word.strip() for word in f.readlines()]
except FileNotFoundError:
    print("Файл зі словником не знайдений")
    sys.exit()
except IOError:
    print("Помилка відкриття файлу зі словником")
    sys.exit()
####
#виведемо слова з файлу
print(dictionary)

while True:
    start_word = input("Введіть початкове слово: ")
    end_word = input("Введіть кінцеве слово: ")
    # перевірка щодо однакової довжини
    if len(start_word) != len(end_word):
        print("Початкове і кінцеве слова мають різну довжину")
    else:
        break

visited = {}

if start_word not in dictionary or end_word not in dictionary:
    print("Початкове або кінцеве слово не знайдено у словнику.")
else:
    # Створюємо словник-множину та додамо до нього початкове слово
    visited = set()
    visited.add(start_word)

# Створити чергу(лист) та додамо до неї початкове слово
queue = deque()
queue.append(start_word)

# Створити словник-список для збереження шляхів до кожної вершини
paths = {}
paths[start_word] = [start_word]

# Почати цикл, доки черга не стане порожньою
while queue:
    # Взяти перший елемент черги
    current_word = queue.popleft()

    # Для кожного сусіднього слова, яке відрізняється від поточного слова на одну літеру та належить до словника,
    # перевірити, чи воно ще не було додане до словника-множини та словник-списку
    for i in range(len(current_word)):
        for letter in string.ascii_lowercase:
            if letter != current_word[i]:
                neighbor_word = current_word[:i] + letter + current_word[i+1:]
                if neighbor_word in dictionary and neighbor_word not in visited:
                    # Якщо слово ще не було додане, додати його до словника-множини, додати його до черги
                    # та зберегти шлях до нього у словник-списку
                    visited.add(neighbor_word)
                    queue.append(neighbor_word)
                    paths[neighbor_word] = paths[current_word] + [neighbor_word]

                    # Якщо поточне слово дорівнює кінцевому слову, то знайдено найкоротший шлях. Зупинити цикл.
                    if neighbor_word == end_word:
                        queue.clear()
                        break

# Якщо шлях не був знайдений, вивести відповідне повідомлення.
if end_word not in paths:
    print("Неможливо знайти шлях:")
    # В іншому випадку вивести знайдений шлях
else:
    print("Найкоротший шлях:")
    for word in paths[end_word]:
        print(word)