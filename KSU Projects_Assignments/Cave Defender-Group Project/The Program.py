import pygame,sys
pygame.init()

import random # defines "random" and allows for the use of "random.randint" to randomize number selection
clock = pygame.time.Clock() # defines "clock" to all for a frame rate to be established

# code for the intructions screen
instruction_screen=pygame.display.set_mode((500,500))
inst1=pygame.font.Font(None,75)
inst1s=inst1.render("INSTRUCTIONS",True,(255,255,255))
inst2=pygame.font.Font(None,30)
inst2s=inst2.render("-Press esc to exit game!",True,(255,255,255))
inst3=pygame.font.Font(None,30)
inst3s=inst3.render("-Press spacebar to shoot fireballs at your foes!",True,(255,255,255))
inst4=pygame.font.Font(None,30)
inst4s=inst4.render("-Use the arrow keys or w,a,s,d to move the dragon!",True,(255,255,255))
inst5=pygame.font.Font(None,30)
inst5s=inst5.render("-Defend your territory from invading heroes ",True,(255,255,255))
inst6=pygame.font.Font(None,30)
inst6s=inst6.render(" by shooting fireballs at them!!!",True,(255,255,255))
inst7=pygame.font.Font(None,30)
inst12s=inst7.render("-Kill 10 heroes to win!",True,(255,255,255))
inst7s=inst7.render(" ",True,(255,255,255))
inst8s=inst7.render("Press 'm' to continue OR",True,(255,255,255))
inst9s=inst7.render("to return to this screen during the game.",True,(255,255,255))
inst10s=inst7.render(" ",True,(255,255,255))
inst11s=inst7.render("Press 'r' to restart / replay the game.",True,(255,255,255))


# screen and background objects
screen= pygame.display.set_mode((520,500))  # intializes the display and its size
screen_image = pygame.image.load("setting image.png").convert()
screen_background_image = pygame.transform.scale(screen_image, (520,500))

        # treasure image
open_treasure_image = pygame.image.load("treasure open.png")
open_treasure = pygame.transform.scale(open_treasure_image, (70,70))

        # treasure image 2
closed_treasure_image = pygame.image.load("treasure closed.png")
closed_treasure_scaled = pygame.transform.scale(closed_treasure_image, (55,60))
closed_treasure = pygame.transform.flip(closed_treasure_scaled,True,False)

        # torch image 1
torch_image = pygame.image.load("wall torch.png")
torch_scale = pygame.transform.scale(torch_image, (70,70))
torch = pygame.transform.rotate(torch_scale, 10)

        # torch image 2
torch_image2 = pygame.image.load("wall torch.png")
torch_scale2 = pygame.transform.scale(torch_image2, (62,62))
torch2 = pygame.transform.rotate(torch_scale2, 10)

# background music
music = pygame.mixer.music.load("music file.mp3")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)




