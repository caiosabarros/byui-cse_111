def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse()
    print(f"reverse: {fruit_list}")
    fruit_list.append("orange")
    print(f"with orange appended: {fruit_list}")
    i = fruit_list.index("apple")
    fruit_list.insert(i-1,"cherry")
    print(f"with cherry inserted: {fruit_list}")
    fruit_list.remove("banana")
    print(f"with banana removed: {fruit_list}")
    fruit_list.pop()
    print(f"with last popped: {fruit_list}")
    fruit_list.sort()
    print(f"sorted: {fruit_list}")
    fruit_list.clear()
    print(f"cleared: {fruit_list}")
    
# Call main to start this program.
if __name__ == "__main__":
    main()
