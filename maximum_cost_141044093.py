"""
This algorithm keeps tracks of two local defined list. For every i'th number in an list Y two assumtions are made
 that is is itself or 1. The subsequent sums of when it is 1 or itself are kept in two list lis and li respectively.
 The list lis[] and li[] are initialized to 0 assuming previous sum is 0.
 lis[i] = The maximum i'th cost when X[i]= 1 which can be when i'th number 1 - 1 + previous sum lis[i-1](assuming in list X[i-1]=1) or
abs(1-X[i-1]) + li[i-1](assuming X[i]=1 and X[i-1]=Y[i-1]) and likewise
li[i] = The maximum i'th cost when X[i]= Y[i] which can be when i'th number X[i] - 1 + previous sum lis[i-1](assuming in list X[i-1]=1) or
abs(X[i]-X[i-1]) + li[i-1](assuming X[i]=Y[i] and X[i-1]=Y[i-1]) so this adds the elements in lis and li subsequently until 
n'th position. So the maximum cost will be maximum value between li[n] or lis[n].
In all the cases it does addition N times in all the two list it keeps. So in worst case the algorithm is O(n).
"""

def find_maximum_cost(Y):
    lis ,li =[0],[0]
    for i in range(1,len(Y),1):
        lis.append(max(lis[i-1],abs(Y[i-1]-1)+li[i-1]))
        li.append(max(abs(Y[i]-1)+lis[i-1],abs(Y[i]-Y[i-1])+li[i-1]))

    return max(lis[len(Y)-1],li[len(Y)-1])


Y = [14,1,14,1,14]
cost = find_maximum_cost(Y)
print(cost) #Output: 52
Y = [1,9,11,7,3]
cost = find_maximum_cost(Y)
print(cost) #Output: 28
Y = [50,28,1,1,13,7]
cost = find_maximum_cost(Y)
print(cost) #Output: 78
Z=[80, 22, 45, 11, 67, 67, 74, 91, 4, 35, 34, 65, 80, 21, 95, 1, 52, 25, 31, 2, 53]
print(find_maximum_cost(Z)) #output: 1107
Z=[79, 6 ,40, 68, 68, 16, 40, 63, 93, 49, 91]
print(find_maximum_cost(Z)) #output: 642
