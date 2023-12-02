

def main():
    # get file from user and word
    filename = input("what's the filename?")
    word = input("What's the word?")
    filename = filename.strip()  # get rid of errors

    # read file &&  get word count for each word
    lines = read_file_into_lines(filename)

    answer = find_word_counter(lines, word)
    # show the answer
    print(f"{answer}")
    # show more than required (like a plot that shows the distributionof the different words or the percentage of that word amid all the words frequencies.


# ----------- INIT Helper functions
def split_lines_into_line(lines):
    return lines.split("\n")


def split_line_into_words(line):
    return line.split(" ")


def make_words_case_insentitive(words):
    for k, word in enumerate(words):
        words[k] = word.lower()
    return words
# ----------- END Helper functions


def read_file_into_lines(filename, ):
    f = open(filename, "r")
    lines = f.read()
    return lines


def find_word_counter(lines, word):
    insentitive_word = str(word.lower())
    lines = split_lines_into_line(lines)
    counter = 0
    for line in lines:
        words = split_line_into_words(line)
        words_insentitive = make_words_case_insentitive(words)
        if insentitive_word in words_insentitive:
            counter += 1
    return counter


# Call main to start this program.
if __name__ == "__main__":
    main()
