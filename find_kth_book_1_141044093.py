"""
The algorithm divides a list into two parts and recursively and makes comparisons.

"""


def kth_book(m,n,index):
    if len(m)==0:
        return n[index]
    if len(n) == 0:
        return m[index]

    mid_m=len(m)//2
    mid_n=len(n)//2
    mid_sum=mid_m+mid_n

    if mid_sum < index:
        if m[mid_m] > n[mid_n]:
            return kth_book(m,n[mid_n+1:],index-mid_n-1)

        return kth_book(m[mid_m+1:],n,index-mid_m-1)

    if m[mid_m] > n[mid_n]:
        return kth_book(m[:mid_m], n, index)
    return kth_book(m, n[:mid_n], index)


def find_kth_book_1(m,n,index):
    if index > len(m+n):
        return "index out of range"
    else:
        book=kth_book(m,n,index-1)
        return book


m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming","oop"]
book = find_kth_book_1(m,n,1)
print(book) #Output: programminglanguages
book = find_kth_book_1(m,n,6)
print(book) #Output: systemsprogramming
