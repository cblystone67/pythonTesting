from operator import itemgetter
import re


def readFile(filename):
    d = {}
    with open(filename, 'r') as f:
        contents = f.read()
    # Convert to lowercase
    contents = contents.lower()

    # Replace hyphens (-) with spaces
    # Ensure Unicode dashes like \u2014 are replaced correctly
    # Decode Unicode characters
    contents = contents.encode('utf-8').decode('unicode_escape')
    contents = re.sub(r"['\"!.,;?(){}\[\]]", "", re.sub(r"(\d)", "", re.sub(
        r"(?<=\w)'(?=\w)", "", re.sub(r"[-\u2014]", " ", contents))))

    contents = re.sub(r"['\"!.,;?(){}\[\]]", "", re.sub(r"(\d)", "", re.sub(
        r"(?<=\w)'(?=\w)", "", re.sub(r"[-\u2014]", " ", contents))))

    # Split into words
    words = contents.split()

    # Count frequencies
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    # Sort by frequency in descending order.
    sorted_words = sorted(d.items(), key=itemgetter(1), reverse=True)

    # Print each word with its frequency.
    for word, freq in sorted_words:
        print(f"{freq} {word}")


def main():
    filename = "testing.txt"
    readFile(filename)


if __name__ == "__main__":
    main()
