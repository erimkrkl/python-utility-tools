
from collections import Counter
import string
import re


def get_word_statistics(words):
    word_frequencies = Counter(
        word.lower().strip(string.punctuation)
        for word in words
        if word.strip(string.punctuation)
        and not word.strip(string.punctuation).isdigit()
    )

    return word_frequencies


def analyze_text(text):
    words = text.split()

    clean_words = [
        word.strip(string.punctuation)
        for word in words
        if word.strip(string.punctuation)
        and not word.strip(string.punctuation).isdigit()
    ]

    characters = len(text)
    characters_without_spaces = len(text.replace(" ", ""))
    word_count = len(clean_words)

    letters = sum(char.isalpha() for char in text)
    digits = sum(char.isdigit() for char in text)

    numbers = re.findall(r'\d+', text)
    number_count = len(numbers)

    punctuation_count = sum(
        char in string.punctuation for char in text
    )

    sentences = text.count(".") + text.count("!") + text.count("?")

    word_frequencies = get_word_statistics(words)
    unique_word_count = len(word_frequencies)

    if clean_words:
        longest_word = max(clean_words, key=len)
        shortest_word = min(clean_words, key=len)
        average_word_length = (
            sum(len(word) for word in clean_words) / len(clean_words)
        )
    else:
        longest_word = "N/A"
        shortest_word = "N/A"
        average_word_length = 0

    reading_time_seconds = (word_count / 200) * 60

    print("\n========== TEXT ANALYSIS V2 ==========")

    print(f"Character count: {characters}")
    print(f"Characters without spaces: {characters_without_spaces}")
    print(f"Letter count: {letters}")
    print(f"Digit count: {digits}")
    print(f"Number count: {number_count}")
    print(f"Numbers found: {numbers}")
    print(f"Punctuation count: {punctuation_count}")

    print(f"\nWord count: {word_count}")
    print(f"Unique word count: {unique_word_count}")
    print(f"Sentence count: {sentences}")

    print(f"\nLongest word: {longest_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Average word length: {average_word_length:.2f}")

    if reading_time_seconds < 60:
        print(f"\nEstimated reading time: {reading_time_seconds:.0f} seconds")
    else:
        minutes = int(reading_time_seconds // 60)
        seconds = int(reading_time_seconds % 60)
        print(f"\nEstimated reading time: {minutes} minutes {seconds} seconds")

    print("\n--- MOST USED WORDS ---")

    for word, count in word_frequencies.most_common(5):
        print(f"{word}: {count}")


while True:
    user_text = input("\nEnter a text to analyze: ")

    if user_text.strip():
        analyze_text(user_text)
    else:
        print("Please enter some text!")

    choice = input("\nDo you want to analyze another text? (y/n): ")

    if choice.lower() != "y":
        print("Thank you for using Text Analyzer!")
        break