"""
Write a Python function that takes 3 ints, x, y z
as parameters and returns True if one of y or
z differs from x by at most 1, while the other
differs from both other values by 2 or more.
 """

def prb(a, b, c):
    if(abs(a-b)<=1 and abs(c-a)>=2 and abs(b-c)>=2):
        print("True")
    elif(abs(a-c)<=1 and abs(b-a)>=2 and abs(b-c)>=2):
        print("True")
    else:
        print("False")

def main():
    x=int(input(""))
    y=int(input(""))
    z=int(input(""))
    prb(x,y,z)

    
main()