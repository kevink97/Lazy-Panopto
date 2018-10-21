from flask import Flask
from requests import get
import detect
import video_to_text
import upload

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/projects/')
def projects():
    return 'Projects page'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/transcribe/<path:gcs_link>')
def transcribe_gsc_link(gcs_link):
    alternative = video_to_text.speech_transcription(gcs_link)
    return ('Transcript: {}'.format(alternative.transcript))

@app.route('/upload/<path:url>')
def ocr(url):
    with open("temp.jpg","wb") as file:
        response = get(url)
        file.write(response.content)

    upload.upload_blob("panopto", "temp.jpg", "temp.jpg")
    return detect.detect_text_uri("gs://panopto/temp.jpg")

@app.route('/translate/<')

if __name__ == "__main__":
    app.run("0.0.0.0",ssl_context='adhoc')





