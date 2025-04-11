from flask import Flask, render_template, request, send_file, redirect, url_for, flash
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
    # Render the HTML form from templates/index.html
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    # Get the text entered by the user from the form
    text = request.form.get('text', '').strip()
    if not text:
        # If the text is empty, flash a message and redirect back to the form
        flash("Please enter some text to convert.")
        return redirect(url_for('index'))
    
    try:
        # Log the received text
        app.logger.info(f"Received text for conversion: {text}")
        
        # Convert the text to speech using gTTS with English as the chosen language
        tts = gTTS(text=text, lang='en')
        
        # Define the output path for your generated audio file
        output_path = os.path.join("static", "output.mp3")
        
        # Ensure the "static" directory exists
        if not os.path.exists("static"):
            os.makedirs("static")
            app.logger.info("Created 'static' directory.")

        # Save the generated audio file
        tts.save(output_path)
        app.logger.info(f"Audio file saved successfully at: {output_path}")

        # Return the generated MP3 file with the appropriate MIME type
        return send_file(output_path, mimetype='audio/mpeg')
    except Exception as e:
        # Log any errors that occur
        app.logger.error(f"Error during TTS generation: {e}")
        flash("An error occurred while generating the audio.")
        return redirect(url_for('index'))

if __name__ == '__main__':
    # Get the port from environment variables or use default port 5000
    port = int(os.getenv("PORT", 5000))
    # Run the app with host set to '0.0.0.0' for public access
    app.run(host="0.0.0.0", port=port, debug=False)
