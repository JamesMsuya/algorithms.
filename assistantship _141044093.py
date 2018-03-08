
#recursive function to find permuation of a list
def permutation(list):

    if len(list) == 0:
        return []

    if len(list) == 1:
        return [list]

    permutationList = []#empty list to feed the permutations
    for i in range(len(list)):
        m = list[i]
        lis = list[:i] + list[i + 1:]
        for p in permutation(lis):
            permutationList.append([m] + p)
    return permutationList


def findOptimalAssistantship(list):
    if(len(list)==0):
        return [],0
    else:
        r=len(list)
        n=len(list[0])
        assList=[]
        for i in range(n):
            assList+= [i]
        for i in range(r-n):
            assList+=[-1]

        permutatedAssList = permutation(assList)
        total=0;
        compare=99999999999999 #for comparison purposes
        temp=0;
        for i in range(len(permutatedAssList)):
            total = 0
            for j in range(len(permutatedAssList[i])):
                if(permutatedAssList[i][j]!=-1):
                    total+=list[j][permutatedAssList[i][j]]
                if (permutatedAssList[i][j] == -1):
                    total+=6#constant number for assistant doing other stuffs
            if(total<compare):
                temp=i
                compare=total;

        return permutatedAssList[temp],compare




inputTable = [[5, 8,  7],  # R.A. 0
              [8, 12, 7],  # R.A. 1
              [4, 8, 5],
              [4, 8, 5]]  # R.A. 2]  # R.A. 2


a=findOptimalAssistantship(inputTable)
print(a)
