import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# 设置参数
SAMPLERATE = 44100  # 采样率（每秒采样的点数）
CHANNELS = 1  # 单声道音频
DURATION = 10  # 每次捕获的时长（秒）

# 初始化图形
plt.ion()  # 开启交互模式
fig, ax = plt.subplots(figsize=(10, 4))
ax.set_ylim([-1, 1])
ax.set_xlim([0, SAMPLERATE * DURATION])
line, = ax.plot([], [], lw=2)
ax.set_facecolor('black')
ax.axis('off')  # 关闭坐标轴

# 处理音频数据的回调函数
def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    # 将音频数据标准化
    audio_data = indata[:, 0] / np.max(np.abs(indata))  # 获取音频数据并归一化
    # 更新绘图数据
    line.set_ydata(audio_data)
    line.set_xdata(np.linspace(0, frames, frames))
    plt.draw()
    plt.pause(0.01)  # 暂停以允许绘图更新

# 开始录音并实时显示波形
try:
    with sd.InputStream(callback=audio_callback, channels=CHANNELS, samplerate=SAMPLERATE):
        print("开始捕获音频数据...")
        plt.show()
        while True:
            pass  # 在这里保持程序运行，等待实时音频输入
except KeyboardInterrupt:
    print("捕获停止")
    plt.ioff()  # 关闭交互模式
    plt.show()  # 显示最终图形
