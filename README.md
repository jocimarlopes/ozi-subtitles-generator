# 🎬 Ozi - MP4 Videos Subtitles Generator with Python

**Ozi** is a simple and powerful tool that automatically extracts audio from your `.mp4` videos and generates subtitle files (`.srt`) using OpenAI's Whisper model.

Developed in Python, it's ideal for creators, editors, or anyone who wants to subtitle their videos locally with ease.

---

## 📦 Features

- Transcribe audio from MP4 using Whisper AI
- Select the subtitles language (EN, PT, ES, FR)
- Save subtitles in `.srt` format  

---

## ✅ Requirements

- Python 3.8 or higher  
- FFmpeg (must be installed and accessible via command line)

---

## ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ozi-subtitles-generator.git  
   cd ozi-subtitles-generator
   ```

2. Make sure you have Python and FFmpeg installed:

   - Python: https://www.python.org/downloads/  
   - FFmpeg: https://ffmpeg.org/download.html  
     (Add FFmpeg to your system PATH.)

3. Run the setup script:

   ```bash
   python setup.py
   ```

This will:

- Install the necessary Python packages (from `requirements.txt`)  

---

## 🚀 Usage

To run the program:

```bash
python app.py
```

You’ll see a User Interface, just select the MP4, the language to substitle, Generate Now! And Ozi will do the rest.

---

## 📁 Folder Structure

```
project/  
├── app.py  
├── setup.py  
├── requirements.txt  
├── icons/  
│   ├── *.png  
│   ├── *.icns  
├── services/  
│   ├── __init__.py  
│   ├── menu.py  
│   ├── gui.py  
│   ├── helpers.py  
│   ├── audio_getter.py  
│   └── audio_transcriber.py  
```

---

## 📄 License

MIT License

---

## 👤 Author

**Jocimar Lopes**  
Developed by **Jolo Systems** 🚀