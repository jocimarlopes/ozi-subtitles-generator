🎬 Ozi - MP4 Videos Subtitles Generator with Python

Ozi is a simple and powerful tool that automatically extracts audio from your .mp4 videos and generates subtitle files (.srt) using OpenAI’s Whisper model.

Developed in Python, it’s ideal for creators, editors, or anyone who wants to subtitle their videos locally with ease.

⸻

📦 Features
	•	List available .mp4 videos
	•	Detect if a subtitle already exists for each video
	•	Extract audio from videos
	•	Transcribe audio using Whisper AI
	•	Save subtitles in .srt format

⸻

✅ Requirements
	•	Python 3.8 or higher
	•	FFmpeg (must be installed and accessible via command line)

⸻

⚙️ Installation
	1.	Clone the repository:
git clone https://github.com/yourusername/ozi-subtitles-generator.git
cd ozi-subtitles-generator
	2.	Make sure you have Python and FFmpeg installed:
	•	Python: https://www.python.org/downloads/
	•	FFmpeg: https://ffmpeg.org/download.html
(Add FFmpeg to your system PATH.)
	3.	Run the setup script:
python setup.py

This will:
	•	Create the required folders: videos/, audios/, and subtitles/
	•	Install the necessary Python packages (from requirements.txt)
	•	Automatically download the Whisper model

⸻

🚀 Usage

To run the program:

python app.py

You’ll see a menu with available videos. Just select one by index and Ozi will do the rest.

⸻

📁 Folder Structure

project/
├── app.py
├── setup.py
├── requirements.txt
├── videos/
├── audios/
├── subtitles/
├── services/
│   ├── __init__.py
│   ├── menu.py
│   ├── audio_getter.py
│   └── audio_transcriber.py

⸻

📄 License

MIT License

⸻

👤 Author

Jocimar Lopes
Developed by Jolo Systems 🚀