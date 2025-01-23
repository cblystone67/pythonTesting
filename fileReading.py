from operator import itemgetter
import re


def readFile(filename):
    d = {}
    with open(filename, 'r') as f:
        contents = f.read()
    # Convert to lowercase
    contents = contents.lower()

    # Replace hyphens (-) with spaces
    contents = re.sub(r"['\"!.,;?(){}\[\]]", "", re.sub(r"(\d)", "", re.sub(
        r"(?<=\w)'(?=\w)", "", re.sub(r"-", " ", contents))))

    # Split into words
    words = contents.split()

    # Count frequencies
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    print(d)


def main():
    filename = "testing.txt"
    print(readFile(filename))


if __name__ == "__main__":
    main()
