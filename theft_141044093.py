"""
This algorithm finds the possible maximum values in the next column. 
It assumes the values in first columns are the maximum values the in the second values for each row
the maximum value can be sum of itself and the left top(X[i][j] + X[i-1][j-1]) or left(X[i][j] + X[i][j-1]) or 
left bottom(X[i][j] + X[i-1][j+1]). For values in the top row maxisum can be itself and left(X[i][j] + X[i][j-1]) 
or left bottom(X[i][j] + X[i-1][j+1]) and Lastly for values in bottom row maxisum can be itself and left(X[i][j] + X[i][j-1]) 
or left top(X[i][j] + X[i-1][j-1]). and last before it return it check which element in the last column has the maximum sunm of coins.
Then it return that value.
Every colums its does m additions and three comparisons. since there are n colums totoal additions are n*m and 
total of 3*m*n comparisons. So in worst case it is O(m*n).

"""
def theft(_2dlist):
    if len(_2dlist)==0 or len(_2dlist[0])==0:
        return 0

    temp = _2dlist.copy()
    col= len(_2dlist[0])
    row = len(_2dlist)

    for i in range(1,col,1):
        res = -1
        for j in range(row):

            if j > 0 and j < row-1:
                temp[j][i] += max(temp[j][i-1],temp[j - 1][i - 1],temp[j + 1][i - 1])

            elif j == 0 :
                temp[j][i] += max(temp[j][i-1],temp[j + 1][i - 1])

            elif j == row-1:
                temp[j][i] += max(temp[j][i-1], temp[j - 1][i - 1])

            res = max(temp[j][i], res)
    return res


amountOfMoneyInLand= [[1,3,1,5],[2,2,4,1],[5,0,2,3],[0,6,1,2]]
res = theft(amountOfMoneyInLand)
print(res) #Output: 16
amountOfMoneyInLand= [[10,33,13,15],[22,21,4,1],[5,0,2,3],[0,6,14,2]]
res = theft(amountOfMoneyInLand)
print(res) #Output: 83