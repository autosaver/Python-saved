mat=[[12,23,34],[45,56,67],[78,89,91]]
N=3
M=3
K=2
K=K%M
for i in range(N):
    for j in range(M):
        mat[i][j],mat[i][(j+K)%M]=mat[i][(j+K)%M],mat[i][j]
print(mat)
