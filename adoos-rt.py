import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sounddevice as sd
import xml.etree.ElementTree as ET

# 读取XML配置
def load_config(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    config = {
        'SAMPLERATE': int(root.find('SAMPLERATE').text),
        'DURATION': float(root.find('DURATION').text),
        'UPDATE_INTERVAL': int(root.find('UPDATE_INTERVAL').text),
        'FREQUENCY': float(root.find('FREQUENCY').text),
        'DEBUGGER_SINE': root.find('DEBUGGER_SINE').text.lower() == 'true',
        'GRAPH': {
            'YMIN': float(root.find('GRAPH/YMIN').text),
            'YMAX': float(root.find('GRAPH/YMAX').text),
            'TIME_WINDOW': float(root.find('GRAPH/TIME_WINDOW').text),
            'BACKGROUND_COLOR': root.find('GRAPH/BACKGROUND_COLOR').text,
            'SHOW_AXIS': root.find('GRAPH/SHOW_AXIS').text.lower() == 'true',
        }
    }
    return config

# 加载配置
config = load_config("config.xml")

# 使用配置中的参数
SAMPLERATE = config['SAMPLERATE']
DURATION = config['DURATION']
UPDATE_INTERVAL = config['UPDATE_INTERVAL']
FREQUENCY = config['FREQUENCY']
debugger_sine = config['DEBUGGER_SINE']
GRAPH_CONFIG = config['GRAPH']

# 初始化图形
fig, ax = plt.subplots(figsize=(10, 4))
ax.set_ylim([GRAPH_CONFIG['YMIN'], GRAPH_CONFIG['YMAX']])  # 设置Y轴范围
ax.set_xlim([0, SAMPLERATE * GRAPH_CONFIG['TIME_WINDOW']])  # 设置X轴范围
ax.set_facecolor(GRAPH_CONFIG['BACKGROUND_COLOR'])  # 设置背景颜色
if not GRAPH_CONFIG['SHOW_AXIS']:
    ax.axis('off')  # 关闭坐标轴
line, = ax.plot([], [], lw=2)

# 音频数据缓存
buffer_size = int(SAMPLERATE * GRAPH_CONFIG['TIME_WINDOW'])  # 根据时间窗大小调整缓存
audio_data = np.zeros(buffer_size)

# 创建正弦波
t = np.linspace(0, DURATION, SAMPLERATE, endpoint=False)
sine_wave = np.sin(2 * np.pi * FREQUENCY * t)

# 音频数据回调函数
def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    # 更新缓存数据
    audio_data[:-frames] = audio_data[frames:]
    audio_data[-frames:] = indata[:, 0]

# 更新绘图函数
def update_plot(frame):
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
