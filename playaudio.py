from playsound import playsound
from gtts import gTTS
import subprocess

mytext = 'Welcome to geeksforgeeks!'
myobj = gTTS(text=mytext, lang='en', slow=False)
myobj.save("welcome.mp3")
play_audio("welcome.mp3")

