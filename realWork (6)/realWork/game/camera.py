
import pygame as pg


class Camera:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.scroll = pg.Vector2(0, 0)
        self.dx = 0
        self.dy = 0
        self.speed = 15

    def update(self):

        mouse_pos = pg.mouse.get_pos()
        keys = pg.key.get_pressed()

        # if player moves to the right
        if (keys[pg.K_RIGHT]):
            self.dx = -self.speed

        # if player moves to the right
        elif (keys[pg.K_LEFT]):
            self.dx = self.speed
        else:
            self.dx = 0
        if (keys[pg.K_DOWN]):
            self.dy = -self.speed

            # if player moves to the right
        elif (keys[pg.K_UP]):
            self.dy = self.speed
        else:
            self.dy = 0

        # x movement
       # if mouse_pos[0] > self.width * 0.97:
          #  self.dx = -self.speed
       # elif mouse_pos[0] < self.width * 0.03:
        #    self.dx = self.speed
        #else:
        #    self.dx = 0


        # (keys[pg.K_DOWN]):
         #   self.dy = -self.speed

            # if player moves to the right
        #elif (keys[pg.K_UP]):
          #  self.dy = self.speed
        #else:
         #   self.dy = 0
        # y movement
        #if mouse_pos[1] > self.height * 0.97:
        #    self.dy = -self.speed
       # elif mouse_pos[1] < self.height * 0.03:
        #    self.dy = self.speed
       # else:
        #    self.dy = 0

        # update camera scroll
        self.scroll.x += self.dx
        self.scroll.y += self.dy
