
def hanoi(height,fromPole, toPole, withPole,time):
    if height >= 1:
        hanoi(height-1,fromPole,withPole,toPole,time)
        moveDisk(height,fromPole,toPole,time)
        hanoi(height-1,withPole,toPole,fromPole,time)

def moveDisk(height,source,destination,time):
    if (source== "SRC" and destination== "DST") or (source== "DST" and destination== "SRC"):
        time[height-1] += 2*height
    if (source == "AUX" and destination == "DST") or (source == "DST" and destination == "AUX"):
        time[height - 1] += 1*height
    if (source == "SRC" and destination == "AUX") or (source == "AUX" and destination == "SRC"):
        time[height - 1] += 1*height

    print("disk",height,":",source,"to",destination)


def hanoiWrapper(height):
    time = [];
    for i in range(height):
        time = time + [0]
    print("Input size is",height)
    hanoi(height,"SRC","DST","AUX",time)
    for i in range(height):
        print("Elapsed time for disk",i+1,":",time[i])

hanoiWrapper(3)