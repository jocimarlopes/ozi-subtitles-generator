import os
import subprocess
import whisper

def create_folders():
    for folder in ["videos", "audios", "subtitles"]:
        os.makedirs(folder, exist_ok=True)
    print("✅ Folders created.")

def install_requirements():
    print("📦 Installing dependencies from requirements.txt...")
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    print("✅ Dependencies installed.")

def download_whisper_model():
    print("⬇️ Downloading AI model (medium)...")
    whisper.load_model("medium")
    print("✅ AI model downloaded.")

if __name__ == "__main__":
    create_folders()
    install_requirements()
    download_whisper_model()
    print("🚀 Setup complete!")