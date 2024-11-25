
```markdown
# YouTube Audio Downloader 🎵

A simple and efficient Python-based tool to download audio from YouTube videos in high-quality MP3 format. This tool uses the powerful `yt-dlp` library for seamless downloads and audio conversion.  

---

## 🌟 Features
- Downloads the **best available audio quality** from YouTube videos.
- Converts audio to **MP3 format** with a bitrate of **192 kbps**.
- Saves the downloaded file using the video title as the filename.
- Includes a user-friendly interface with clear instructions and error handling.

---

## 🛠 Requirements
To use this tool, you need to have the following installed:
- **Python 3.6 or above**
- **FFmpeg** (for audio conversion)
- **yt-dlp** (Python library)

---

## 🚀 Installation and Setup
Follow these steps to set up the tool locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/nag2mani/AwesomePythonTools.git
   cd YouTubeAudioDownloader
   ```

2. **Install Required Python Libraries:**
   Use pip to install the dependencies.
   ```bash
   pip install yt-dlp
   ```

3. **Install FFmpeg:**
   FFmpeg is required to extract and convert audio. Install it based on your OS:
   - **Linux:**  
     ```bash
     sudo apt update
     sudo apt install ffmpeg
     ```
   - **MacOS:**  
     ```bash
     brew install ffmpeg
     ```
   - **Windows:**  
     Download the FFmpeg binary from [FFmpeg's official site](https://ffmpeg.org/) and add it to your system's PATH.

---

## 🎉 How to Use
1. Run the script:
   ```bash
   python3 download_audio.py
   ```

2. Enter the YouTube video URL when prompted:
   ```
   🔗 Enter a YouTube video URL to download the audio: https://www.youtube.com/watch?v=example
   ```

3. The script will download and save the audio file in the **current directory** with the video title as the filename.

---

## ✨ Example Output
```text
************************************************************
🎉 YouTube Audio Downloader Script 🎉
Made with ❤️ by Nikhil Yadav
************************************************************

🔗 Enter a YouTube video URL to download the audio: https://www.youtube.com/watch?v=example
🎵 Downloading audio... Please wait.
✅ Download completed successfully!

Thank you for using this tool! Happy listening! 🎶
```

---

## ❗ Troubleshooting
If you encounter any issues, here are some common solutions:
1. **HTTP Error 403: Forbidden**
   - This might occur if the URL is restricted. Make sure the video is public and accessible.
   
2. **FFmpeg not found**
   - Ensure FFmpeg is installed and added to your system's PATH. You can verify the installation by running:
     ```bash
     ffmpeg -version
     ```

3. **yt-dlp errors**
   - Update `yt-dlp` to the latest version:
     ```bash
     pip install -U yt-dlp
     ```

---

## 🤝 Contributing
Feel free to fork the repository, make improvements, and submit a pull request. Contributions are always welcome!

---

### ❤️ Developed by Nikhil Yadav
If you enjoy this tool, give it a star 🌟 and share it with others!
```

