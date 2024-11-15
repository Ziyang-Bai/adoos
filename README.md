# 音频流示波器

### 该项目用于从音频流（如 音频输入设备麦克风）生成相应的波形。有实时生成和音频文件生成视频两种模式。
# 功能
从音频流或音频文件（MP3、WAV 等）生成波形图像
如果用视频自动根据音频时长生成对应帧数的视频
支持将音频与波形视频同步，生成带有音频的 MP4 文件
# 组件
adoos.py
    生成波形图像序列并保存到指定文件夹中
    将生成的波形图像序列与音频合成为一个视频文件

adoos-lf.py
    与前者并无太大区别
    可以实时查看生成的波形

主要组件 adoos-rt.py
    实时从音频流生成波形图像序列
    允许实时查看生成的波形
    
# 依赖项

在运行本项目之前，请确保已安装以下 Python 库：
    numpy
    matplotlib
    moviepy
    pydub
    tqdm
    sounddevice
    ffmpeg（需要安装系统级的 ffmpeg 工具，用于处理音频和视频）

# 可以通过以下命令来安装这些库：

```
pip install numpy matplotlib moviepy pydub tqdm sounddevice
```

## 安装 FFmpeg

该程序依赖于 FFmpeg 来处理音频和视频文件。你可以通过以下命令来安装：
对于 Ubuntu：

```
sudo apt update
sudo apt install ffmpeg
```
对于 macOS (使用 Homebrew)：

```
brew install ffmpeg
```
对于 Windows：

请访问 FFmpeg 官方网站，下载并按照说明安装。
需要注意的是，FFmpeg 的安装路径需要添加到系统的环境变量中，以便程序能够正确调用。
# 使用说明

将你的音频文件（如 input.mp3）放在与脚本相同的目录下。
在终端或命令行中运行以下命令：
```
adoos.py
```
脚本会生成名为 output.mp4 的波形视频文件。

adoos-rt.py 安装完所需的库（源代码）后直接执行程序即可。
# config.xml 配置文件
```<SAMPLERATE>44100</SAMPLERATE> <!-- 音频采样率（Hz），标准值为44100 -->
<DURATION>20</DURATION> <!-- 捕获音频的总时长（秒） -->
<UPDATE_INTERVAL>25</UPDATE_INTERVAL> <!-- 动画更新间隔（毫秒） -->
<FREQUENCY>440</FREQUENCY> <!-- 正弦波频率（Hz），440为标准音A4 -->
<DEBUGGER_SINE>false</DEBUGGER_SINE> <!-- 是否显示正弦波：true为显示，false为显示麦克风波形 -->
<GRAPH>
    <YMIN>-1</YMIN> <!-- Y轴最小值 -->
    <YMAX>1</YMAX> <!-- Y轴最大值 -->
    <TIME_WINDOW>0.2</TIME_WINDOW> <!-- 显示的时间窗（秒） -->
    <BACKGROUND_COLOR>white</BACKGROUND_COLOR> <!-- 背景颜色 -->
    <SHOW_AXIS>true</SHOW_AXIS> <!-- 是否显示坐标轴 -->
</GRAPH>
<MOTD>
    <!-- ASCII 艺术提示信息 -->
    ('-.     _ .-') _                              .-')    
  ( OO ).-.( (  OO) )                            ( OO ).  
  / . --. / \     .'_  .-'),-----.  .-'),-----. (_)---\_) 
  | \-.  \  ,`'--..._)( OO'  .-.  '( OO'  .-.  '/    _ |  
.-'-'  |  | |  |  \  '/   |  | |  |/   |  | |  |\  :` `.  
 \| |_.'  | |  |   ' |\_) |  |\|  |\_) |  |\|  | '..`''.) 
  |  .-.  | |  |   / :  \ |  | |  |  \ |  | |  |.-._)   \ 
  |  | |  | |  '--'  /   `'  '-'  '   `'  '-'  '\       / 
  `--' `--' `-------'      `-----'      `-----'  `-----'  
</MOTD>
<prop>
    <!-- 程序关键运行信息，请勿随意更改，请按照程序源码为准 -->
    <version>Alpha1.0</version> <!-- 程序版本号 -->
    <author>Ziyang-Bai</author> <!-- 作者信息 -->
    <res>https://github.com/Ziyang-Bai/adoos</res> <!-- 资源链接 -->
</prop>
```
# 注意事项
存储空间: 程序生成的图像帧数较多，可能会占用大量存储空间。建议定期清理生成的 frames 文件夹。

性能: 对于长时间的音频文件，生成和处理波形图像可能会消耗大量内存和处理时间。如果处理较长的音频，可以考虑调整帧率以减少生成的帧数。

# 贡献

如果你对该项目有任何改进建议或发现了问题，欢迎通过提交 Issue 或 Pull Request 来贡献你的代码。
# 许可

该项目采用 Apache-2.0 许可。详情请参阅 LICENSE 文件。
