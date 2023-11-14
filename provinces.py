
def main():
    new_list = []
    modify("provinces.txt", new_list)

def modify(filename, new_list):
    with open(filename, "rt") as file:
        for line in file:
            new_list.append(line)
        
        new_list.pop(0)
        new_list.pop()

        i = 0
        print(f"{new_list}")
        for line in new_list:
            if line == "AB\n":
                new_list[i] = "Alberta\n"
            i += 1

        y = 0
        for line in new_list:
            if line == "Alberta\n":
                y += 1
        
        print(f"Alberta occurs {y} times in the modified list.")
        



if __name__ == "__main__":
    main()
