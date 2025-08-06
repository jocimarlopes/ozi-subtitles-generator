
import os
import shutil
import sys
import platform

class FFMPEGVerify:
    def __init__(self):
        pass

    def verify(self):
        return self._verify_ffmpeg_installed()

    def _verify_ffmpeg_installed(self):
        if shutil.which("ffmpeg"):
            return  # ffmpeg já está acessível no PATH

        system = platform.system()
        possible_paths = []

        if system == "Darwin":  # macOS (Homebrew)
            possible_paths = [
                "/opt/homebrew/bin",
                "/usr/local/bin"
            ]
        elif system == "Windows":
            # Tenta caminhos padrão de instalação no Windows
            possible_paths = [
                "C:\\ffmpeg\\bin",
                "C:\\Program Files\\ffmpeg\\bin"
            ]
        elif system == "Linux":
            possible_paths = [
                "/usr/bin",
                "/usr/local/bin"
            ]

        for path in possible_paths:
            ffmpeg_path = os.path.join(path, "ffmpeg")
            if os.path.exists(ffmpeg_path) or os.path.exists(ffmpeg_path + ".exe"):
                os.environ["PATH"] += os.pathsep + path
                return

        print("⚠️  Error: ffmpeg not found! Please install ffmpeg and add it to your system PATH.")
        sys.exit(1)