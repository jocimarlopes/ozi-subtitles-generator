from moviepy import VideoFileClip
import tempfile
import os

class AudioGetter:
    def __init__(self, video_path: str):
        self.video_path = video_path

    def get_audio(self):
        print("Extracting audio from video...")
        audio_file = self._get_audio_from_video()
        if not audio_file:
            print("Failed to extract audio from video.")
            exit(1)
        return audio_file

    def _get_audio_from_video(self):
        try:
            video_path = self.video_path
            video = VideoFileClip(video_path)

            # Save to temporary WAV file
            temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
            temp_audio_path = temp_file.name
            temp_file.close()

            video.audio.write_audiofile(temp_audio_path)
            return temp_audio_path  # temporary file path for use with Whisper
        except Exception as e:
            print(f"Error: {e}")
            return None

    def delete_temp_audio_file(file_path: str):
        try:
            os.remove(file_path)
            print(f"Temporary audio file deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting temporary audio file: {e}")