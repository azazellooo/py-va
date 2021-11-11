import PySimpleGUI as sg


class Window:
    theme = 'DarkGreen'
    title = 'PyVA'
    header = "Enter your command: "

    def setup(self):
        sg.theme(self.theme)
        layout = [[sg.Text(self.header)],
                  [sg.Input()],
                  [sg.Button('Ok')],
                  [sg.Button('Speech')],
                  [sg.Button('Exit')]]
        return sg.Window(self.title, layout)
