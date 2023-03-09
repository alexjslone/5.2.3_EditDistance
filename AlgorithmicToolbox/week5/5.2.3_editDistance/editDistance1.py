def edit_distance(first_string, second_string):
    #return 0
    stringList1 = list(first_string)
    stringList2 = list(second_string)
    letterCounts = {}

    for letter in stringList1:
        if letter in letterCounts:
            letterCounts[letter] += 1
        else:
            letterCounts[letter] = 1

    # iterate over the second string and count the occurrences of each letter
    for letter in stringList2:
        if letter in letterCounts:
            letterCounts[letter] += 1
        else:
            letterCounts[letter] = 1
    sameCount= 0 
    for value in letterCounts.values(): 
        if value >= 2: 
            sameCount +=1 
    length = max(len(first_string), len(second_string))
    if sameCount == length:
        final= 0
    else:
        final = (length - sameCount) +2
    return final 



#first_string = "shorts"
#second_string = "ports"

#print(edit_distance(first_string, second_string))


if __name__ == "__main__":
    print(edit_distance(input(), input()))



"""
count = 0
    for i in stringList1:
        for s in stringList2: 
            if i == s: 
                count+=1
    length = max(len(first_string), len(second_string))
    if count == length:
        final= 0
    else:
        final = (length - count) +1
    return final 
"""