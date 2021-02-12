def isPermutations(list1, list2):#take parameter as two list
    l1 = sorted(list1)#sort a using the sorted (built in) function and assign c.
    l2 = sorted(list2)#sort b using the sorted (built in) function and assign d.

    requiredElementsList1=[]#additional  for l1
    requiredElementsList2 =[] # additional  for l2

    if (l1 == l2):#contol the list elements
        return True

    else:
        count = 0#the number of elements that should be added to the lists.
        for i in range (1,len(l1)):
            if l1[i] not in l2:
                for j in range (len(l1)):
                        if(l1[j] not in l2 ):
                            requiredElementsList2.append(l1[j])#elements that should be added to l2 were found and these elements were added to a new list.
                            count+=1

            elif l2[i] not in l1:
                for k in range(len(l2)):
                    if(l2[k] not in l1):
                        requiredElementsList1.append(l2[k])#elements that should be added to l1 were found and these elements were added to a new list.
                        count+=1
            else:
                requiredElementsList2.append(l1[i])#If the same element exists, these elements are added to the list again.
                count+=1

    return print("list1 needs {} ,list2 needs {} to make them permutations .".format(requiredElementsList1,requiredElementsList2))


print(isPermutations([10, 9, 11, 1], [9, 1, 11, 10]))
print(isPermutations([10, 9, 1, 10], [8, 1, 11, 10]))


