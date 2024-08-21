def my_avg(num1: int, num2: int) -> float:
    """
    This function takes two integers and return their average as a float
    """
    return (num1 + num2) / 2
avg1 = my_avg(90, 99)
print(avg1)

#################################################################################

def my_headline(text1 :str) -> str:
    """
    This function takes a string and returns it in uppercase with an exclamation mark at the end.
    """
    return text1.upper() + "!"
head1 = my_headline("the world has concurred python")
print(head1)
print(head1)

#################################################################################

from typing import List

def list_concat(list1: List[int], list2: List[int], list3: List[int]) -> List[int]:
    """
    This function takes three lists and unites them into one list.
    """
    return list1 + list2 + list3

con_res = list_concat([9, 8, 7], [6, 5, 4, 3], [2, 1])
print(con_res)
print(len(con_res))
#################################################################################

help(my_avg)
help(my_headline)
help(list_concat)


#################################################################################

from typing import List

def zugi_print_str(numbers: List[int]) -> List[str]:
    """
    This function takes a list of integers and returns a list of strings
    indicating whether each number is even or odd.
    """
    return ["even" if num % 2 == 0 else "odd" for num in numbers]


result = zugi_print_str([14, 14, 15, 10, 2, 3, 5])
print(result)
