def main():
    grades=[]
    n=int(input())
    for i in range(n):
        grade=int(input())
        if (grade<=40 or grade%5<=2):
            grades.append(grade)
        else:
            grade=grade+5-(grade%5)
            grades.append(grade)
    print("")
    for a in grades:
        print(a)
if __name__ == "__main__":
    main()