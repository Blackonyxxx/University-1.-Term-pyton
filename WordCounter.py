def function(string):
    counter=1
    result=""
    for i in range(len(string)-1):
        if(string[i]==string[i+1]):
            counter=counter+1
        else:
            result=result+string[i]+str(counter)
            counter=1
    result=result+string[-1]+str(counter)
    return result

def main():
    outputs=[]
    n=int(input())
    for i in range(n):
        str=input("")
        outputs.append(function(str))
    print("")
    for output in outputs:
        print(output)

if __name__ == "__main__":
    main()