"""
Consider the leftmost and righmost appearances of some value in an int list. We'll say that
the "range" is the number of elements between the two inclusive. A single value has a range
of 1. Write a Python function that returns the largest range found in the given list.
"""

def foo(lst):
    result=1
    if(len(lst)<1):
        print("0")
    else:
        for i in range(len(lst)):
            first=lst[i]
            for j in reversed(range(len(lst))):
                second=lst[j]
                if(first==second):
                    temp=j-i+1
                    if(temp>result):
                        result=temp
        print(result)
            
def main():
    numbers=input("write numbers separated with space ")
    lst=[int(x) for x in numbers.split()]
    foo(lst)
main()