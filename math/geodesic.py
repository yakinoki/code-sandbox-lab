# coding: utf-8

#%%

#原点中心、半径rの球面上の2点の座標が与えられた時、その間の最短測地線の長さを求める。
#ここでは共に北半球、東側の点とする。また北極点は除く。

import math
import matplotlib.pyplot as plt
import numpy as np


#まず半径を決める。
r=float(input())
print("半径は{}".format(r))

#一つ目の座標を決定。
x1=float(input())
y1=float(input())
z1=math.sqrt(r**2-x1**2-y1**2)

print("一つ目の座標は({},{},{})".format(x1,y1,z1))
theta1 = math.acos(x1/math.sqrt(x1**2+y1**2))

phi1 = math.atan(z1/math.sqrt(x1**2+y1**2))

x1 = r * math.cos(theta1)*math.cos(phi1)
print("x1={}".format(x1))
y1 = r * math.sin(theta1)*math.cos(phi1)
print("y1={}".format(y1))
z1 = r * math.sin(phi1)
print("z1={}".format(z1))

print("緯度は{}".format(phi1))
print("経度は{}".format(theta1))

#二つ目の座標を決定。
x2=float(input())
y2=float(input())
z2=math.sqrt(r**2-x2**2-y2**2)

print("二つ目の座標は({},{},{})".format(x2,y2,z2))

theta2 = math.acos(x2/math.sqrt(x2**2+y2**2))
print("経度は{}".format(theta2))

phi2 = math.atan(z2/math.sqrt(x2**2+y2**2))
print("緯度は{}".format(phi2))

x2 = r * math.cos(theta2)*math.cos(phi2)
#print("x2={}".format(x2))
y2 = r * math.sin(theta2)*math.cos(phi2)
#print("y2={}".format(y2))
z2 = r * math.sin(phi2)
#print("z2={}".format(z2))

d = r * math.acos(math.sin(theta1)*math.sin(theta2) + math.cos(theta1)*math.cos(theta2)*math.cos(phi1-phi2))

print("二点間の球面上の距離は{}".format(d))

# 2つの点を配列に格納
points = [(x1, y1, z1), (x2, y2, z2)]

# 可視化のための関数
def plot_geodesic(points, r):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # 球面をプロット
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = r * np.outer(np.cos(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.sin(v))
    z = r * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='b', alpha=0.1)
    
    # 2点をプロット
    x, y, z = zip(*points)
    ax.scatter(x, y, z, c='r', marker='o', s=100)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

# 可視化関数を呼び出し
plot_geodesic(points, r)

#%%

