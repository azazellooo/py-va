import speech_recognition as sr
import pyttsx3


class SpeechRecognizer:
    recognizer = sr.Recognizer()
    voice_engine = pyttsx3.init()

    def recognize(self):
        with sr.Microphone() as mic:
            self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            self.voice_engine.say("I hear you..")
            self.voice_engine.runAndWait()
            audio = self.recognizer.listen(mic)
            try:
                text = self.recognizer.recognize_google(audio)
                print(f'text:            {text}')
                print('Converting audio transcripts into text ...')
                print(text)
            except:
                text = None
                self.voice_engine.say('Sorry, try again.')
                self.voice_engine.runAndWait()
        return text

