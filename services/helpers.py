import os
import subprocess

class Helpers:
    def open_file_folder(srt_path: str):
        # open the srt_path folder with the default file explorer
        if os.name == 'nt':  # Windows
            os.startfile(os.path.dirname(srt_path))
        elif os.name == 'posix':  # macOS or Linux
            subprocess.call(['open', os.path.dirname(srt_path)]) if os.name == 'posix' else subprocess.call(['xdg-open', os.path.dirname(srt_path)])