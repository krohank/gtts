from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from gtts import gTTS
import os

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Replace with a strong secret key

@app.route('/')
def index():
    # Render the HTML form from templates/index.html
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    # Get the text entered by the user from the form
    text = request.form.get('text', '')
    if not text.strip():
        # If the text is empty, flash a message and redirect back to the form
        flash("Please enter some text to convert.")
        return redirect(url_for('index'))
    
    # Convert the text to speech using gTTS with English as the chosen language
    tts = gTTS(text=text, lang='en')
    
    # Define the output path for your generated audio file
    # Save the file in the "static" folder so it can be easily served
    output_path = os.path.join("static", "output.mp3")
    tts.save(output_path)
    
    # Return the generated MP3 file with the appropriate MIME type
    # Your browser should play the audio or prompt for download
    return send_file(output_path, mimetype='audio/mpeg')

if __name__ == '__main__':
    # Get the port from environment variables or use default port 5000
    port = int(os.getenv("PORT", 5000))
    # Run the app with host set to '0.0.0.0' for public access
    app.run(host="0.0.0.0", port=port, debug=False)
