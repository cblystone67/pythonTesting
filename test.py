from operator import itemgetter
import re


def word_frequencies(filename):
    d = {}
    with open(filename, 'r') as file:
        contents = file.read()

    # Convert to lowercase
    contents = contents.lower()

    # Replace hyphens (-) with spaces
    contents = re.sub(r'-', ' ', contents)

    # Insert spaces between words that are squished together (e.g., "readableno" -> "readable no")
    contents = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', contents)

    # Remove unwanted punctuation but keep apostrophes initially
    contents = re.sub(r'[^\w\s\']|[\d]', '', contents)

    # Remove apostrophes from words
    contents = re.sub(r"['']", '', contents)

    # Split into words
    words = contents.split()

    # Count frequencies
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    return d


def print_map_by_value(map):
    for k, v in sorted(map.items(), key=itemgetter(1), reverse=True):
        print("%6d %s" % (v, k))


def main():
    filename = "turing.txt"
    print("=" * 10, filename, "=" * 10)
    word_freq = word_frequencies(filename)
    print_map_by_value(word_freq)


if __name__ == "__main__":
    main()