# class for user character, "dragon"  /  defines the properties and attributes of the "Dragon"
class Dragon(pygame.sprite.Sprite):
    def __init__(self,color,x,y):  # the basic properties of the Dragon
        super().__init__()
        user_image = pygame.image.load("Dragon.png")   # use this to upload the file
        self.image = pygame.transform.scale(user_image, (62,62))   # use this to resize the file
        #self.image = pygame.Surface((55,40)) # creates the surface for the Dragon (its size)
        x = 465
        y = 472
        self.rect = self.image.get_rect(center=(x,y)) # allows for the spawning location to be assigned
        self.dragon_health = 1200  # initializes a counter for the "health" of the Dragon

    def move(self,screen_width,screen_height):  # when called, allows for the Dragon to be moved according to specific requirements defined below 
        keys = pygame.key.get_pressed()

        if showInstructions or game_over or game_over_win:
            # arrow controls
            if keys[pygame.K_RIGHT] and self.rect.right < 500:
                self.rect.x += 0
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= 0
            if keys[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= 0
            if keys[pygame.K_DOWN] and self.rect.bottom < 500:
                self.rect.y += 0
            # WASD controls
            if keys[pygame.K_a] and self.rect.left > 0:
                self.rect.x -= 0
            if keys[pygame.K_d] and self.rect.right < 500:
                self.rect.x += 0
            if keys[pygame.K_s] and self.rect.bottom < 500:
                self.rect.y += 0
            if keys[pygame.K_w] and self.rect.top > 0:
                self.rect.y -= 0
        else:
            # WASD controls
            if keys[pygame.K_a] and self.rect.left > 0:
                self.rect.x -= 5  # the "A" key moves the Dragon left / forward
            if keys[pygame.K_d] and self.rect.right < 500:
                self.rect.x += 5  # the "D" key moves the Dragon right / backward
            if keys[pygame.K_s] and self.rect.bottom < 500:
                self.rect.y += 5  # the "S" key mpves the Dragon down
            if keys[pygame.K_w] and self.rect.top > 0:
                self.rect.y -= 5  # the "W" key moves the Dragon up

            # arrow controls
            if keys[pygame.K_RIGHT] and self.rect.right < 500:
                self.rect.x += 5  # the RIGHT arrow key moves the user right
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= 5  # the LEFT arrow key moves the user left / forward
            if keys[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= 5  # the UP arrow key moves the user up
            if keys[pygame.K_DOWN] and self.rect.bottom < 500:
                self.rect.y += 5  # the DOWN arrow key moves the down right / backward



# class for the enemy characters, "heroes"  /  defines the properties and attributes of the "Heroes"
class Hero(pygame.sprite.Sprite):
    def __init__(self,color):
        super().__init__()
        hero_image = pygame.image.load("knight yellow.png")   # use this to upload the file
        self.image = pygame.transform.scale(hero_image, (40,40))   # use this to resize the file
        #self.image = pygame.Surface((16,16)) # creates the surface (and defines its size)
        self.rect = self.image.get_rect(center=(-10, random.randint(0,500)))  # specifies the spawning location; in this case, the y-coordinate is a randomly generated integer between 0 and 500 (the full height of the screen)
        self.hero_health = 300  # initializes a counter for the "health" of the Heroes

    def follow_dragon(self, dragon_x, dragon_y):   # when called, allows for the Heroes to move according to specific requirements defined below
        # the Heroes are programmed to follow the Dragon
        if showInstructions or game_over or game_over_win:            # stops movement while the instructions screen is visible / when the user has died
            if self.rect.x < dragon_x:
                self.rect.x += 0
            elif self.rect.x > dragon_x:
                self.rect.x -= 0
            if self.rect.y < dragon_y:
                self.rect.y += 0
            elif self.rect.y > dragon_y: 
                self.rect.y -= 0
        else:
            if self.rect.x < dragon_x:
                self.rect.x += random.randint(1,3)
            elif self.rect.x > dragon_x:
                self.rect.x -= random.randint(1,3)
            if self.rect.y < dragon_y:
                self.rect.y += random.randint(1,3)
            elif self.rect.y > dragon_y: 
                self.rect.y -= random.randint(1,3) 

# function that, when called, causes a new Hero to spawn for each Hero that is 'killed'
def spawn():
    hero = Hero((255,255,255))  # the variable "hero" is defined by the class "Hero"
    all_sprites.add(hero)  # adds each spawned hero into the group "all_sprites"
    heroes.add(hero) # adds each spawned hero in to the group "heroes"



# class for user's attack, "fireballs"
class Fireball(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        fireball_image = pygame.image.load("FireBall.png")   # use this to upload the file
        self.image = pygame.transform.scale(fireball_image, (32,32))   # use this to resize the file
        #self.image = pygame.Surface((20,20))
        self.rect = self.image.get_rect(center=(x,y))
    def update(self): # when called, assigns the direction and speed of the rect's travel
        self.rect.x -= 6.3


# create a sprite group for ALL sprites
all_sprites = pygame.sprite.Group()

# create sprite group for "heroes"
heroes = pygame.sprite.Group()

# create sprite group for "fireballs" (user's attack object)
fireballs = pygame.sprite.Group()

# initialize the sprites
dragon = Dragon((201,0,201), 185, 450)
all_sprites.add(dragon)  # adds the dragon to the group "all_sprites"

# spawn the initial heroes
for i in range(3):
    spawn()




# cover screen
cover_image = pygame.image.load("cover screen.png")
resized_cover_image = pygame.transform.scale(cover_image, (520,500))
# cover screen text
cover_text = pygame.font.SysFont("Courier New",20)

# user / dragon health bar
health_text = pygame.font.Font(None,30)


kill_count = 0  # initializes the kill count tracker
kc_font = pygame.font.Font(None,30) # initializes the font and size for the tracker to be displayed on the screen

# end of game report (high score and current score)
#current_kills_record = kill_count  # defines the player's current number of kills as the equivalent of the kill_count / tracker
ckr_font = pygame.font.Font(None,50)

record_kill_count = 0 # will track the user's "high score" or the most kills they've done in a round
rkc_font = pygame.font.Font(None,65)

# game over
game_over_image = pygame.image.load("game over image.png")
resized_game_over_image = pygame.transform.scale(game_over_image, (520,500))

victory_image = pygame.image.load("victory screen.png")
resized_victory = pygame.transform.scale(victory_image, (520,500))


running = True
show_cover = True
showInstructions = True
game_over = False  # if user dies
game_over_win = False  # if user wins

while running:
    # quit game, shoot fireballs, show instructions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:  # spacebar control for attack
                fireball = Fireball((255,128,0), dragon.rect.centerx, dragon.rect.centery)
                all_sprites.add(fireball)  # adds every spawned fireball into the "all_sprites" group
                fireballs.add(fireball) # adds every spawned fireball into the "fireballs" group
                # audio effect for fireball attack
                attack_audio = pygame.mixer.Sound("fireball attack audio.wav")
                attack_audio.set_volume(0.2)
                attack_audio.play(1,1000)
            elif event.key == pygame.K_m:
                if show_cover == False:
                    showInstructions = not showInstructions
            elif game_over: # this section of code ONLY works if the user has lost all of his/her health
                if event.key == pygame.K_r:
                    game_over = False
                    hero.hero_health = 300 # resets heroes' health
                    dragon.dragon_health = 1200 # resets user's health
                    # spawn the initial heroes
                    for i in range(3):
                        spawn()
                    # reset kill count
                    kill_count = 0
            elif game_over_win:
                if event.key == pygame.K_r:
                    game_over_win = False
                    hero.hero_health = 300 # resets heroes' health
                    dragon.dragon_health = 1200 # resets user's health
                    # spawn the initial heroes
                    for i in range(3):
                        spawn()
                    # reset kill count
                    kill_count = 0


    # updates
    dragon.move(500,500)    # calls the Dragon's move method to update user position
    fireballs.update()  # updates the entire "fireballs" group

    # The heroes follow the dragon
    for hero in heroes:
        hero.follow_dragon(dragon.rect.centerx, dragon.rect.centery)

    # collision detection / taking damage
    heroes_damage = pygame.sprite.groupcollide(fireballs,heroes,True,False)  # collision between fireball and a hero = damage to hero
       # "True" applies to removing the fireball ; False applies to keeping the hero
    for fireball_contact, hero_contact in heroes_damage.items():
        for hero in hero_contact:
            hero.hero_health -= 40
            if hero.hero_health <= 0:
                all_sprites.remove(hero)
                heroes.remove(hero)
                spawn()
    
    # hero kill count (aka, how many heroes the user/dragon has killed)
    if hero.hero_health <= 0:
        kill_count += 1  # increases the kill count for each hero that loses all its health
    kills_tracker = kc_font.render("Hero Kill Count: " + str(kill_count), True, (255,0,0))

        
    dragon_damage = pygame.sprite.spritecollide(dragon, heroes, False)   # collision between dragon and hero = damage dealt to dragon
        # "False" applies to keeping the hero
    for hero in dragon_damage:
        dragon.dragon_health -= 10
        if dragon.dragon_health <= 0:
            game_over = True
    user_health_tracker = health_text.render("Your Health: " + str(dragon.dragon_health), True, (204,0,204))


    # high score verification
    if record_kill_count < kill_count:  # if the current kill count is less than the high score, then this kill count becomes the new high score
        record_kill_count = kill_count

    if kill_count == 10:
        game_over_win = True


    screen.fill((0,0,0))
    screen.blit(screen_background_image, (0,0))


    screen.blit(open_treasure, (160,380))
    screen.blit(closed_treasure, (350,320))

    screen.blit(torch, (50,290))
    screen.blit(torch, (0,240))

    screen.blit(kills_tracker, (15,15))
    screen.blit(user_health_tracker, (15,50))

    all_sprites.draw(screen)


    # user wins
    if game_over_win:
        screen.blit(resized_victory, (0,0))
            # despawn heroes
        all_sprites.remove(hero)  # removes the heroes from the all_sprites group
        heroes.remove(hero)  # removes the heroes from the hero group
        attack_audio.set_volume(0) # prevents audio sound

    # game over
    if game_over:
        screen.blit(resized_game_over_image, (0,0))
        current_kills_report = ckr_font.render("Your Kills: " + str(kill_count), True, (0,0,255))
        high_score = rkc_font.render("Your Record: " + str(record_kill_count), True, (0,0,255))
        screen.blit(current_kills_report, (162,445))
        screen.blit(high_score, (105,397))
            # despawn heroes
        all_sprites.remove(hero)  # removes the heroes from the all_sprites group
        heroes.remove(hero)  # removes the heroes from the hero group

    
    # show instructions
    if showInstructions:
        screen.fill((0,0,0))
        screen.blit(instruction_screen, (0, 0))
        screen.blit(inst1s, (20, 20))
        screen.blit(inst2s, (20, 100))
        screen.blit(inst3s, (20, 140))
        screen.blit(inst4s, (20, 180))
        screen.blit(inst5s, (20, 220))
        screen.blit(inst6s, (20, 260))
        screen.blit(inst12s, (20,300))
        screen.blit(inst7s, (20, 320))
        screen.blit(inst8s, (20, 340))
        screen.blit(inst9s, (20, 360))
        screen.blit(inst10s, (20, 382))
        screen.blit(inst11s, (20, 400))

        
    # cover screen
    if show_cover:
        screen.blit(resized_cover_image, (0,0))
        cover_screen_text = cover_text.render("Click Anywhere to Continue", True, (255,255,255))
        screen.blit(cover_screen_text, (100,477))
        if event.type == pygame.MOUSEBUTTONDOWN:
            show_cover = False


    pygame.display.flip()
    clock.tick(60)
