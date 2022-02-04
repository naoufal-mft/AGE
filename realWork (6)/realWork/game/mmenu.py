import pygame as pg
import sys

from pygame import MOUSEBUTTONDOWN
from pygame import mixer
from . import game, SaveLoadManager
from .SaveLoadManager import SaveLoadSystem

from .utils import *
from tkinter import *
from tkinter import messagebox


global saveloadmanager
saveloadmanager=SaveLoadSystem(".save","save_data")
class StartMenu:

    pg.mixer.init()
    pg.mixer.music.load('assets/graphics/sound/viking.ogg')
    pg.mixer.music.play()

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.screen_size = self.screen.get_size()

    def run(self):
        self.menu_running = True
        while self.menu_running:
            self.clock.tick(60)
            self.draw()
        return True

    global click

    def draw(self):
        global click

        interface = pg.image.load("assets/graphics/back.png")

        self.screen.fill([255,255,255])
        self.screen.blit(interface, [0, 0])
        pos = pg.mouse.get_pos()
        start = pg.image.load("assets/graphics/start button.png")
        load = pg.image.load("assets/graphics/quit.png")
        guide = pg.image.load("assets/graphics/guide.png")
        self.screen.blit(start, [200, 720])
        self.screen.blit(load, [600, 720])
        self.screen.blit(guide, [1200, 720])
        if mixer.get_num_channels() >= 1:
            # loading sound on/off icon on the screen
            sound = pg.image.load("assets/graphics/sound on.png")
            self.screen.blit(sound, [1000, 720])
            # if background music is not playing
        else:
            sound = pg.image.load("assets/graphics/sound off.png")
            self.screen.blit(sound, [1000, 720])


        cb1 = start.get_rect()
        cb2 = load.get_rect()  # repositionnement du bouton invisible
        cb3 = sound.get_rect()
        cb4 = guide.get_rect()

        cb1.topleft = (200, 720)
        cb2.topleft = (600, 720)
        cb3.topleft = (1000, 720)
        cb4.topleft = (1200, 720)

        if cb1.collidepoint(pos):
            if click:
                self.menu_running = False


        if cb2.collidepoint(pos):
            if click:
                pg.quit()
                sys.exit()

        if cb3.collidepoint(pos):
            if click:
                if mixer.get_num_channels() >= 1:
                    mixer.music.pause()
                    mixer.set_num_channels(0)
                else:
                    mixer.music.unpause()
                    mixer.set_num_channels(1)

        if cb4.collidepoint(pos):
            if click:
                Tk().wm_withdraw()  # to hide the main window
                messagebox.showinfo("Guide on how to play", "1- Our player is the explorer  \n2- the map move with the movement of player "
                                                                "\n3- Use keybord arrows to move \n4- Select a building from the bottom right so you can put it on the mapvv")

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.menu_running = False
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            click=False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            pg.display.flip()




class GameMenu:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.screen_size = self.screen.get_size()
        self.playing = True

    def run(self):
        self.menu_running = True
        while self.menu_running:
            self.clock.tick(60)
            self.update()
            self.draw()
        return self.playing

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    saveloadmanager.save_data(SaveLoadManager.some, "slot1")
                    self.menu_running = False
                if event.key == pg.K_ESCAPE:
                    saveloadmanager.save_data(SaveLoadManager.some,"slot1")
                    self.playing = False
                    self.menu_running = False

    def draw(self):

        menu_img = pg.image.load("assets/graphics/pause.png")
        menu_rec = menu_img.get_rect()
        self.screen.blit(menu_img, [280, 200])


        pg.display.flip()