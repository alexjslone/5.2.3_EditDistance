def edit_distance(first_string, second_string):
    #return 0
    stringList1 = list(first_string)
    stringList2 = list(second_string)
    comparisonString = []
    for num in range(0, len(stringList2)):
        comparisonString.append("")
    count = 0
    index = 0
    for i in stringList1:
        if stringList1.index(i) < len(stringList2) and i == stringList2[index]:
            comparisonString[stringList1.index(i)]=i
            index +=1
            continue
        elif index > 0 and i == stringList2[index-1]:
            comparisonString[stringList1.index(i)]= i
            index +=1
            continue
        elif index < len(stringList2)-1 and i == stringList2[index+1]:
            comparisonString[stringList1.index(i)]= i
            index +=1 
            continue 
        else: 
            index +=1

    return comparisonString


first_string = "editing"
second_string = "distance"

print(edit_distance(first_string, second_string))


"""

    count = 0
    index = 0
    for i in stringList1:
        if stringList1.index(i) < len(stringList2) and i == stringList2[index]:
            count +=1 
            index +=1 
            continue
        elif index > 0 and i == stringList2[index-1]:
            count +=1
            index +=1
            continue
        elif index < len(stringList2)-1 and i == stringList2[index+1]:
            count +=1
            index +=1 
            continue 
        else: 
            index +=1

    length = max(len(first_string), len(second_string))
    if count == length:
        final= 0
    else:
        final = (length - count) +1
    return final 
"""
#first_string = "ab"
#second_string = "ab"

#print(edit_distance(first_string, second_string))

#if __name__ == "__main__":
#    print(edit_distance(input(), input()))