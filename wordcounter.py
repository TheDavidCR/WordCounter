#!/usr/bin/env python3

import sys

def count_word_occurrences(text, word):
    return text.lower().split().count(word.lower())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 wordcounter.py <word> [file]")
        sys.exit(1)

    word_to_count = sys.argv[1]

    if len(sys.argv) == 3:
        filename = sys.argv[2]
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            sys.exit(1)
    else:
        print("Enter text (Ctrl+D to finish):")
        text = sys.stdin.read()

    count = count_word_occurrences(text, word_to_count)
    print(f"The word '{word_to_count}' appears {count} times.")
