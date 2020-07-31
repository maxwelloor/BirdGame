import random
import pygame

class Bird:

    bird_types = ['left', 'mid', 'right']
    bird_speed = 8
    player_score = 0
    birds = []
    birds_spawned = 0

    mid_mouse_up = True
    left_mouse_up = True
    right_mouse_up = True

    @classmethod
    def bird_spawned(cls):
        cls.birds_spawned += 1

    @classmethod
    def get_birds_spawned(cls):
        return cls.birds_spawned

    # Get mid method
    @classmethod
    def get_mid_mouse_up(cls):
        return cls.mid_mouse_up

    # Get left method
    @classmethod
    def get_left_mouse_up(cls):
        return cls.left_mouse_up

    # Get right method
    @classmethod
    def get_right_mouse_up(cls):
        return cls.right_mouse_up

    # Set mid method
    @classmethod
    def set_mid_mouse_up(cls, set_to):
        cls.mid_mouse_up = set_to

    # Set left method
    @classmethod
    def set_left_mouse_up(cls, set_to):
        cls.left_mouse_up = set_to

    # Set right method
    @classmethod
    def set_right_mouse_up(cls, set_to):
        cls.right_mouse_up = set_to

    @classmethod
    def get_player_score(cls):
        return cls.player_score

    @classmethod
    def add_player_score(cls, score):
        cls.player_score += score


    def __init__(self, screen_w, screen_h):

        # Sets the type of the bird randomly
        self.type = random.choice(self.bird_types)
        self.bird_spawned()

        # Sets the image based on the type of bird
        if self.type == 'left':
            self.img = pygame.image.load('sprites\\Left_Bird.png')
        elif self.type == 'right':
            self.img = pygame.image.load('sprites\\Right_Bird.png')
        elif self.type == 'mid':
            self.img = pygame.image.load('sprites\\Mid_Bird.png')
        
        # Sets the position based on the screen size and bird size.
        self.x = random.randint(0, screen_w - self.img.get_width() * 1.5)
        self.y = -80

        self.hitbox = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
        
        self.speed = Bird.bird_speed

        # Changes the speed based on the amount of birds that have spawned so far
        if self.birds_spawned == 25:
            Bird.bird_speed += 1
        elif self.birds_spawned == 100:
            Bird.bird_speed += 1
        elif self.birds_spawned == 150:
            Bird.bird_speed += 2

        print(self.get_birds_spawned())

        # Adds itself to the entity list
        Bird.birds.append(self)

    def destroy(self, add_score):
        Bird.birds.remove(self)
        Bird.add_player_score(add_score)

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))

    def update(self, display):
        self.hitbox = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

        self.y += self.speed

        self.draw(display)

    # Checks all birds to see if the player clicked on them
    @classmethod
    def check_for_clicks(self):

        mouse_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if mouse_buttons[0] == 0:
            Bird.set_left_mouse_up(True)
        if mouse_buttons[1] == 0:
            Bird.set_mid_mouse_up(True)
        if mouse_buttons[2] == 0:
            Bird.set_right_mouse_up(True)

        # If the player has clicked left this game loop.
        if Bird.get_left_mouse_up() and mouse_buttons[0] == 1 and mouse_buttons[1] == 0 and mouse_buttons[2] == 0:
            Bird.set_left_mouse_up(False)
            for bird in Bird.birds:
                if bird.type == 'left':
                    if bird.hitbox.collidepoint(mouse_pos):
                        bird.destroy(1)

        if Bird.get_mid_mouse_up() and mouse_buttons[1] == 1 and mouse_buttons[0] == 0 and mouse_buttons[2] == 0:
            Bird.set_mid_mouse_up(False)
            for bird in Bird.birds:
                if bird.type == 'mid':
                    if bird.hitbox.collidepoint(mouse_pos):
                        bird.destroy(1)

        if Bird.get_right_mouse_up() and mouse_buttons[2] == 1 and mouse_buttons[1] == 0 and mouse_buttons[0] == 0:
            Bird.set_right_mouse_up(False)
            for bird in Bird.birds:
                if bird.type == 'right':
                    if bird.hitbox.collidepoint(mouse_pos):
                        bird.destroy(1)
               
                

                    


                    
        