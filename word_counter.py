

def main():
    # get file from user and word
    filename = input("what's the filename?")
    word = input("What's the word?")
    filename = filename.strip() # get rid of errors

    # read file &&  get word count for each word
    read_file(filename, word)

    # show the answer

    # show more than required (like a plot that shows the distributionof the different words or the percentage of that word amid all the words frequencies.


def read_file(filename, word):
    f = open(filename, "r")
    lines = f.read()
    print(type(lines))
    #words = [i.split("\n") for i in lines]
    #words = lines.split(" ")
    print(f"{words}")



# Call main to start this program.
if __name__ == "__main__":
    main()
