import pygame as pg
import sys


from . import mmenu, SaveLoadManager

from .world import World
from .settings import TILE_SIZE
from .utils import draw_text
from .camera import Camera
from .actions import Hud
from .resource_manager import ResourceManager
from .workers import Worker
from .animation import Build



class Game:
    #global saveloadmanager
    #saveloadmanager = SaveLoadSystem(".save", "save_data")
    def __init__(self, screen, clock):

        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.entities = []

        # ressources
        self.resource_manager = ResourceManager()
        SaveLoadManager.some.append(self.resource_manager.resources)
        # hud
        self.hud = Hud(self.resource_manager, self.width, self.height)
        self.anime=Build()

        # world
        self.world = World(self.resource_manager, self.entities, self.hud, 70, 70, self.width, self.height)
        for _ in range(10): Worker(self.world.world[25][25],self.world)
        # camera
        self.camera = Camera(self.width, self.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                #saveloadmanager.save_data(self.entities, "save")
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    #saveloadmanager.save_data(self.entities, "save")
                    self.playing=False
                #if event.key == pg.K_i:
                   # menu(self.screen)
                    #print(2)

    def update(self):
        self.camera.update()
        for e in self.entities: e.update()
        self.hud.update()
        self.world.update(self.camera)
        self.anime.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.world.draw(self.screen, self.camera)
        self.hud.draw(self.screen)

        draw_text(
            self.screen,
            'fps={}'.format(round(self.clock.get_fps())),
            25,
            (255, 255, 255),
            (10, 10)
        )

        pg.display.flip()



    #def load(self):
       # entities = saveloadmanager.load_data(["save"],[[]])
        #self.world=saveloadmanager.load_data(self.world,"save")