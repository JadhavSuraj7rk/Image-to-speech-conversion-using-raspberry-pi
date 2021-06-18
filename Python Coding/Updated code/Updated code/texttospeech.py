from gtts import gTTS
import os


def text_to_speech():

    fh = open("sample.txt", "r")
    Text = fh.read()

    language = 'en'

    output = gTTS(text=Text, lang=language, slow=False)

    output.save("output.mp3")
    fh.close()

    os.system("start output.mp3")
