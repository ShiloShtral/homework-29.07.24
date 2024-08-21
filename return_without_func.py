def my_ascending(x, y):
    """In this function, the user inputs 2 numbers and receives them in ascending order."""

    if x < y:
        print(f"{x}, {y}")
    elif y < x:
        print(f"{y}, {x}")
    else:
        print("You entered the same number, try entering two different numbers.")



my_ascending(7, 12)

##############################################################

def my_details(s):
    """In this function, the user inputs a string and receives the first letter, the middle letter, and the last letter."""

    if len(s) > 0:
        first_letter = s[0]
        middle_index = len(s) // 2
        middle_letter = s[middle_index]
        last_letter = s[-1]

        print(f"The first letter in the string is: {first_letter}")
        print(f"The middle letter in the string is: {middle_letter}")
        print(f"The last letter in the string is: {last_letter}")
    else:
        print("The string is empty.")


my_details("Ai is the best")

##############################################################

def say_bool(value):
    """if the value is true , print yes .
      if the value is false , print no ."""

    if value:
        print("yes")
    else:
        print("no")

say_bool(True)
say_bool(False);

##############################################################
def zugi_print(numbers):
    """This function receives a list of integers and prints whether each number is 'even' or 'odd'."""
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")


zugi_print([14, 14, 15, 10, 2, 3, 5])

##############################################################

from typing import List

def my_statistic(grades: List[int]):
    """In this function, the user gets the highest grade, the lowest grade, the number of grades, and the average of the grades."""

    if not grades:
        print("No grades provided.")
        return

    highest = max(grades)
    lowest = min(grades)
    count = len(grades)
    average = sum(grades) / count

    print(f"The highest grade: {highest}")
    print(f"The lowest grade: {lowest}")
    print(f"The number of grades: {count}")
    print(f"The average of grades: {average:.2f}")

grades = []

while True:
    input_str = input("Enter a grade (-99 to exit): ")
    try:
        grade = int(input_str)

        if grade == -99:
            break

        if 0 <= grade <= 100:
            grades.append(grade)
        else:
            print("Grade must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

print("List of grades:", grades)

my_statistic(grades)


help(my_ascending)
help(my_details)
help(say_bool)
help(zugi_print)
help(my_statistic)