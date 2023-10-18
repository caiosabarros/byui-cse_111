print("This program is an implementation of the Rosenberg")
print("Self-Esteem Scale. This program will show you ten statements that you could possibly apply to yourself.")
print("Please rate how much you agree with each of the statements by responding with one of these four letters:")

print("D means you strongly disagree with the statement.")
print("d means you disagree with the statement.")
print("a means you agree with the statement.")
print("A means you strongly agree with the statement.")

def grades_asc(grade):
    if grade == "D":
        return 0
    if grade == "d":
        return 1
    if grade == "a":
        return 2
    if grade == "A":
        return 3
def grades_dec(grade):
    if grade == "D":
        return 3
    if grade == "d":
        return 2
    if grade == "a":
        return 1
    if grade == "A":
        return 0 

sum = 0
print("1. I feel that I am a person of worth, at least on an equal plane with others.")
first = input("     Enter D, d, a, or A:")
sum += grades_asc(first)
print("2. I feel that I have a number of good qualities.")
second = input("    Enter D, d, a, or A:")
print("3. All in all, I am inclined to feel that I am a failure.")
sum += grades_asc(second)
third = input("     Enter D, d, a, or A:")
print("4. I am able to do things as well as most other people.")
sum += grades_dec(third)
fourth = input("    Enter D, d, a, or A:")
print("5. I feel I do not have much to be proud of.")
sum += grades_asc(fourth)
fifth = input("     Enter D, d, a, or A:")
print("6. I take a positive attitude toward myself.")
sum += grades_dec(fifth)
sixth = input("     Enter D, d, a, or A:")
print("7. On the whole, I am satisfied with myself.")
sum += grades_asc(sixth)
seventh = input("   Enter D, d, a, or A:")
sum += grades_asc(seventh)
print("8. I wish I could have more respect for myself.")
eigth = input("     Enter D, d, a, or A:")
sum += grades_dec(eigth)
print("9. I certainly feel useless at times.")
ninth = input("     Enter D, d, a, or A:") 
sum += grades_dec(ninth)
print("10. At times I think I am no good at all.")
tenth = input("     Enter D, d, a, or A:")
sum += grades_dec(tenth)
print(f"Your score is {sum}.")
print("A score below 15 may indicate problematic low self-esteem.")