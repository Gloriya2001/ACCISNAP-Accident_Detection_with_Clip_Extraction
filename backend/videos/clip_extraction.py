import os
import subprocess

def extract_clip(video_path, start_time, duration, output_path):
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Use full path to FFmpeg
        ffmpeg_path = r"C:\ffmpeg\ffmpeg-7.1-essentials_build\bin\ffmpeg.exe"  # Change this if needed

        command = [
            ffmpeg_path,  # Use full path
            "-i", video_path,
            "-ss", str(start_time),
            "-t", str(duration),
            "-c", "copy",
            output_path
        ]
        
        print(f"Running FFmpeg command: {' '.join(command)}")  # Debugging log
        
        subprocess.run(command, check=True)

        print(f"Clip saved successfully at: {output_path}")  # Debugging log

    except Exception as e:
        print(f"Error in extract_clip: {str(e)}")
        raise
