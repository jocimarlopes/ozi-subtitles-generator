import whisper
from services.helpers import Helpers

class AudioTranscriber:
    def __init__(self, audio_path: str, language: str = "pt", video_path: str = None):
        self.model = whisper.load_model("medium")  # pode usar 'small', 'medium' ou 'large'
        self.audio_path = audio_path
        self.video_path = video_path
        self.language = language

    def transcribe(self):
        print("Transcribing audio to subtitles...")
        subtitles_file = self._transcribe_audio()
        if not subtitles_file:
            print("Failed to transcribe audio.")
            Helpers.exit()
        return subtitles_file

    def _transcribe_audio(self):
        try:
            import os
            audio_path = self.audio_path
            video_path = os.path.basename(self.video_path)
            video_directory = os.path.dirname(self.video_path)
            srt_filename = os.path.basename(video_path).replace(".mp4", ".srt")
            FINAL_PATH = os.path.join(video_directory, srt_filename)
            print('\n\nSetting/Downloading AI model... Wait a moment.\n\n')
            result = self.model.transcribe(audio_path, task="transcribe", language=self.language, verbose=True)
            # Salvar como SRT
            with open(FINAL_PATH, "w", encoding="utf-8") as f:
                for i, segment in enumerate(result["segments"], start=1):
                    start = segment["start"]
                    end = segment["end"]
                    text = segment["text"]

                    def format_time(seconds):
                        h = int(seconds // 3600)
                        m = int((seconds % 3600) // 60)
                        s = int(seconds % 60)
                        ms = int((seconds - int(seconds)) * 1000)
                        return f"{h:02}:{m:02}:{s:02},{ms:03}"

                    f.write(f"{i}\n")
                    f.write(f"{format_time(start)} --> {format_time(end)}\n")
                    f.write(f"{text.strip()}\n\n")
            return FINAL_PATH
        except Exception as e:
            print(f"Error: {e}")
            return None
