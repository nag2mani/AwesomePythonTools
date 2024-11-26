# This script allows users to download audio from YouTube videos in MP3 format.
# Developed by Nikhil Yadav
# Utilizes the yt-dlp library for robust and seamless downloading.

import yt_dlp

def download_audio():
    """
    Prompts the user to input a YouTube video URL and downloads the audio in MP3 format.
    The downloaded file will be saved with the video title as the filename.
    """
    print("\nWelcome to the YouTube Audio Downloader!")
    print("Developed by Nikhil Yadav 💻\n")
    
    # Ask the user for the YouTube video URL
    url = input("🔗 Enter a YouTube video URL to download the audio: ").strip()
    
    # Define options for yt-dlp
    options = {
        'format': 'bestaudio/best',  # Ensure the best available audio quality is downloaded
        'outtmpl': '%(title)s.%(ext)s',  # Save file with video title as the filename
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Extract audio using FFmpeg
            'preferredcodec': 'mp3',      # Convert to MP3 format
            'preferredquality': '192',    # Set audio quality to 192 kbps
        }],
    }

    try:
        # Initialize yt-dlp with the defined options and start the download
        with yt_dlp.YoutubeDL(options) as ydl:
            print("🎵 Downloading audio... Please wait.")
            ydl.download([url])
            print("✅ Download completed successfully!")
    except Exception as e:
        # Handle any errors gracefully and display the issue to the user
        print(f"❌ An error occurred while downloading: {e}")

if __name__ == "__main__":
    print("************************************************************")
    print("🎉 YouTube Audio Downloader Script 🎉")
    print("Made with ❤️ by Nikhil Yadav")
    print("************************************************************\n")
    
    # Call the main function to start the audio download process
    download_audio()
    print("\nThank you for using this tool! Happy listening! 🎶")
