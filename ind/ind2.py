import sys

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    def find_duplicate_words(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            word_set = set()
            for line_num, line in enumerate(lines):
                words = line.strip().split()
                for word in words:
                    word = word.lower()
                    if word in word_set:
                        print(f"Повторяющееся слово найдено на строке {line_num + 1}: {word}")
                    else:
                        word_set.add(word)
        file.close()

    if len(sys.argv) < 2:
        print("Ошибка: не указан файл")
    else:
        filename = sys.argv[1]
        try:
            find_duplicate_words(filename)
        except FileNotFoundError:
            print(f"Ошибка: файл '{filename}'не найден")
