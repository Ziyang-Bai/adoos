import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import AudioFileClip, ImageSequenceClip
from pydub import AudioSegment
import os
from tqdm import tqdm  # 进度条库

def generate_waveform(audio_path, target_duration, output_dir="frames"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load the audio file with pydub
    audio = AudioSegment.from_file(audio_path)
    
    # Convert audio to numpy array
    audio_data = np.array(audio.get_array_of_samples())
    
    # Handle stereo to mono conversion if necessary
    if audio.channels > 1:
        audio_data = audio_data.reshape(-1, audio.channels).mean(axis=1)
    
    # Normalize audio data
    max_abs_value = np.max(np.abs(audio_data))
    if max_abs_value > 0:
        audio_data = audio_data / max_abs_value  # Ensure audio data is in the range [-1, 1]
    
    # Calculate the number of frames based on target video duration
    fps = 30  # 视频帧率
    num_frames = int(target_duration * fps)  # 确保 num_frames 是整数

    # 确保音频数据能填满所有帧，避免卡顿
    audio_data_len = len(audio_data)
    step_size = int(audio_data_len / num_frames)  # 确保 step_size 是整数
    
    # 增加每帧的采样点数量
    frame_samples = max(step_size, 100)  # 每帧的最小采样点数为 100
    num_frames = int(np.ceil(audio_data_len / frame_samples))  # 计算调整后的帧数

    # 进度条
    with tqdm(total=num_frames, desc="生成波形图像") as pbar:
        # Generate waveform images
        for i in range(num_frames):
            plt.figure(figsize=(10, 4))
            
            # 根据帧数动态调整采样点数量
            start_frame = int(i * frame_samples)
            end_frame = min(int((i + 1) * frame_samples), audio_data_len)
            audio_segment = audio_data[start_frame:end_frame]
            
            # 绘制波形，设置颜色和背景
            plt.plot(audio_segment, color="green")  # 绿色波形
            plt.ylim([-1, 1])  # 根据归一化音频数据调整 y 轴范围
            
            # 设置背景为黑色
            plt.gcf().patch.set_facecolor('black')  # 整个图的背景为黑色
            plt.gca().set_facecolor('black')  # 坐标轴背景为黑色
            
            plt.axis('off')  # 关闭坐标轴
            
            # 保存图像并确保背景为黑色
            plt.savefig(f"{output_dir}/frame_{i:04d}.png", bbox_inches='tight', pad_inches=0, facecolor='black')  # 确保背景为黑色
            plt.close()
            
            pbar.update(1)  # 更新进度条
    
    return output_dir

def create_waveform_video(audio_path, output_mp4="output.mp4"):
    # Load audio and check its full duration
    audio_clip = AudioFileClip(audio_path)
    audio_duration = audio_clip.duration  # 获取音频的完整时长
    
    # 生成波形图像，使用音频的实际时长
    frames_dir = generate_waveform(audio_path, target_duration=audio_duration)
    
    fps = 30  # 视频帧率
    num_frames = int(audio_duration * fps)  # 根据音频时长计算总帧数
    
    frames = [f"{frames_dir}/frame_{i:04d}.png" for i in range(num_frames)]
    
    # Create the video from the frames
    video_clip = ImageSequenceClip(frames, fps=fps)
    
    # 同步音频与视频时长
    video_with_audio = video_clip.set_audio(audio_clip)
    
    # Write the video to the output file
    video_with_audio.write_videofile(output_mp4, codec="libx264")

if __name__ == "__main__":
    mp3_file = "input.mp3"
    create_waveform_video(mp3_file, output_mp4="output.mp4")
