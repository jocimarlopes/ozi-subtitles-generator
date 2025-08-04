import whisper

class AudioTranscriber:
    def __init__(self, audio_path: str):
        self.model = whisper.load_model("medium")  # pode usar 'small', 'medium' ou 'large'
        self.audio_path = audio_path

    def transcribe(self):
        print("Transcribing audio to subtitles...")
        subtitles_file = self._transcribe_audio()
        if not subtitles_file:
            print("Failed to transcribe audio.")
            exit(1)
        return subtitles_file

    def _transcribe_audio(self):
        try:
            audio_path = self.audio_path
            FINAL_PATH = 'subtitles/' + audio_path.split("/")[-1].replace(".wav", ".srt")
            result = self.model.transcribe(audio_path, task="transcribe", language="pt", verbose=True)
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