import math

def torus_geodesic_length(R, r, theta1, theta2):
    phi1 = theta1 * 2 * math.pi
    phi2 = theta2 * 2 * math.pi
    cos_phi_diff = math.cos(phi1 - phi2)
    length = math.sqrt((R + r * cos_phi_diff)**2 + (r * math.sin(phi1 - phi2))**2)
    return length

# トーラスの主半径
R = 5

# トーラスの管の半径
r = 2

# 2点間を結ぶ角度パラメータ
theta1 = 0.25
theta2 = 0.75

# 測地線の長さを計算
length = torus_geodesic_length(R, r, theta1, theta2)

# 結果を出力
print("Geodesic length between theta1 and theta2:", length)
