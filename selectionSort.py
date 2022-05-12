numbres=[1,22,3,4,557,5];
def selectionSort(numes):

    for i in range(len(numes)):
        for i in range(len(numes)-1-i):
            if numes[i]>numes[i+1]:
                temp = numes[i+1];
                numes[i+1] = numes[i];
                numes[i] = temp;
    return numes
print (selectionSort(numbres));