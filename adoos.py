import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import AudioFileClip, ImageSequenceClip
from pydub import AudioSegment
import os
from tqdm import tqdm  # 进度条库

def generate_waveform(audio_path, output_dir="frames", fps=30):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load and process the audio
    audio = AudioSegment.from_file(audio_path)
    audio_data = np.array(audio.get_array_of_samples())
    if audio.channels > 1:
        audio_data = audio_data.reshape(-1, audio.channels).mean(axis=1)
    audio_data = audio_data / np.max(np.abs(audio_data))  # Normalize

    num_frames = int(audio.duration_seconds * fps)  # Total frames based on duration
    step_size = len(audio_data) // num_frames  # Step size for each frame

    # Generate waveform images
    with tqdm(total=num_frames, desc="生成波形图像") as pbar:
        for i in range(num_frames):
            start = i * step_size
            end = min((i + 1) * step_size, len(audio_data))
            plt.figure(figsize=(10, 4))
            plt.plot(audio_data[start:end], color="green")
            plt.ylim([-1, 1])
            plt.gca().set_facecolor('black')  # Set background to black
            plt.axis('off')  # Hide axes
            plt.savefig(f"{output_dir}/frame_{i:04d}.png", bbox_inches='tight', pad_inches=0, facecolor='black')
            plt.close()
            pbar.update(1)

    return output_dir

def create_waveform_video(audio_path, output_mp4="output.mp4"):
    # Load audio and get its full duration
    audio_clip = AudioFileClip(audio_path)
    frames_dir = generate_waveform(audio_path)
    
    frames = [f"{frames_dir}/frame_{i:04d}.png" for i in range(int(audio_clip.duration * 30))]
    
    # Create video from the frames and add audio
    video_clip = ImageSequenceClip(frames, fps=30)
    video_with_audio = video_clip.set_audio(audio_clip)
    
    video_with_audio.write_videofile(output_mp4, codec="libx264")

if __name__ == "__main__":
    create_waveform_video("input.mp3")
