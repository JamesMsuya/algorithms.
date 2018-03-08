

def compareScales (leftScaleList, rightScaleList):
    result = sum(leftScaleList) - sum(rightScaleList)
    if result < 0:
        return 1
    elif result > 0:
        return -1
    else:
        return 0


def rottenWalnut (walnut):
    if len(walnut)==2:
        if compareScales(walnut[0:1],walnut[1:])==1:
            return 0
        elif compareScales(walnut[0:1],walnut[1:])==-1:
            return 1
        else:
            return -1

    if len(walnut)%2==0 and len(walnut)>2:

        if compareScales(walnut[0:int((len(walnut)) / 2)], walnut[int((len(walnut)) / 2):]) == 1:
            return rottenWalnut(walnut[0:int((len(walnut)) / 2)])

        elif compareScales(walnut[0:int((len(walnut)) / 2)], walnut[int((len(walnut)) / 2):]) == -1:
            return rottenWalnut(walnut[int((len(walnut)) / 2):])+ int((len(walnut)) / 2)
        elif compareScales(walnut[0:int((len(walnut))/2)],walnut[int((len(walnut))/2):])==0 :
            return -1

    if len(walnut) % 2 != 0:
        if compareScales(walnut[0:int((len(walnut)) / 2)], walnut[int(((len(walnut)) / 2)+1):]) == 0 and walnut[int(len(walnut)/2)]!= walnut[0]:
            return int((len(walnut)) / 2)
        if compareScales(walnut[0:int((len(walnut)) / 2)], walnut[int(((len(walnut)) / 2)+1):]) == 0 and walnut[int(len(walnut)/2)]== walnut[0]:
            return 0
        elif compareScales(walnut[0:int((len(walnut)) / 2)], walnut[int(((len(walnut)) / 2)+1):]) == -1:
            return rottenWalnut(walnut[int(((len(walnut)) / 2)+1):]) + int((len(walnut)) / 2)+1

        elif compareScales(walnut[0:int((len(walnut)) / 2)], walnut[int((len(walnut)) / 2):]) == 1:
            return rottenWalnut(walnut[0:int((len(walnut)) / 2)])



print(rottenWalnut([1,1,1,0.5,1,1]))