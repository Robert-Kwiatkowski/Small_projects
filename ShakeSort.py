def ShakeSort(alist):
    def swap(i, j):
        alist[i], alist[j] = alist[j], alist[i]
    upp = len(alist) -1
    down = 0

    no_change = False
    while(not no_change and upp - down > 1):
        no_change = True
        for j in range(down, upp):
            if alist[j+1] < alist[j]:
                swap(j+1,j)
                no_change = False
        upp = upp -1

        for j in range(upp, down, -1):
            if alist[j-1] > alist[j]:
                swap(j -1, j)
                no_change = False
        down = down + 1

alist = [1, 3, 10, 2, 5, 4, 6, 11, 9]
ShakeSort(alist)
print(alist)


