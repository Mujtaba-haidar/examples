from gtts import gTTS
from playsound import playsound

mytext = 'Hello mujtaba'
myjob = gTTS(text=mytext)
myjob.save('move.mp3')
playsound('move.mp3')
