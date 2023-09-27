# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

subtotal = float(input("Please enter the subtotal: "))

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

# Print the day of the week for the user to see.

#0 Monday
#1 Tuesday
#2 Wednesday
#3 Thursday
#...

## Calculate the sales tax

# If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal. Your program must then compute the total amount due by adding sales tax of 6% to the subtotal.
new_total = subtotal
if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    new_total = subtotal * .9
    print(f"Discount amount: {(subtotal - new_total):.2f}")
taxes = new_total * .06
print(f"Sales tax amount: {taxes:.2f}")
print(f"Total: {(new_total + taxes):.2f}")

