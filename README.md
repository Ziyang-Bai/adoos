# 波形视频生成器

### 该项目用于从音频文件（如 MP3）生成相应的波形视频。通过将音频转换为波形图像序列，最终合成一个包含音频的可视化视频。
# 功能

    从音频文件（MP3、WAV 等）生成波形图像
    自动根据音频时长生成对应帧数的视频
    支持将音频与波形视频同步，生成带有音频的 MP4 文件

# 依赖项

在运行本项目之前，请确保已安装以下 Python 库：

    numpy
    matplotlib
    moviepy
    pydub
    tqdm
    ffmpeg（需要安装系统级的 ffmpeg 工具，用于处理音频和视频）

# 可以通过以下命令来安装这些库：

```
pip install numpy matplotlib moviepy pydub tqdm
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

# 函数说明
generate_waveform(audio_path, target_duration, output_dir="frames")

    功能: 从音频文件生成波形图像序列，并保存到指定文件夹中。
    参数:
        audio_path: 输入音频文件的路径。
        target_duration: 视频的目标时长（通常为音频的时长）。
        output_dir: 图像保存的目录，默认为 frames。

create_waveform_video(audio_path, output_mp4="output.mp4")

    功能: 将生成的波形图像序列与音频合成为一个视频文件。
    参数:
        audio_path: 输入音频文件的路径。
        output_mp4: 输出视频文件名，默认为 output.mp4。

# 注意事项

    存储空间: 程序生成的图像帧数较多，可能会占用大量存储空间。建议定期清理生成的 frames 文件夹。
    性能: 对于长时间的音频文件，生成和处理波形图像可能会消耗大量内存和处理时间。如果处理较长的音频，可以考虑调整帧率以减少生成的帧数。

# 贡献

如果你对该项目有任何改进建议或发现了问题，欢迎通过提交 Issue 或 Pull Request 来贡献你的代码。
# 许可

该项目采用 Apache-2.0 许可。详情请参阅 LICENSE 文件。
