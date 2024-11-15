import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sounddevice as sd

# 设置参数
SAMPLERATE = 44100  # 采样率（每秒采样的点数）
DURATION = 1  # 每次捕获的时长（秒）
UPDATE_INTERVAL = 50  # 动画更新的时间间隔（毫秒）
FREQUENCY = 440  # 正弦波频率（Hz）

# 控制是否显示正弦波（True 为显示正弦波，False 为显示麦克风音频波形）
debugger_sine = False

# 初始化图形
fig, ax = plt.subplots(figsize=(10, 4))
ax.set_ylim([-1.5, 1.5])  # 调整Y轴范围，以便看到更清晰的波形
ax.set_xlim([0, SAMPLERATE])  # 显示1秒钟的数据
line, = ax.plot([], [], lw=2)
ax.set_facecolor('black')
ax.axis('off')  # 关闭坐标轴

# 音频数据缓存
audio_data = np.zeros(SAMPLERATE)

# 创建正弦波
t = np.linspace(0, DURATION, SAMPLERATE, endpoint=False)
sine_wave = np.sin(2 * np.pi * FREQUENCY * t)

# 音频数据回调函数
def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    # 获取输入数据，并更新缓存
    audio_data[:-frames] = audio_data[frames:]
    audio_data[-frames:] = indata[:, 0]

# 用于更新绘图的函数
def update_plot(frame):
    # 根据debugger_sine的值来选择绘制正弦波或麦克风数据
    if debugger_sine:
        line.set_ydata(sine_wave)  # 显示正弦波
    else:
        line.set_ydata(audio_data)  # 显示麦克风音频波形
    line.set_xdata(np.linspace(0, len(audio_data), len(audio_data)))  # 更新X轴数据
    return line,

# 开始录音并实时显示波形
def start_audio_stream():
    with sd.InputStream(callback=audio_callback, channels=1, samplerate=SAMPLERATE):
        ani = FuncAnimation(fig, update_plot, blit=True, interval=UPDATE_INTERVAL, cache_frame_data=False)
        plt.show()

if __name__ == "__main__":
    start_audio_stream()
