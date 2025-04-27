import numpy as np
import matplotlib.pyplot as plt

# データの作成
N = 1000 # サンプル数
t = np.linspace(0, 10, N) # 時間軸
f1 = 1 # 周波数1
f2 = 2 # 周波数2
data = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t) # 信号データ

# フーリエ変換
freq = np.fft.fftfreq(N, d=t[1]-t[0]) # 周波数軸
fft = np.fft.fft(data) # フーリエ変換結果
abs_fft = np.abs(fft) # 振幅スペクトル
angle_fft = np.angle(fft) # 位相スペクトル

# グラフの描画
fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(8, 6))
axs[0].plot(t, data)
axs[0].set_ylabel('Amplitude')
axs[0].set_title('Signal')
axs[1].plot(freq, angle_fft)
axs[1].set_ylabel('Phase')
axs[1].set_xlabel('Frequency [Hz]')
axs[1].set_xlim(0, 5)
axs[1].set_title('Phase Spectrum')
plt.show()
