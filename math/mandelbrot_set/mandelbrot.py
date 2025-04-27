import numpy as np
import matplotlib.pyplot as plt

# 画像のサイズと計算領域の設定
width, height = 1000, 1000  # 画像の幅と高さ
xmin, xmax = -2.0, 1.0     # x軸の範囲
ymin, ymax = -1.5, 1.5     # y軸の範囲

# ピクセルごとの複素数を生成
x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)
c = np.array([complex(x_val, y_val) for y_val in y for x_val in x])

# マンデルブロ集合の計算
z = c
mandelbrot = np.zeros(z.shape, dtype=int)
max_iter = 256  # 最大反復回数

for i in range(max_iter):
    z = z * z + c
    mask = np.abs(z) < 2
    mandelbrot += mask

# マンデルブロ集合の描画
mandelbrot = mandelbrot.reshape((height, width))

# カスタマイズオプション
plt.figure(figsize=(8, 8))  # 画像サイズを調整
plt.imshow(mandelbrot, extent=(xmin, xmax, ymin, ymax), cmap='viridis', origin='lower')
# カラーマップを'viridis'に変更
plt.colorbar(label='Iterations')
plt.title('Mandelbrot Set')
plt.xlabel('Real')
plt.ylabel('Imaginary')

# 画像を保存
plt.savefig('mandelbrot_custom.png', bbox_inches='tight')
plt.show()
