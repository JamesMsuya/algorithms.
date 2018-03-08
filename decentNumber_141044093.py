"""
This algorithm work by optimizing the number of 5's in a decentNumber. So the greedy choice is
assuming the number at hand is the maximum number of fives that can be divisible by three.
If it is not minus five then test. If a  number is found then the number of 3's is N-number of 5's .
If there is no possibility of 5's to be represented another greedy option is made.
That the number can only be represented in 3's divisible by 5. If it does not comply then the number can not be represented 
and -1 is returned.
"""
def decentNumber(num):
    m=0
    N=num
    while(m<num):
        if N%3==0:
            return "5" * N + "3" * m
        N = N - 5
        m = m + 5
    if(num%5==0):
        return "3" * num
    return "-1"

dn =  decentNumber(1)
print(dn) #Output: -1
dn =  decentNumber(3)
print(dn) #Output: 555
dn =  decentNumber(5)
print(dn) #Output: 33333
dn =  decentNumber(10)
print(dn) #Output: 55555533333