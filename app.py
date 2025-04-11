from flask import Flask, render_template, request, redirect, url_for, flash
from gtts import gTTS
import os
import logging

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Replace with a strong secret key

# Configure logging for debugging purposes
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    # Check if audio file exists and pass it to template if it does
    audio_file_path = os.path.join("static", "output.mp3")
    if os.path.exists(audio_file_path):
        audio_url = url_for('static', filename='output.mp3')
    else:
        audio_url = None
    return render_template('index.html', audio_file=audio_url)

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form.get('text', '').strip()
    if not text:
        flash("Please enter some text to convert.")
        return redirect(url_for('index'))
    
    try:
        app.logger.info(f"Received text for conversion: {text}")
        tts = gTTS(text=text, lang='en')

        # Ensure the static folder exists
        if not os.path.exists("static"):
            os.makedirs("static")
            app.logger.info("Created 'static' directory.")

        # Save the generated audio
        output_path = os.path.join("static", "output.mp3")
        tts.save(output_path)
        app.logger.info(f"Audio file saved at {output_path}")

        # Redirect back to index to play the audio
        return redirect(url_for('index'))

    except Exception as e:
        app.logger.error(f"Error during TTS generation: {e}")
        flash("An error occurred while generating the audio.")
        return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
