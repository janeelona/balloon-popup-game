import pygame
import sys
from settings import *
from background import Background
import ui
import cv2
import os
from pathlib import Path
import PySimpleGUI as sg
import pandas as pd


class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()
        self.click_sound = pygame.mixer.Sound(f"Assets/Sounds/slap.wav")

    def draw(self):
        self.background.draw(self.surface)
        # draw title
        ui.draw_text(self.surface, GAME_TITLE, (SCREEN_WIDTH//2, 120), COLORS["title"], font=FONTS["big"],
                    shadow=True, shadow_color=(255,255,255), pos_mode="center")

    def update(self):
            self.draw()
            if ui.button(self.surface, 390+BUTTONS_SIZES[1]*1.2, "INDEX", click_sound=self.click_sound):
                return "game"

            if ui.button(self.surface, 470+BUTTONS_SIZES[1]*1.5, "QUIT", click_sound=self.click_sound):
                pygame.quit()
                sys.exit()

            if ui.button(self.surface, 280+BUTTONS_SIZES[1]*1.2, "MIDDLE", click_sound=self.click_sound):
                os.chdir("C:/Users/JOHNREMY/Documents/gameV2/Gametwo")
                os.system("python C:/Users/JOHNREMY/Documents/gameV2/Gametwo/main.py")

            if ui.button(self.surface, 175+BUTTONS_SIZES[1]*1.2, "RING", click_sound=self.click_sound):
                os.chdir("C:/Users/JOHNREMY/Documents/gameV2/Gamethree")
                os.system("python C:/Users/JOHNREMY/Documents/gameV2/Gamethree/main.py")

            if ui.button(self.surface, 175, "PINKY", click_sound=self.click_sound):
                os.chdir("C:/Users/JOHNREMY/Documents/gameV2/Gamefour")
                os.system("python C:/Users/JOHNREMY/Documents/gameV2/Gamefour/main.py")


    # def update(self):
    #     self.draw()
    #     if ui.button(self.surface, 320, "START", click_sound=self.click_sound):
    #         current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
    #         EXCEL_FILE = current_dir / 'Data_Entry.xlsx'
    #         df = pd.read_excel(EXCEL_FILE)
        #     layout = [
        #     [sg.Text('Please enter your name:')],
        #     [sg.Text('Name', size=(15,1)), sg.InputText(key='Name')],
        #     [sg.Submit(), sg.Exit()]
        # ]
        #     window = sg.Window('Enter your name', layout)
        #     while True:
        #         event, values = window.read()
        #         if event == sg.WIN_CLOSED or event == 'Exit':
        #             window.close()
        #             return
                
        #         name = values['Name']
        #         row = df.loc[df['Name'] == name]
        #         if not row.empty:
        #             playerName = name
        #             window.close()
        #             return "game"
        #         else:
        #             if event == 'Submit':
        #                 playerName = name
        #                 new_record = pd.DataFrame(values, index=[0])
        #                 df = pd.concat([df, new_record], ignore_index=True)
        #                 df.to_excel(EXCEL_FILE, index=False)
        #                 sg.popup('New Data Saved!')
        #                 window.close()
        #                 return "game"

    #     if ui.button(self.surface, 320+BUTTONS_SIZES[1]*1.5, "Quit", click_sound=self.click_sound):
    #         pygame.quit()
    #         sys.exit()