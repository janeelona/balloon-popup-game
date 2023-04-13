from pathlib import Path

import PySimpleGUI as sg
import pandas as pd

# Add some color to the window
sg.theme('DarkTeal9')

current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
EXCEL_FILE = current_dir / 'Data_Entry.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
    [sg.Text('Please enter your name:')],
    [sg.Text('Name', size=(15,1)), sg.InputText(key='Name')],
    [sg.Submit(), sg.Exit()]
]

window = sg.Window('Simple data retrieval form', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    name = values['Name']
    row = df.loc[df['Name'] == name]
    if not row.empty:
        new_score = row['NewScore'].values[0]
        old_score = row['OldScore'].values[0]
        sg.popup(f"Name: {name}\nNewScore: {new_score}\nOldScore: {old_score}")
    else:
         if event == 'Submit':
                    new_record = pd.DataFrame(values, index=[0])
                    df = pd.concat([df, new_record], ignore_index=True)
                    df.to_excel(EXCEL_FILE, index=False)
                    sg.popup('Data saved!')
window.close()
