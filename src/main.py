import PySimpleGUI as sg
import pyttsx3
from wikipedia.exceptions import DisambiguationError, PageError

from setup import Window
from search import get_wolframs_answer, get_wikis_answer
from recognizer import SpeechRecognizer


def main():
    voice_engine = pyttsx3.init()
    window = Window().setup()
    while True:
        event, values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        command = values[0]
        if event == 'Speech':
            sr = SpeechRecognizer()
            command = sr.recognize()
            if not command:
                main()
        try:
            wiki_res = get_wikis_answer(command)
            wolfram_res = get_wolframs_answer(command)
            voice_engine.say(wolfram_res)
            sg.PopupNonBlocking(f"Wolfram says: {wolfram_res}\nWikipedia says: {wiki_res}")

        except (DisambiguationError, PageError):
            wolfram_res = get_wolframs_answer(command)
            voice_engine.say(wolfram_res)
            sg.PopupNonBlocking(wolfram_res)

        except:
            wiki_res = get_wikis_answer(command)
            voice_engine.say(wiki_res)
            sg.PopupNonBlocking(wiki_res)

        voice_engine.runAndWait()

    window.close()


if __name__ == '__main__':
    main()

