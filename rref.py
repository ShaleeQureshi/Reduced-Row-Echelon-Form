from sys import stdin
from fractions import Fraction

rowNum = int(input("Enter the number of rows\n"))
colNum = 4  # for 3D
matrix = []

for x in range(rowNum):
    element1, element2, element3, element4 = map(int, stdin.readline().split())
    matrix.append((element1, element2, element3, element4))


def rref(M, rowCount, columnCount):
    current = 0
    for r in range(rowCount):
        if current >= columnCount:
            return
        i = r
        while M[i][current] == 0:
            i += 1
            if i == rowCount:
                i = r
                current += 1
                if columnCount == current:
                    return
        M[i], M[r] = M[r], M[i]
        lv = M[r][current]
        M[r] = [mrx / float(lv) for mrx in M[r]]
        for i in range(rowCount):
            if i != r:
                lv = M[i][current]
                M[i] = [iv - lv*rv for rv, iv in zip(M[r], M[i])]
        current += 1


rref(matrix, rowNum, colNum)
for r in matrix:
    print(', '.join((str(Fraction(c).limit_denominator()) for c in r)))
