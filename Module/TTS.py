import pyttsx3


class TTS:
    engine = pyttsx3.init()

    def __init__(self, tts=True):
        self.tts = tts

    def say(self, text):
        if self.tts:
            TTS.engine.say(text)
            TTS.engine.runAndWait()
        else:
            print(text)
