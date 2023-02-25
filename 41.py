Matrix = [[6,4],[2,8],[1,12]]
Matrix2 = [[0 for j in range(len(Matrix))] for i in range(len(Matrix[0]))]
for i in range(len(Matrix)):
    for j in range(len(Matrix[0])):
        Matrix2[j][i] = Matrix[i][j]
        print(Matrix2)
