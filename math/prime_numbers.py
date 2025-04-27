
#nからn^2までの間を長さnの区間で分割したときに、各区間に素数が存在することを確認するためのコード
import math
 
n = int(input())
a = 1
while a <= n:
    m = int(math.sqrt(n*a))
    k = [n*a // i for i in range(1, m+1)]
    k += range(k[-1]-1, 0, -1)
    h = {i: i-1 for i in k}
 
    for i in range(2, m+1):
        if h[i] > h[i-1]:
            p = h[i-1]
            i2 = i*i
            for j in k:
                if j < i2:
                   break
                h[j] -= h[j // i] -p            

    l = int(math.sqrt(n*(a+1)))
    k = [n*(a+1) // i for i in range(1, l+1)]
    k += range(k[-1]-1, 0, -1)
    g = {i: i-1 for i in k}
 
    for i in range(2, l+1):
        if g[i] > g[i-1]:
            p = g[i-1]
            i2 = i*i
            for j in k:
                if j < i2:
                   break
                g[j] -= g[j // i] -p            
                               
    print(g[n*(a+1)]-h[n*a])
    a += 1
