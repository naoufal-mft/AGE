import pygame

class Build(pygame.sprite.Sprite):
    def __init__(self):
        super(Build, self).__init__()
        #creating a list for every building containing the 2 states
        self.wood=[]
        self.wood.append(pygame.image.load("assets/graphics/wood_0.png").convert_alpha())
        self.wood.append(pygame.image.load("assets/graphics/wood.png").convert_alpha())
        self.mining = []
        self.mining.append(pygame.image.load("assets/graphics/mining_0.png").convert_alpha())
        self.mining.append(pygame.image.load("assets/graphics/mining.png").convert_alpha())
        self.house = []
        self.house.append(pygame.image.load("assets/graphics/house_0.png").convert_alpha())
        self.house.append(pygame.image.load("assets/graphics/house.png").convert_alpha())
        self.castle = []
        self.castle.append(pygame.image.load("assets/graphics/castle_0.png").convert_alpha())
        self.castle.append(pygame.image.load("assets/graphics/castle.png").convert_alpha())

        self.index = 0 #the images will be in the 1st state of building
        self.image4 = self.house[self.index]
        self.image2 = self.mining[self.index]
        self.image3 = self.castle[self.index]
        self.image1 = self.wood[self.index]
        self.build_timer = pygame.time.get_ticks()
#change the image of building to look like a process of build
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.build_timer > 2000: #2sec

            self.index = 1
            #the images will be the final state of buildings
            self.image1 = self.wood[self.index]
            self.image2 = self.mining[self.index]
            self.image3 = self.castle[self.index]

            self.image4 = self.house[self.index]

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        # adding all the left run images to sprite array
        self.images = []
        self.images.append(pygame.image.load("assets/graphics/standing.png").convert_alpha())
        self.images.append(pygame.image.load("assets/graphics/L1.png").convert_alpha())
        self.images.append(pygame.image.load("assets/graphics/L2.png").convert_alpha())
        self.images.append(pygame.image.load("assets/graphics/L3.png").convert_alpha())
        self.images.append(pygame.image.load("assets/graphics/L4.png").convert_alpha())
        self.images.append(pygame.image.load("assets/graphics/L5.png").convert_alpha())
        self.images.append(pygame.image.load("assets/graphics/L6.png").convert_alpha())
        self.images.append(pygame.image.load("assets/graphics/L7.png").convert_alpha())
        self.images.append(pygame.image.load("assets/graphics/L8.png").convert_alpha())
        self.images.append(pygame.image.load("assets/graphics/L9.png").convert_alpha())

        #adding all the right run images to sprite array
        self.images.append(pygame.image.load("assets/graphics/R1.png").convert_alpha())
        self.images.append(pygame.image.load("assets/graphics/R2.png").convert_alpha())
        self.images.append(pygame.image.load("assets/graphics/R3.png").convert_alpha())
        self.images.append(pygame.image.load("assets/graphics/R4.png").convert_alpha())
        self.images.append(pygame.image.load("assets/graphics/R5.png").convert_alpha())
        self.images.append(pygame.image.load("assets/graphics/R6.png").convert_alpha())
        self.images.append(pygame.image.load("assets/graphics/R7.png").convert_alpha())
        self.images.append(pygame.image.load("assets/graphics/R8.png").convert_alpha())
        self.images.append(pygame.image.load("assets/graphics/R9.png").convert_alpha())

        # index value to get the image from the array
        # initially it is 0
        self.index = 0

        # now the image that we will display will be the index from the image array
        self.image = self.images[self.index]

        # creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite
        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        # when the update method is called, we will increment the index
        self.index += 1

        #if index is on the last left image
        if self.index==8:
            self.index=1

        # if the index is larger than the total images
        if self.index >= len(self.images):
            # we will make the index to 0 again
            self.index = 10

        # finally we will update the image that will be displayed
        self.image = self.images[self.index]
    def run_left(self):
        if self.index>8:
            self.index=1
        self.update()
    def run_right(self):
        if self.index<9:
            self.index=9
        self.update()
    def run_up(self):
        self.index=0
    def run_down(self):
        self.index=0