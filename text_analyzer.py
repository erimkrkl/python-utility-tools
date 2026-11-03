
from collections import Counter


def analyze_text(text):
    words = text.split()
    characters = len(text)
    characters_without_spaces = len(text.replace(" ", ""))
    word_count = len(words)




    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)

    sentences = text.count(".") + text.count("!") + text.count("?")

    print("\n--- TEXT ANALYSIS ---")
    print(f"Character count: {characters}")
    print(f"Characters without spaces: {characters_without_spaces}")
    print(f"Word count: {word_count}")
    print(f"Sentence count: {sentences}")




    print(f"Longest word: {longest_word}")
    print(f"Shortest word: {shortest_word}")

    word_frequencies = Counter(
        word.lower().strip(".,!?;:") for word in words
    )

    print("\n--- MOST USED WORDS ---")
    for word, count in word_frequencies.most_common(5):
        print(f"{word}: {count}")


user_text = input("Enter a text to analyze: ")

if user_text.strip():
    analyze_text(user_text)
else:
    print("Please enter some text!")