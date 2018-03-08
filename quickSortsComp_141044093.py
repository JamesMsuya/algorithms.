"""
Lomuto gives worst running time when the list contains duplicates while Houre works fine in those conditions.
Houare partition is more efficient as it does less swaps than lomuto at worst case.
both schemes reduces to O(n^2) ift the list is already sorted.

"""

def partitionLomuto(arr,low,high):
    pivot = arr[high]
    i = low-1
    j=low
    while j <= high-1:

        if arr[j] <= pivot:
            i=i+1
            arr[i], arr[j]= arr[j], arr[i]
        j+=1

    arr[i+1], arr[high]=arr[high], arr[i+1]
    return i+1


def partitionHoure(arr,low,high):
    pivot = arr[low]
    i = low + 1
    j = high
    done = True
    while done:
        while arr[i] <= pivot and i <= j:
            i=i+1
        while arr[j] >= pivot and i <= j:
            j=j-1

        if i > j:
            done=False
        else:
            arr[i],arr[j]=arr[j],arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quicksortLomutoHelper(arr,low,high):

    if low < high:
        pi=partitionLomuto(arr,low,high)#pertition index

        quicksortLomutoHelper(arr, low, pi-1)
        quicksortLomutoHelper(arr, pi + 1, high)


def quicksortHoareHelper(arr,low,high):

    if low < high:
        pi=partitionHoure(arr,low,high)

        quicksortHoareHelper(arr, low, pi-1)
        quicksortHoareHelper(arr, pi + 1, high)


def quickSortHoare(arr):
    quicksortHoareHelper(arr,0,len(arr)-1)
    return arr

def quickSortLomuto(arr):
    quicksortLomutoHelper(arr,0,len(arr)-1)
    return arr


arr = [15,4,68,24,75,16,42]

qsh = quickSortHoare(arr)
print(qsh) #Output: [4, 15, 16, 24, 42, 68, 75]
qsl = quickSortLomuto(arr)
print(arr) #Output: [4, 15, 16, 24, 42, 68, 75]