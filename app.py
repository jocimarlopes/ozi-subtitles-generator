import threading
from services import AudioGetter, AudioTranscriber, GUI, Helpers, FFMPEGVerify

class Main:
    def __init__(self, gui):
        self.gui = gui
        
    def run(self, video_path, language):
        audio_file = AudioGetter(video_path).get_audio()
        srt_path = AudioTranscriber(audio_file, language, video_path).transcribe()
        self.gui.set_buttons_enabled(True)
        AudioGetter.delete_temp_audio_file(audio_file)
        print("===============\nProcess completed successfully\n===============\n")
        Helpers.open_file_folder(srt_path)


if __name__ == "__main__":
    FFMPEGVerify().verify()
    gui = GUI()
    main = Main(gui)
    gui.set_generate_callback(lambda path, lang: threading.Thread(target=main.run, args=(path, lang), daemon=True).start())
    gui.run()