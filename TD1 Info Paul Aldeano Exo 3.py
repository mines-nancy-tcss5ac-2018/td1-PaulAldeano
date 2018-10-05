def palyndrome(x):
    L=str(x)
    for i in range(len(L)//2):
        if L[i]!=L[len(L)-1-i]:
            return False
        return True