# 連続した5つの整数の積が平方数になるかチェックするためのコード
import numpy as np
import math
import matplotlib.pyplot as plt

n = 6
while n < 3000:
    a = n*(n-1)*(n-2)*(n-3)*(n-4)
    b = math.sqrt(a)
    try:
        print(isinstance(b, int))
        n += 1
    except Exception as e:
        print(error)




# nの範囲を指定
n_values = np.linspace(0, 6, 100)  # 0から6までの間を100点で分割

# yを計算
y_values = n_values * (n_values - 1) * (n_values - 2) * (n_values - 3) * (n_values - 4)

# グラフ描画
plt.plot(n_values, y_values)
plt.xlabel('n')
plt.ylabel('y')
plt.title('Graph of y = n*(n-1)*(n-2)*(n-3)*(n-4)')
plt.grid(True)
plt.show()


"""
import numpy as np
import math

n = 6
while n < 3000:
    a = n*(n-1)*(n-2)*(n-3)*(n-4)
    b = math.sqrt(a)
    print(b)
    n += 1
"""