import PySimpleGUI as sg
import pyttsx3
from wikipedia.exceptions import DisambiguationError, PageError

from search import get_wolframs_answer, get_wikis_answer

sg.theme('DarkGreen')
voice_engine = pyttsx3.init()
layout = [[sg.Text("Enter your command: ")],
          [sg.Input()],
          [sg.Button('Ok')],
          [sg.Button('Exit')]]
window = sg.Window('PyVA', layout)

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    command = values[0]
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

