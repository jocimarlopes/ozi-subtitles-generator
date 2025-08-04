from services import AudioGetter, AudioTranscriber, Menu

class Main:
    def run(self):
        video_path = Menu().get_video_path()
        audio_file = AudioGetter(video_path).get_audio()
        AudioTranscriber(audio_file).transcribe()
        print("Process completed successfully.")

if __name__ == "__main__":
    Main().run()