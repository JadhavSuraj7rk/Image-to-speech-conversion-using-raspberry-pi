from gtts import gTTS
import os

Text = "Text to speech conversion using Python "

language = 'en'

output = gTTS(text=Text, lang=language, slow=False)

output.save("output.mp3")

os.system("start output.mp3")
