"""
This algorith divides the K value and make comaparisons of Kth indexes of the two list.
It then recur untill K value is one. So in worst case the algorithm is log(K).

"""

def kth_book_2(m,n,index):
    if len(m)==0:
        return n[index-1]
    elif len(n) == 0:
        return m[index-1]
    elif index == 1 and (len(m)!=0 or len(n)!=0):
        if m[0]< n[0]:
            return m[index-1]
        return n[index-1]

    temp=index//2

    if len(m)<= temp-1:
        if m[-1] < n[0]:
            return n[index - len(m)]

        return kth_book_2(m, n[temp:],  index-temp)

    if len(n) <= temp-1:
        if n[-1] < m[0]:
            return m[index-len(n)]

        return kth_book_2(m[temp:], n, index-temp)
    else:
        if m[temp-1] > n[temp-1]:
            return kth_book_2(m, n[temp:], index-temp)
        if m[temp-1] < n[temp-1]:
            return kth_book_2(m[temp:], n, index-temp)






def find_kth_book_2(m,n,index):
    if index > len(m+n) or index==0:
        return "index out of range"
    else:
        book=kth_book_2(m,n,index)
        return book


m = ["algotihm","baba","programminglanguages","systemsprogramming"]
n = ["computergraphics","ca", "cprogramming","oop"]
book = find_kth_book_2(m,n,5)
print(book) #Output: programminglanguages
book = find_kth_book_2(m,n,6)
print(book) #Output: systemsprogramming
