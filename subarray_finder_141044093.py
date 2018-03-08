"""
The algorithm divides a list into two parts and recursively check for the side with minimum contagious sum,
it then checks across the middle  to see if there is a continous array with minmum sum. 
So every time it makes comparison of three sums,the left side,rightside and across the middle.
It divides the list until the left side and the right side of the subarrays have only one element.
It generally divides the whole list. 
So at worst condition its complexity is O(nlogn) - O(n){the time to find sum in a crossmid part of the array}.
O(nlogn) - O(n)= O(nlogn)
"""


#function that finds the minimun contigous array crossing the middle point
def crossSum(arr,mid,start,end):
    sum=0
    positive = 10000000
    leftindex=0
    rightindex = 0
    for i in range(mid, start-1,-1):
        sum = sum + arr[i]
        if sum < positive:
            positive = sum
            leftindex = i
    left = positive

    positive = 10000000
    sum = 0

    for j in range(mid+1, end+1):
        sum = sum + arr[j]
        if sum < positive:
            positive = sum
            rightindex = j
    right = positive
    return(leftindex,rightindex,left + right)


def minarr(arr, low, high):

    mid = (low + high) // 2
    if low == high:

        if (arr[low] <= min(arr)):
            return low, high,arr[low]
        else:
            return arr.index(min(arr)),arr.index(min(arr)),min(arr)


    leftleft,leftright,minLeftSum = minarr(arr, low+1, high)
    rightleft,rightright,minRightSum = minarr(arr, mid + 1, high)
    crossleft,crossright,crosssum = crossSum(arr, mid, low, high)


    if minLeftSum <= minRightSum and minLeftSum <= crosssum:
        return leftleft, leftright, minLeftSum
    if minRightSum <= minLeftSum and minRightSum <= crosssum:
        return rightleft, rightright, minRightSum
    else:
        return crossleft, crossright, crosssum




def min_subarray_finder(arr):
    left,right,sum = minarr(arr,0,len(arr)-1)
    if left==len(arr)-1:
        return arr[left:]
    return arr[left:right+1]


inpArr = [1,-4,-7,5,-13,9,23,-1]

msa = min_subarray_finder(inpArr)
print(msa) #Output: [-4, -7, 5, -13]
print(sum(msa)) #Output: -19