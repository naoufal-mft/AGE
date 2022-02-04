import pygame as pg
from pygame import MOUSEBUTTONDOWN


from .utils import draw_text


class Hud:

    def __init__(self, resource_manager, width, height):

        self.resource_manager = resource_manager
        self.width = width
        self.height = height

        self.hud_colour = (170, 0, 0, 175)

        # resouces hud
        self.resouces_surface = pg.Surface((width, height * 0.02), pg.SRCALPHA)
        self.resources_rect = self.resouces_surface.get_rect(topleft=(0, 0))
        self.resouces_surface.fill(self.hud_colour)

        # building hud
        #self.build_surface = pg.Surface((width * 0.25, height * 0.25), pg.SRCALPHA)
        #self.build_rect = self.build_surface.get_rect(topleft=(self.width * 0.84, self.height * 0.74))
        #self.build_surface.fill(self.hud_colour)
        self.build_surface = pg.image.load(r'assets/graphics/cadre.png').convert_alpha()
        self.build_rect = self.build_surface.get_rect(topleft=(self.width * 4, self.height * 1))

        # select hud
        self.select_surface = pg.image.load(r'assets/graphics/cadrox.png').convert_alpha()
        self.select_rect = self.select_surface.get_rect(topleft=(self.width * 0.35, self.height * 0.79))
        #self.select_surface.fill(self.hud_colour)

        self.images = self.load_images()
        self.tiles = self.create_build_hud()

        self.selected_tile = None
        self.examined_tile = None

    def create_build_hud(self):

        render_pos = [self.width * 0.83 + 10, self.height * 0.74 + 10]
        object_width = self.build_surface.get_width() // 10

        tiles = []

        for image_name, image in self.images.items():

            pos = render_pos.copy()
            image_tmp = image.copy()
            image_scale = self.scale_image(image_tmp, w=object_width)
            rect = image_scale.get_rect(topleft=pos)

            tiles.append(
                {
                    "name": image_name,
                    "icon": image_scale,
                    "image": self.images[image_name],
                    "rect": rect,
                    "affordable": True
                }
            )

            render_pos[0] += image_scale.get_width() + 10

        return tiles

    def update(self):

        mouse_pos = pg.mouse.get_pos()
        mouse_action = pg.mouse.get_pressed()

        if mouse_action[2]:
            self.selected_tile = None

        for tile in self.tiles:
            if self.resource_manager.is_affordable(tile["name"]):
                tile["affordable"] = True
            else:
                tile["affordable"] = False
            if tile["rect"].collidepoint(mouse_pos) and tile["affordable"]:
                if mouse_action[0]:
                    self.selected_tile = tile

    def draw(self, screen):
        #menu

        #screen.blit(self.settings_surface, (0, 0))

        #pos = pg.mouse.get_pos()
        #cbl= self.settings_surface.get_rect()
        #cbl.center=(0,0)

        #click = False

        #if cbl.collidepoint(pos):
           # if click:
               # print(50)
                #menu(screen)



      # resouce hud
        screen.blit(self.resouces_surface, (0, 0))
        # build hud
        screen.blit(self.build_surface, (1150,590))
        # select hud
        if self.examined_tile is not None:
            w, h = self.select_rect.width, self.select_rect.height
            screen.blit(self.select_surface, (500,590))
            img = self.examined_tile.image.copy()
            img_scale = self.scale_image(img, h=h*0.5)
            screen.blit(img_scale, (self.width * 0.35 + 10, self.height * 0.75 + 40))
            draw_text(screen, self.examined_tile.name, 40, (255, 255, 255), (self.width * 0.45 + 10, self.height * 0.72 + 40))

        for tile in self.tiles:
            icon = tile["icon"].copy()
            if not tile["affordable"]:
                icon.set_alpha(100)
            screen.blit(icon, tile["rect"].topleft)

        # resources
        pos = self.width - 400
        for resource, resource_value in self.resource_manager.resources.items():
            txt = resource + ": " + str(resource_value)
            draw_text(screen, txt, 30, (255, 255, 255), (pos, 0))
            pos += 100

       # for event in pg.event.get():
        #    if event.type == MOUSEBUTTONDOWN:
         #       if event.button == 1:
          #          click = True
           #         print(1)

    def load_images(self):

        # read images
        castle = pg.image.load("assets/graphics/castle.png")
        house = pg.image.load("assets/graphics/house.png")
        mining = pg.image.load("assets/graphics/mining.png")
        wood = pg.image.load("assets/graphics/wood.png")

        images = {
            "Castle": castle,
            "House": house,
            "Mining": mining,
            "Wood": wood,

        }

        return images

    def scale_image(self, image, w=None, h=None):

        if (w == None) and (h == None):
            pass
        elif h == None:
            scale = w / image.get_width()
            h = scale * image.get_height()
            image = pg.transform.scale(image, (int(w), int(h)))
        elif w == None:
            scale = h / image.get_height()
            w = scale * image.get_width()
            image = pg.transform.scale(image, (int(w), int(h)))
        else:
            image = pg.transform.scale(image, (int(w), int(h)))

        return image

