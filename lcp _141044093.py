"""
The algorithm divides a list until its length is either one or two, 
then it finds the common postfix of that substring.
It then goes up in a recursive way to find the common postfix of the postfixes found.
The algorithm is backed by a function which finds the common postfix of two strings at O(m)(where m is the length of the longest word)time.
With assumption that string comparisons happen at constant time, then the algorithm being divide and conqure
at worst case  n-1 comparisons are made which make this algorithm O(nm)if n>>m then algorithm is simply O(n).
"""

def longest_common_postfix(inpStrings):
    if(len(inpStrings)==1 or len(inpStrings)==2):
        return common_postfix(inpStrings)

    mid=len(inpStrings)//2
    left_postfix=longest_common_postfix(inpStrings[:mid+1])
    righ_postfix=longest_common_postfix(inpStrings[mid+1:])

    lis=[left_postfix,righ_postfix]
    return(common_postfix(lis))

#this is a function which finds longest postfix between two string or a single string
#The assumption is this function runs at constant time.
def common_postfix(strings):
    if len(strings) == 1:
        return strings[0]

    postfix = strings[0]
    if strings[1] !="" and strings[0]!="":
        while strings[1][-len(postfix):] != postfix:
                postfix = postfix[-(len(postfix)-1):]
                if len(postfix)==1 and postfix!=strings[1][-1]:
                    postfix=""
                    break
        return postfix
    return ""

inpStrings = ["absorptivity", "circularity", \
              "electricity", "importunity", "humanity"]
lcp = longest_common_postfix(inpStrings)

print(lcp)
