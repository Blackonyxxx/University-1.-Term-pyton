"""
Write a Python function that takes a list containing ints and returns the sum of
the numbers in the given list, returning 0 for an empty list. Here the number 7
does not count and numbers that come immediately after 7 also do not count.
"""

def foo(lst):
    i=0
    total=0
    if(len(lst)<1):
        print("0")
    else:
        while i<len(lst):
            if(lst[i]==7):
                i=i+2
            else:
                total+=lst[i]
                i+=1
        print(total)

def main():
    numbers=input("write numbers separated with space ")
    lst=[int(x) for x in numbers.split()]
    foo(lst)
main()