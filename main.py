# jww 1-5-25
# main.py - bookbot - test project

def word_count(file_contents):
    count = 0
    for word in (file_contents.split()):
        count += 1
    return count

def letter_count(file_contents):
    count = 0
    for c in file_contents.lower()[0::]:
        count += 1
    return count

def letter_occurences(file_contents):
    letters = {}
    for c in file_contents.lower()[0::]:
        if c in "abcdefghijklmnopqrstuvwxyz":
            if c not in letters:
                letters[c] = 1
            else:
                letters[c] += 1
    return letters

def create_report(file_contents):
    report = ""
    report += "--- Begin report of books/frankenstein.txt ---\n"

    words = word_count(file_contents)
    report += f"{words} words found in the document\n\n"

    letters = letter_occurences(file_contents)

    sorted_dict = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))
    for k in sorted_dict:
        report += f"The '{k}' character was fount {sorted_dict[k]} times\n"

    report += "--- Begin report of books/frankenstein.txt ---\n"

    return report

book_path = "/home/joel/workspace/github.com/joelwheeler/bookbot/books/frankenstein.txt"
with open(book_path) as f:
    file_contents = f.read()

print(create_report(file_contents))
