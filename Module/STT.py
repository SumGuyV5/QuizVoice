import speech_recognition as sr


class STT:
    rec = sr.Recognizer()

    def __init__(self, stt=True):
        self.stt = stt

    def speech_rec(self, text, valid_responses=[]):
        valid_responses = [item.lower() for item in valid_responses]
        answer = ""
        if self.stt:
            while not answer:
                with sr.Microphone() as source:
                    print("Speak:")
                    audio = STT.rec.listen(source)

                try:
                    answer = STT.rec.recognize_sphinx(audio)
                    print(f"You said: {answer}")
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")

                if answer == 'repeat':
                    answer = '-1'
                else:
                    try:
                        answer = str(valid_responses.index(answer.lower()) + 1)
                    except ValueError:
                        answer = '-1'
        else:
            answer = input(text)
        return answer

