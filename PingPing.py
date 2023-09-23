from pygame import *
from random import *
init()
mixer.init()

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed):
        super().__init__()
        self.picture = image.load(sprite_image)
        self.rect = self.picture.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        self.speed = sprite_speed
        self.rect = self.picture.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
    def reset(self):
        window.blit(self.picture, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed):
        super().__init__(sprite_image, sprite_x, sprite_y, sprite_speed)
        self.picture = image.load(sprite_image)
        self.rect = self.picture.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 32:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 424:
            self.rect.y += self.speed
            
class Player1(GameSprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed):
        super().__init__(sprite_image, sprite_x, sprite_y, sprite_speed)
        self.picture = image.load(sprite_image)
        self.rect = self.picture.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 32:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 424:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed, sprite_speed_x):
        super().__init__(sprite_image, sprite_x, sprite_y, sprite_speed)
        self.picture = image.load(sprite_image)
        self.rect = self.picture.get_rect()
        self.can_change_direction_player = True
        self.can_change_direction_player1 = True
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        self.speed_y = sprite_speed
        self.speed_x = sprite_speed_x
    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y >= 600 or self.rect.y <= 0:
            self.speed_y = -self.speed_y
        if self.rect.x <= 0 or self.rect.x >= 960:
            global lost
            lost += 1
            if lost != 5:
                self.speed_x = -self.speed_x
                self.rect.x = randint(400, 520)
                self.rect.y = randint(248, 408)
            self.can_change_direction_player = True
            self.can_change_direction_player1 = True
        if sprite.collide_rect(player, ball) and self.can_change_direction_player:
            global kills
            kills += 1
            self.speed_x = -self.speed_x
            self.can_change_direction_player = False
            self.can_change_direction_player1 = True
        elif sprite.collide_rect(player1, ball) and self.can_change_direction_player1:
            kills += 1
            self.speed_x = -self.speed_x
            self.can_change_direction_player1 = False
            self.can_change_direction_player = True

window = display.set_mode((960, 656))
display.set_caption('stuka verband im angriff auf bolschewistische panzer und truppen ansammlungen')
background = transform.scale(image.load('backgr.png'), (960, 656))
background1 = transform.scale(image.load('backgr1.png'), (960, 656))

kills = 0
lost = 0

fontTxt = font.SysFont('Comic Sans', 30)
fontResult = font.SysFont('Comic Sans', 90)

ball = Ball('ball.png', 350, 250, 6, 12)
player1 = Player1('racket.png', 48, 160, 10)
player = Player('racket1.png', 848, 160, 10)

clock = time.Clock()
finish = False
FPS = 60
game = True
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    if not finish:
        window.blit(background,(0, 0))

        if kills > 14:
            finish = True
            window.blit(background1,(0, 0))
            window.blit(fontResult.render('Победа!',True,(255,255,135)), (300,250))

        if lost > 4:
            finish = True
            window.blit(background1,(0, 0))
            window.blit(fontResult.render('Поражение',True,(255,255,135)), (250,250))

        player.update()
        player.reset()
        player1.update()
        player1.reset()
        ball.update()
        ball.reset()

        window.blit(fontTxt.render('Пропущено: '+str(lost),True,(255,255,135)), (230,570))
        window.blit(fontTxt.render('Словлено: '+str(kills),True, (255,255,135)), (500,570))
        clock.tick(FPS)
        display.update()