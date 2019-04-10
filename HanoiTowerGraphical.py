import numpy as np
global space
space = 10
start = 1


def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    global start
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        MoveKlocek(from_rod, to_rod)
        ViewHanoi()
        return

    if start == 1:
        # creating Tower on start of solving
        start = 0
        # first tower from which we take klocki
        index = (ord(from_rod) - 65)
        for i in range((number_of_klocki - n), number_of_klocki):
            Towers[index][i] = 1
        # second tower on which we put klocki
        index = (ord(to_rod) - 65)
        for i in range(n, number_of_klocki):
            Towers[index][i] = 1
        # third tower still is empty
        index = (ord(aux_rod) - 65)

    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    MoveKlocek(from_rod,to_rod)
    ViewHanoi()
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)


def MoveKlocek(from_rod, to_rod):
        index1 = (ord(from_rod) - 65)
        index2 = (ord(to_rod) - 65)
        for i in range(0, number_of_klocki):
            if Towers[index1][i] == 1:
                Towers[index1][i] = 0
                Towers[index2][i] = 1
                break


def ViewHanoi():
    print("##########################")

    for k in range(0, number_of_klocki):
        for i in range(0, 3):
            # printing space for wciecie in tower
            for x in range(0, int(number_of_klocki - k)):
                print(" ", end='')
            # printing hashtags
            for x in range(0, (Towers[i][k] * (k + 1))):
                print("#", end='')
            # printing space between towers
            for x in range(0, space+k):
                print(" ", end='')

        # print new line
        print("")
    print("##########################")



n = 3
global number_of_klocki
global Towers
number_of_klocki = n

A = np.zeros((number_of_klocki,), dtype=int)
B = np.zeros((number_of_klocki,), dtype=int)
C = np.zeros((number_of_klocki,), dtype=int)
Towers = [A, B, C]
ViewHanoi()
TowerOfHanoi(n, 'A', 'C', 'B')