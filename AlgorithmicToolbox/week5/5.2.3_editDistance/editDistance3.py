#solution using 2d list/array with dynamic programming principles 
import math


def edit_distance(first_string, second_string):
    first_string = list(first_string)
    second_string= list(second_string)
    twoDimList=  [[math.inf for j in range(len(second_string)+1)] for i in range(len(first_string)+1)]
    #for i in range(len(twoDimList)):
    #    for j in range(len(twoDimList[i])):
     #       twoDimList[i][j]
    for j in range(len(second_string)+1):
        twoDimList[len(first_string)][j]=len(second_string)-j
    for i in range(len(first_string)+1):
        twoDimList[i][len(second_string)]=len(first_string)-i

    for i in range(len(first_string)-1, -1, -1):
        for j in range(len(second_string)-1, -1, -1 ):
            if first_string[i] == second_string[j]:
                twoDimList[i][j]= twoDimList[i+1][j+1]
            else: 
                twoDimList[i][j]= 1+ min(twoDimList[i+1][j], twoDimList[i][j+1], twoDimList[i+1][j+1])
    return twoDimList[0][0]      
#first_string = 'editing'
#second_string= 'distance'
#print(edit_distance(first_string, second_string))

if __name__ == "__main__":
    print(edit_distance(input(), input()))