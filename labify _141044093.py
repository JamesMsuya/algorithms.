
def dfs(graph, root,superList,list1):
    lis = []
    temp = []
    visited, stack = set(), [root]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    list1 += visited
    temp += visited
    lis=list(graph.keys())
    for i in list1:
        lis.remove(i)
    superList.append(temp)
    if(len(lis)==0):
        return superList
    return dfs(graph,lis[0],superList, list1)


def dfsCover(graph):
    lis = []
    list1 = []
    root=  list(graph.keys())[0]
    list2 = dfs(graph,root,lis, list1)
    return list2

def findMinimumCostToLabifyGTU(x ,y ,mapOfGTU):
    if(y>x):
        return(y*len(mapOfGTU))

    graphPath=dfsCover(mapOfGTU)
    sum=0;
    for i in graphPath:
        sum += x + y*(len(i)-1)

    return sum



mapOfGTU = {
            1 : set([2 ,3]),
            2 : set([1 ,3]),
            3 : set([1 ,2]) } # graph is initialized as dictionary

minCost = findMinimumCostToLabifyGTU(2 ,1 ,mapOfGTU)
print(minCost)

mapOfGTU = {1: set([2, 3]),
            2: set([1, 3, 4]),
            3: set([1, 2, 4]),
            4: set([3, 2]),
            5: set([6]),
            6: set([5])}  # graph is initialized as dictionary


minCost = findMinimumCostToLabifyGTU(5, 2, mapOfGTU)
print(minCost)
