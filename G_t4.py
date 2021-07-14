
def lcs(X , Y):
    
    m = len(X)
    n = len(Y)
  
    L = [[None]*(n+1) for i in range(m+1)]
  
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
  
    return L[m][n]

n1,n2,x1,x2 = input().split()
s1 = input()
s2 = input()

lcsN = lcs(s1,s2)
print((int(n1) - lcsN)*int(x1)+(int(n2) - lcsN)*int(x2))