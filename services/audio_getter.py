from moviepy import VideoFileClip

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
            audio_path = 'audios/' + video_path.split("/")[-1].replace(".mp4", ".wav")
            video.audio.write_audiofile(audio_path)
            return audio_path
        except Exception as e:
            print(f"Error: {e}")
            return None
