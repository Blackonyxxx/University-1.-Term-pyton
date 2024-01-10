def foo(lst):
    if (len(lst)>=1):
        print(max(lst)-min(lst))
    else:
        main()
        

def main():
    numbers=input("give a numbers with space seperated ")
    lst=[int(x) for x in numbers.split()]
    foo(lst)
main()

