import pygame
from sys import exit
import random
# Import Required Modules

# Create Animation Class for Wallpaper
class Animate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spriteList = []
        # Import Sprites for Animation
        firstSprite = pygame.image.load('graphics/wallpaper/roadframe_1.png')
        secondSprite = pygame.image.load('graphics/wallpaper/roadframe_2.png')
        thirdSprite = pygame.image.load('graphics/wallpaper/roadframe_3.png')
        fourthSprite = pygame.image.load('graphics/wallpaper/roadframe_4.png')
        fifthSprite = pygame.image.load('graphics/wallpaper/roadframe_5.png')
        sixthSprite = pygame.image.load('graphics/wallpaper/roadframe_6.png')
        seventhSprite = pygame.image.load('graphics/wallpaper/roadframe_7.png')
        eighthSprite = pygame.image.load('graphics/wallpaper/roadframe_8.png')
        # Append Sprites to SpriteList
        self.spriteList.append(firstSprite)
        self.spriteList.append(secondSprite)
        self.spriteList.append(thirdSprite)
        self.spriteList.append(fourthSprite)
        self.spriteList.append(fifthSprite)
        self.spriteList.append(sixthSprite)
        self.spriteList.append(seventhSprite)
        self.spriteList.append(eighthSprite)

        self.currentSprite = 0
        self.image = self.spriteList[self.currentSprite]

        self.rect = self.image.get_rect()
        self.rect.center = (480,256)
    def update(self):
        self.currentSprite += 0.5

        if self.currentSprite >= len(self.spriteList):
            self.currentSprite = 0

        self.image = self.spriteList[int(self.currentSprite)]
# Create Animation Class for Car
class AnimateCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spriteList = []
        # Import and Scale Sprites for Animation
        firstSprite = pygame.image.load('graphics/car/frame_00_delay-0.1s.png')
        firstSprite = pygame.transform.scale(firstSprite, (304,485))
        secondSprite = pygame.image.load('graphics/car/frame_01_delay-0.1s.png')
        secondSprite = pygame.transform.scale(secondSprite, (304,485))
        thirdSprite = pygame.image.load('graphics/car/frame_02_delay-0.1s.png')
        thirdSprite = pygame.transform.scale(thirdSprite, (304,485))
        fourthSprite = pygame.image.load('graphics/car/frame_03_delay-0.1s.png')
        fourthSprite = pygame.transform.scale(fourthSprite, (304,485))
        fifthSprite = pygame.image.load('graphics/car/frame_04_delay-0.1s.png')
        fifthSprite = pygame.transform.scale(fifthSprite, (304,485))
        sixthSprite = pygame.image.load('graphics/car/frame_05_delay-0.1s.png')
        sixthSprite = pygame.transform.scale(sixthSprite, (304,485))
        seventhSprite = pygame.image.load('graphics/car/frame_06_delay-0.1s.png')
        seventhSprite = pygame.transform.scale(seventhSprite, (304,485))
        eighthSprite = pygame.image.load('graphics/car/frame_07_delay-0.1s.png')
        eighthSprite = pygame.transform.scale(eighthSprite, (304,485))
        ninthSprite = pygame.image.load('graphics/car/frame_08_delay-0.1s.png')
        ninthSprite = pygame.transform.scale(ninthSprite, (304,485))
        tenthSprite = pygame.image.load('graphics/car/frame_09_delay-0.1s.png')
        tenthSprite = pygame.transform.scale(tenthSprite, (304,485))
        eleventhSprite = pygame.image.load('graphics/car/frame_10_delay-0.1s.png')
        eleventhSprite = pygame.transform.scale(eleventhSprite, (304,485))
        twelfthSprite = pygame.image.load('graphics/car/frame_11_delay-0.1s.png')
        twelfthSprite = pygame.transform.scale(twelfthSprite, (304,485))
        thirteenthSprite = pygame.image.load('graphics/car/frame_12_delay-0.1s.png')
        thirteenthSprite = pygame.transform.scale(thirteenthSprite, (304,485))
        fourteenthSprite = pygame.image.load('graphics/car/frame_13_delay-0.1s.png')
        fourteenthSprite = pygame.transform.scale(fourteenthSprite, (304,485))
        fifteenthSprite = pygame.image.load('graphics/car/frame_14_delay-0.1s.png')
        fifteenthSprite = pygame.transform.scale(fifteenthSprite, (304,485))
        sixteenthSprite = pygame.image.load('graphics/car/frame_15_delay-0.07s.png')
        sixteenthSprite = pygame.transform.scale(sixteenthSprite, (304,485))
        seventeenthSprite = pygame.image.load('graphics/car/frame_16_delay-0.03s.png')
        seventeenthSprite = pygame.transform.scale(seventeenthSprite, (304,485))
        eighteenthSprite = pygame.image.load('graphics/car/frame_17_delay-0.03s.png')
        eighteenthSprite = pygame.transform.scale(eighteenthSprite, (304,485))

        # Append Sprites to SpriteList
        self.spriteList.append(firstSprite)
        self.spriteList.append(secondSprite)
        self.spriteList.append(thirdSprite)
        self.spriteList.append(fourthSprite)
        self.spriteList.append(fifthSprite)
        self.spriteList.append(sixthSprite)
        self.spriteList.append(seventhSprite)
        self.spriteList.append(eighthSprite)
        self.spriteList.append(ninthSprite)
        self.spriteList.append(tenthSprite)
        self.spriteList.append(eleventhSprite)
        self.spriteList.append(twelfthSprite)
        self.spriteList.append(thirteenthSprite)
        self.spriteList.append(fourteenthSprite)
        self.spriteList.append(fifteenthSprite)
        self.spriteList.append(sixteenthSprite)
        self.spriteList.append(seventeenthSprite)
        self.spriteList.append(eighteenthSprite)

        self.currentSprite = 0
        self.image = self.spriteList[self.currentSprite]

        self.rect = self.image.get_rect()
        self.rect.center = (640,340)
    def update(self):
        self.currentSprite += 0.15

        if self.currentSprite >= len(self.spriteList):
            self.currentSprite = 0

        self.image = self.spriteList[int(self.currentSprite)]



    
