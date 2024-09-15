import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import AudioFileClip, ImageSequenceClip

# 生成音频波形图
def generate_waveform(audio_path, num_frames=1000, output_dir="frames"):
    audio = AudioFileClip(audio_path)
    
    # 提取音频数据
    audio_data = audio.to_soundarray(fps=44100)
    
    # 生成波形图
    for i in range(num_frames):
        plt.figure(figsize=(10, 4))
        start_frame = int(i * len(audio_data) / num_frames)
        end_frame = int((i + 1) * len(audio_data) / num_frames)
        audio_segment = audio_data[start_frame:end_frame]
        
        plt.plot(audio_segment)
        plt.title(f"Frame {i+1}")
        plt.ylim([-1, 1])
        plt.axis('off')
        
        # 保存每一帧波形图
        plt.savefig(f"{output_dir}/frame_{i:04d}.png", bbox_inches='tight', pad_inches=0)
        plt.close()
    
    return output_dir

# 将生成的波形图合成为MP4视频
def create_waveform_video(audio_path, output_mp4="output.mp4"):
    # 生成波形图并存储为图像帧
    frames_dir = generate_waveform(audio_path)
    
    # 提取音频
    audio_clip = AudioFileClip(audio_path)
    
    # 加载所有生成的帧图像
    frames = [f"{frames_dir}/frame_{i:04d}.png" for i in range(1000)]
    
    # 生成视频
    video_clip = ImageSequenceClip(frames, fps=30)
    
    # 将音频添加到视频中
    video_with_audio = video_clip.set_audio(audio_clip)
    
    # 导出为MP4文件
    video_with_audio.write_videofile(output_mp4, codec="libx264")

if __name__ == "__main__":
    mp3_file = "your_audio_file.mp3"  # 输入的MP3文件
    create_waveform_video(mp3_file, output_mp4="output.mp4")
