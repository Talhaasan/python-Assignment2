def findSubString(givenString, lengthOfGivenString):#find and print all sub strings.
    sublists=[]#the resulting sublists are added to this list.
    print("[ ")
    for iter in range(1, lengthOfGivenString + 1):
        for i in range(lengthOfGivenString - iter + 1):
            j = i + iter - 1
            for k in range(i, j + 1):
                 sublists.append(givenString[k])#append givenString to the sublists.
                 print(sublists[k],end=",")#print sublists.
            print()

    print("]")


subString = input("Enter string: ") #give string
findSubString(subString, len(subString))
