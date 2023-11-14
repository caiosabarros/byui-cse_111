import csv

def read_dictionary(filename, key_column_index = 0):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    students = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for line in reader:
            stud_key = line[key_column_index]
            students[stud_key] = line[1]

        return students

def main():
    stud = read_dictionary("students.csv")
    
    s = input("Please enter an I-Number (xxxxxxxxx): ")
    if s in stud:
        print(f"{stud[s]}")
    else:
        print("No such student")

if __name__ == "__main__":
    main()
