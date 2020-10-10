from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse,Message
import pytube

app = Flask(__name__)

@app.route("/", methods=['POST'])
def index():
    msg = request.form.get('Body')
    resp = MessagingResponse()
    msg = str(msg)
    # url = msg[3:]
    if 'http' in msg:
        youtube = pytube.YouTube(msg)
        video = youtube.streams.first()
        video.download('static', filename='1')
        mediaurl = resp.message("ok")
        mediaurl.media("./static/1.mp4")
    else:
        resp.message('Hello!')
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)