
import os
import shutil
import sys
import platform

class FFMPEGVerify:
    def __init__(self):
        pass

    def verify(self):
        return self._verify_ffmpeg_installed()

    def verify_system_paths(system):
        paths = {
            'Darwin': [
                "/opt/homebrew/bin",
                "/usr/local/bin"
            ],
            'Windows': [
                "C:\\ffmpeg\\bin",
                "C:\\Program Files\\ffmpeg\\bin"
            ],
            'Linux': [
                "/usr/bin",
                "/usr/local/bin"
            ]
        }
        return paths[system]

    def _verify_ffmpeg_installed(self):
        if shutil.which("ffmpeg"):
            return  # ffmpeg já está acessível no PATH

        system = platform.system()
        possible_paths = []

        possible_paths = verify_system_paths(system)

        for path in possible_paths:
            ffmpeg_path = os.path.join(path, "ffmpeg")
            if os.path.exists(ffmpeg_path) or os.path.exists(ffmpeg_path + ".exe"):
                os.environ["PATH"] += os.pathsep + path
                return

        print("⚠️  Error: ffmpeg not found! Please install ffmpeg and add it to your system PATH.")
        sys.exit(1)
