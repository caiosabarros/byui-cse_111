import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        
        products = {}
        for row_list in reader:
            name = row_list[key_column_index]
            products[name] = row_list

       # print("All Products")
       # print(f"{products}")
        return products

def main():
    store_name = input("What's the store's name?")

    print(f"{store_name}")

    products_dict = read_dictionary("products.csv", 0)
    
    # below is unneeded for w10
    # print(f"{products_dict}")

    try:
        with open("request.csv", "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            print("")
            print("Requested Items")
            number = 0
            price = 0
            print(f"reader: {reader}")
            for row_list in reader:
                print(f"{row_list}")
                prod = row_list[0]
                item = products_dict[prod]
                number += 1
                price += float(row_list[1]) * float(item[2])
                print(f"{item[1]}: {row_list[1]} @ {item[2]}")
            
            tax = price * .06
            print(f"Number of Items: {number}")
            print(f"Subtotal: {price}")
            print(f"Sales Tax: {tax}")
            print(f"Total: {price + tax}")
            print(f"Thank you for shopping at the {store_name}")
            print(f"{datetime.now():%A %I:%M %p}")
    except FileNotFoundError as err:
        print(type(err).__name__, err, sep=":")
    except KeyError as err:
        print(f"Error: unknown product ID in the request.csv file {err}")

    print(f"How was your experience shopping at {store_name} today? Would you like to participe on an online survey so that we can improve our customer service? \U0001f600")

if __name__ == "__main__":
    main()
