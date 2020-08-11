import os
import numpy as np
import matplotlib.pyplot as plt

# excelデータをインポート
folderName = os.path.dirname(os.path.abspath(__file__))
fileName = "sinc_4.csv"
time_wave = np.loadtxt(os.path.join(folderName, fileName))
time = np.array(range(time_wave.size)) * 0.01

# 波形を描画する
# plt.figure(0, figsize=(10, 6))
# plt.plot(time, time_wave, "b")
# plt.xlim([0, 20])
# plt.xlabel("Time [µs]")
# plt.ylabel("Voltage [V]")
# plt.show()

# スペクトル波形を作る
freq_wave = np.fft.fft(time_wave)  # 複素数
freq = np.fft.fftfreq(freq_wave.size, d=0.01)

# スペクトル波形を描画する
plt.figure(1, figsize=(10, 6))
plt.plot(freq, np.abs(freq_wave), "b")
plt.xlim([-2, 2])
plt.ylim([0, 1500])
plt.xlabel("Frequency [MHz]")
plt.ylabel("Amplitude [V]")
plt.show()

# fftしたデータを保存
saveFileName = fileName.split(".")[0] + "_freq.csv"
saveData = np.array([freq, np.abs(freq_wave)], dtype=np.float64).T
np.savetxt(os.path.join(folderName, saveFileName), saveData, delimiter=",", fmt="%.5e")

# ピークを特定
# print("peek at 1.0MHz: {}".format(np.abs(freq_wave[np.where(freq == 1.0)[0]])))
# print("peek at 1.1MHz: {}".format(np.abs(freq_wave[np.where(freq == 1.1)[0]])))
# print("peek at 1.2MHz: {}".format(np.abs(freq_wave[np.where(freq == 1.2)[0]])))

