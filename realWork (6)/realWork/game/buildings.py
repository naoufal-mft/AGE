import pygame as pg



class Castle:

    def __init__(self, pos,resource_manager):
        image = pg.image.load("assets/graphics/castle.png")
        self.image = image
        self.name = "Castle"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pg.time.get_ticks()
        self.counter = 0
    def update(self):
        now = pg.time.get_ticks()
        if now - self.resource_cooldown > 2000:
            self.resource_manager.resources["wood"] += 1
            self.resource_cooldown = now
        self.counter +=1



class House:

    def __init__(self, pos, resource_manager):
        image = pg.image.load("assets/graphics/house.png")
        self.image = image
        self.name = "House"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pg.time.get_ticks()

    def update(self):
        now = pg.time.get_ticks()
        if now - self.resource_cooldown > 2000:
            self.resource_manager.resources["meat"] += 1
            self.resource_cooldown = now



class Mining:

    def __init__(self, pos,resource_manager):
        image = pg.image.load("assets/graphics/mining.png")
        self.image = image
        self.name = "Mining"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pg.time.get_ticks()

    def update(self):
        now = pg.time.get_ticks()
        if now - self.resource_cooldown > 2000:
            self.resource_manager.resources["stone"] += 1
            self.resource_cooldown = now

class Wood:

    def __init__(self, pos,resource_manager):
        image = pg.image.load("assets/graphics/wood.png")
        self.image = image
        self.name = "Wood"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pg.time.get_ticks()

    def update(self):
        now = pg.time.get_ticks()
        if now - self.resource_cooldown > 2000:
            self.resource_manager.resources["wood"] += 1
            self.resource_cooldown = now


