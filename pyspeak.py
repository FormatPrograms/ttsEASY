from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS
import os

def speak(text):
    text = None
    speak = gTTS(f'{text}', lang='en')
    speak.save("voice.mp3")
    pwd = os.getcwd()
    speak(pwd + '/voice.mp3')
    nee = AudioSegment.from_mp3("voice.mp3")
    play(nee)
    os.system("rm " + pwd + '/voice.mp3')
