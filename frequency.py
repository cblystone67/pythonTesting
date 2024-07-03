import string
import re


def count_word_frequencies(filename):
    """Return a dictionary of word frequencies from the given file."""
    word_freq = {}

    # open the file and read its contents
    with open(filename, 'r') as file:
        text = file.read()

        # Split text into words, ignoring punctuation and converting to lowercase
        text = text.replace('-', ' ')
        words = text.lower().split()
        table = str.maketrans('', '', string.punctuation)
        cleaned_words = [word.translate(table) for word in words]

        # Regular expression to match numbers
        non_numeric_pattern = re.compile(r'^[a-z]+$')

        # Count frequencies of each word using a dictionary
        for word in cleaned_words:
            # Check if the word is a number
            if non_numeric_pattern.match(word):
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1

    return word_freq


def print_sorted_word_frequencies(word_frequencies):
    """Print the word frequencies in sorted order."""
    sorted_word_frequencies = sorted(
        word_frequencies.items(), key=lambda item: item[1], reverse=True)
    for freq, word in sorted_word_frequencies:
        print(f'{freq} {word}')


filename = 'turing.txt'
word_frequencies = count_word_frequencies(filename)

# for word, freq in word_frequencies.items():
#     print(f'{freq} {word}')

print_sorted_word_frequencies(word_frequencies)
