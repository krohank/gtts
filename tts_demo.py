from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3", lang="en"):
    """Convert text to speech and save it as an MP3 file."""
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(filename)

    # Play the audio file (on Windows, 'start' works; use 'open' for macOS)
    os.system(f"start {filename}")

if __name__ == "__main__":
    sample_text = "Hello, welcome to your text-to-speech demo!"
    text_to_speech(sample_text)