# Initialize PyGame 
pygame.init()
# Create Window and Define Constants
windowDimensions = (960,512)
midPoint = (480,256)
screen = pygame.display.set_mode(windowDimensions)
pygame.display.set_caption('PyRacer')
clock = pygame.time.Clock()
pressedLeft = False
pressedRight = False
gameActive = False
drawTitle = True
obstacleCarInFrame = True
obstacleSize = 300
xVal = 260
yVal = 340
moving = False

# Fonts
retroFont = pygame.font.Font('fonts/font1.ttf',50) 
# ToDo - Fix Font (Get better Font)

# Create & Display Background Surface
movingSprites = pygame.sprite.Group()
animate = Animate()
animateCar = AnimateCar()
movingSprites.add(animate)
movingSprites.add(animateCar)

# Create Variables and Surfaces

titleSurf = retroFont.render('PyRacer - Press Space to Race',False,'hotpink')
titleRect = titleSurf.get_rect(center = (480,50))

winSurf = retroFont.render("You Won!",False,'black')
winRect = winSurf.get_rect(center = (480,50))

playAgainSurf = retroFont.render("Restart to play again.",False,'black')
playAgainRect = playAgainSurf.get_rect(center = (480,100))

loseSurf = retroFont.render("You're Losing!",False,'black')
loseRect = loseSurf.get_rect(center = (480,50))


# Run Game
while True:
    
    # Game Functionality
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        if e.type == pygame.KEYDOWN:
            gameActive = True
            if e.key == pygame.K_LEFT:
                pressedLeft = True
            elif e.key == pygame.K_RIGHT:
                pressedRight = True
            elif e.key == pygame.K_SPACE:
                moving = True
                xVal -= 2.5
                yVal += 2.5
                obstacleSize += 1
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_SPACE:
                moving = False
            if e.key == pygame.K_LEFT:
                pressedLeft = False
            elif e.key == pygame.K_RIGHT:
                pressedRight = False
        if e.type == pygame.KEYDOWN:
            drawTitle = False

    # Movement
    if pressedLeft:
        animateCar.rect.x -= 5
    elif pressedRight:
        animateCar.rect.x += 5
    
    # Borders
    if animateCar.rect.right >= 993:
       animateCar.rect.right = 993
    elif animateCar.rect.left <= -34:
        animateCar.rect.left = -34

    # Deploy Animations
    movingSprites.draw(screen)
    movingSprites.update()

    # Blit Surfaces and Rectangles onto Screen when game hasn't started
    if gameActive == False:
        screen.blit(titleSurf, titleRect)



  
    
    obstacleCarSurf = pygame.image.load('graphics/car/obstaclecar.png')
    obstacleCarSurf = pygame.transform.scale(obstacleCarSurf, (obstacleSize,obstacleSize))
    obstacleCarRect = obstacleCarSurf.get_rect(center = (xVal,yVal))
    screen.blit(obstacleCarSurf, obstacleCarRect)

    if obstacleCarRect.y >= 300:
        screen.blit(winSurf,winRect)
        screen.blit(playAgainSurf,playAgainRect)


    # Refresh Display and Set Framerate
    pygame.display.update()
    clock.tick(60)


