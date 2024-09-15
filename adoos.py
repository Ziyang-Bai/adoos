import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import AudioFileClip, ImageSequenceClip
from pydub import AudioSegment
import os

def generate_waveform(audio_path, num_frames=1000, output_dir="frames"):
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
    audio_data = audio_data / np.max(np.abs(audio_data))
    
    # Generate waveform images
    for i in range(num_frames):
        plt.figure(figsize=(10, 4))
        
        # Calculate frame segments for each chunk
        start_frame = int(i * len(audio_data) / num_frames)
        end_frame = int((i + 1) * len(audio_data) / num_frames)
        audio_segment = audio_data[start_frame:end_frame]
        
        plt.plot(audio_segment)
        plt.ylim([-1, 1])
        plt.axis('off')
        
        # Save the plot as an image file
        plt.savefig(f"{output_dir}/frame_{i:04d}.png", bbox_inches='tight', pad_inches=0)
        plt.close()
    
    return output_dir

def create_waveform_video(audio_path, output_mp4="output.mp4"):
    frames_dir = generate_waveform(audio_path)
    audio_clip = AudioFileClip(audio_path)
    
    # Ensure correct frame count and fps for the video
    num_frames = 1000
    frames = [f"{frames_dir}/frame_{i:04d}.png" for i in range(num_frames)]
    
    # Create the video from the frames
    video_clip = ImageSequenceClip(frames, fps=num_frames / audio_clip.duration)
    
    # Combine video with audio
    video_with_audio = video_clip.set_audio(audio_clip)
    
    # Write the video to the output file
    video_with_audio.write_videofile(output_mp4, codec="libx264")

if __name__ == "__main__":
    mp3_file = "input.mp3"
    create_waveform_video(mp3_file, output_mp4="output.mp4")
