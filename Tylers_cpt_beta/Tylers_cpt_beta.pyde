buttons = []
player_pos = PVector(200, 560)
boss_pos = PVector(750, 400)
jump_time = 5
health = 10
boss_time = 0
enemy_hitbox = 0
enemy_health = 20
whip_time = 0
ground = False
direction = 1
position = 0
drift = 0
enemy_randomizer = 0
yspeed = 0
enemy_attack = 0
enemy_attack_time = 0
pilar_pos = 0
attack_done = True
fireball_single = 0
if_hit = False
last_attack = -1
screen = "menu"
fire_falling = []
fire_falling_right = []

while len(fire_falling_right) != 3:
    fire_falling_right.append(PVector(-50,-50))

while len(fire_falling) != 3:
    fire_falling.append(PVector(-50,-50))

for i in range(0, 233):
    buttons.append(False)

def setup():
    size(900, 700)


def draw():
    global boss_time
    global last_attack
    global pilar_pos
    global whip_hitbox
    global fire_falling
    global fire_falling_right
    global fireball_single
    global enemy_attack_time
    global enemy_hitbox
    global boss_pos
    global position
    global enemy_health
    global health
    global player_pos
    global yspeed
    global attack_done
    global buttons
    global ground
    global whip_time
    global enemy_randomizer
    global enemy_attack
    global direction
    global drift
    global screen
    global if_hit
    global jump_time
    frameRate(60)
    textSize(32)
    background(50, 50, 90)
    fill(180, 150, 90)
    rect(-1, 650, 902, 75)
    noStroke()
    if screen == "menu":
        background(0)
        fill(255)
        rect(300, 400, 300, 70)
        fill(0)
        textSize(50)
        text("Start", 390, 450)
        fill(255)
        textSize(32)
        text("""Instructions:
Move with the left and right arrow keys
Attack with z and jump with x
duck with the down arrow key

This is a very early version of the game""",100,100)
        if mouseX >= 300 and mouseX <= 600:
            if mouseY >= 400 and mouseY <= 470:
                if mousePressed == True:
                    player_pos = PVector(200, 560)
                    boss_pos = PVector(750, 400)
                    jump_time = 5
                    health = 10
                    boss_time = 0
                    enemy_hitbox = 0
                    enemy_health = 20
                    whip_time = 0
                    ground = False
                    direction = 1
                    position = 0
                    drift = 0
                    enemy_randomizer = 0
                    yspeed = 0
                    enemy_attack = 0
                    enemy_attack_time = 0
                    pilar_pos = 0
                    attack_done = True
                    fireball_single = 0
                    if_hit = False
                    last_attack = -1
                    screen = "game"

    elif screen == "game":
        if attack_done == True and enemy_attack_time + 2000 - (50 * (20 - enemy_health)) <= millis() and enemy_health > 0:
            if enemy_health <= 5:
                enemy_randomizer = random(4)
            else:
                enemy_randomizer = random(3)
            print(enemy_randomizer)
            #print(enemy_randomizer)
            #print(2000 - (50 * (20 - enemy_health)))

    #add more rng 
        if enemy_randomizer <= last_attack and enemy_randomizer >= last_attack - 1 and enemy_randomizer != 0:
            if 3 <= enemy_randomizer <= 4 and enemy_health <= 5 or 2 <= enemy_randomizer <= 3 and enemy_health > 5:
                enemy_randomizer -= 1
            else:
                enemy_randomizer += 1
        if enemy_randomizer == 0:
            True
        elif enemy_randomizer < 1:
            enemy_randomizer = 0
            enemy_attack = 1
            attack_done = False
            enemy_attack_time = millis()
        elif enemy_randomizer < 2:
            if boss_pos.x == 50:
                if random(2) <= 1:
                    fireball_single = PVector(boss_pos.x + 30, 560)
                else:
                    fireball_single = PVector(boss_pos.x +30, 620)
            else:
                if random(2) <= 1:
                    fireball_single = PVector(boss_pos.x, 560)
                else:
                    fireball_single = PVector(boss_pos.x, 620)
            enemy_randomizer = 0
            enemy_attack_time = millis()
            attack_done = False
            enemy_attack = 2
            last_attack = 2
        elif enemy_randomizer < 3:
            enemy_randomizer = 0
            enemy_attack_time = millis()
            attack_done = False
            enemy_attack = 3
        elif enemy_randomizer < 4:
            enemy_attack = 4 
            enemy_randomizer = 0
            enemy_attack_time = millis()
            attack_done = False


        if enemy_attack == 1:
            fill(200, 90, 90)
            if enemy_attack_time + 2500 >= millis():
                if boss_pos.x == 750:
                    rect(75, 450, 30, 80)
                    ellipse(90, 550, 35, 35)
                elif boss_pos.x == 50:
                    rect(750, 450, 30, 80)
                    ellipse(765, 550, 35, 35)
            if enemy_attack_time + 2500 <= millis():
                if boss_pos.x == 50:
                    boss_pos.x = 750
                elif boss_pos.x == 750:
                    boss_pos.x = 50
                enemy_attack = 0
                attack_done = True
                enemy_attack_time = millis()
                last_attack = 1

        elif enemy_attack == 2:
            fill(200, 90, 90)
            ellipse(fireball_single.x, fireball_single.y, 50, 50)
            if player_pos.x < boss_pos.x:
                fireball_single.x -= 5
            else:
                fireball_single.x += 5
            if player_pos.x + 35 > fireball_single.x - 25 and player_pos.x < fireball_single.x + 25:
                if buttons[40] == True and player_pos.y + 55 < fireball_single.y + 25 and player_pos.y + 55 > fireball_single.y - 25:
                    health -= 1
                    if_hit = True
                elif buttons[40] == False and player_pos.y < fireball_single.y + 25 and player_pos.y + 70 > fireball_single.y - 25:
                    health -= 1
                    if_hit = True
            if fireball_single.x >= 925 or fireball_single.x <= - 25 or if_hit == True:
                enemy_attack = 0
                last_attack = 2
                fireball_single = 0
                attack_done = True
                if_hit = False
                enemy_attack_time = millis()

        elif enemy_attack == 3:
            fill(200, 90, 90)
            if enemy_attack_time + 1000 > millis():
                pilar_pos = player_pos.x
                rect(pilar_pos, 420, 30, 80)
                ellipse(pilar_pos + 15, 520, 35, 35)
            elif enemy_attack_time + 2000 > millis():
                rect(pilar_pos, 420, 30, 80)
                ellipse(pilar_pos + 15, 520, 35, 35)
            elif enemy_attack_time + 3000 > millis():
                fill(255)
                rect(pilar_pos - 25, 0, 100, 650)
                if player_pos.x >= pilar_pos - 60 and player_pos.x <= pilar_pos + 75:
                    health -= 1
            elif enemy_attack_time + 3000 <= millis():
                attack_done = True
                last_attack = 3
                enemy_attack_time = millis()
                enemy_attack = 0


        elif enemy_attack == 4:
            if enemy_attack_time + 1500 > millis():
                boss_pos = PVector(random(800), 100)
                fire_falling[0] = PVector(boss_pos.x + 50, boss_pos.y + 150)
                fire_falling_right[0] = PVector(boss_pos.x + 50, boss_pos.y + 150)
            elif enemy_attack_time + 2000 > millis():
                True
            elif enemy_attack_time + 3500 > millis():
                boss_pos.x = random(800) #change it
                fire_falling[1] = PVector(boss_pos.x + 50, boss_pos.y + 150)
                fire_falling_right[1] = PVector(boss_pos.x + 50, boss_pos.y + 150)
            elif enemy_attack_time + 4000 > millis():
                True
            elif enemy_attack_time + 5500 > millis():
                boss_pos.x = random(800) #change it
                fire_falling[2] = PVector(boss_pos.x + 50, boss_pos.y + 150)
                fire_falling_right[2] = PVector(boss_pos.x + 50, boss_pos.y + 150)
            elif enemy_attack_time + 6000 > millis():
                True
            elif enemy_attack_time + 6100 > millis():
                if random(2) >= 1:
                    boss_pos = PVector(750, 400)
                else:
                    boss_pos = PVector(50, 400)
                last_attack = 4
                attack_done = True
                enemy_attack = 0
                enemy_attack_time = millis()
            #DO AN ATTACK WHERE THE ENEMY FLIES WITH SOME fireball_single CIRCLING AROUND HIM AND YOU HAVE TO JUMP OVER THEM  


        for i in fire_falling:
            if i.x < -25 or i.x > 925 or i.y == -50:
                True
            else:
                if i.y >= 620:
                    fill(200, 90, 90)
                    ellipse(i.x, i.y, 50, 50)
                    i.x -= 5
                elif i.y < 725:
                    fill(200, 90, 90)
                    ellipse(i.x, i.y, 50, 50)
                    i.y += 5
                if player_pos.x + 35 > i.x - 25 and player_pos.x < i.x + 25:
                    if buttons[40] == True and player_pos.y + 55 < i.y + 25 and player_pos.y + 55 > i.y - 25:
                        health -= 1
                        i.x = -50
                        i.y = -50
                    elif buttons[40] == False and player_pos.y < i.y + 25 and player_pos.y + 70 > i.y - 25:
                        health -= 1
                        i.x = -50
                        i.y = -50


        for e in fire_falling_right:
            if e.x < -25 or e.x > 925 or e.y == -50:
                True
            else:
                if e.y >= 620:
                    fill(200, 90, 90)
                    ellipse(e.x, e.y, 50, 50)
                    e.x += 5
                elif e.y < 725:
                    fill(200, 90, 90)
                    ellipse(e.x, e.y, 50, 50)
                    e.y += 5
                if player_pos.x + 35 > e.x - 25 and player_pos.x < e.x + 25:
                    if buttons[40] == True and player_pos.y + 55 < e.y + 25 and player_pos.y + 55 > e.y - 25:
                        health -= 1
                        e.x = -50
                        e.y = -50
                    elif buttons[40] == False and player_pos.y < e.y + 25 and player_pos.y + 70 > e.y - 25:
                        health -= 1
                        e.x = -50
                        e.y = -50



        #player healthbar
        for i in range(10):
            fill(220, 70, 70)
            i += 10 * i
            rect(30, i + 10, 20, 10)
            for e in range(10 - health):
                fill(255)
                e += 10 * e
                rect(30, e + 10, 20, 10)

        #enemy healthbar
        for i in range(20):
            fill(220, 70, 70)
            i += 10 * i
            rect(850, i + 10, 20, 10)
            for e in range(20 - enemy_health):
                fill(255)
                e += 10 * e
                rect(850, e + 10, 20, 10)

        fill(255)
        text("P", 30, 150)
        text("B", 850, 260)

        if enemy_health > 0:
            fill(0)
            rect(boss_pos.x, boss_pos.y, 100, 250)

    #super complicated player sprite and eye, and whip code
        fill(180, 230, 120)
        if buttons[40] == True:
            rect(player_pos.x, player_pos.y + 35, 40, 55)
            fill(0)
            if direction == 1:
                rect(player_pos.x + 30, player_pos.y + 35, 10, 10)
                position = 1

            else:
                rect(player_pos.x, player_pos.y + 35, 10, 10)
                position = 2
        else:
            rect(player_pos.x, player_pos.y, 40, 90)
            fill(0)
            if direction == 1:
                rect(player_pos.x + 30, player_pos.y + 10, 10, 10)
                position = 3
            else:
                rect(player_pos.x, player_pos.y + 10, 10, 10)
                position = 4

        if player_pos.y < 560:
            ground = False
        elif player_pos.y >= 560:
            ground = True
        if buttons[90] == True and millis() >= whip_time + 600:
            whip_time = millis()

        if whip_time + 600 >= millis() and millis() >= whip_time + 300:
            fill(139, 69, 19)
            if position == 1:
                rect(player_pos.x + 40, player_pos.y + 50, 50, 10)
                if player_pos.x + 90 <= boss_pos.x + 100 and player_pos.x + 90 >= boss_pos.x and millis() >= boss_time + 600 and enemy_attack != 4:
                    enemy_health -= 1
                    boss_time = millis()
            elif position == 2:
                rect(player_pos.x - 50, player_pos.y + 50, 50, 10)
                if player_pos.x - 50 <= boss_pos.x + 100 and player_pos.x - 50 >= boss_pos.x and millis() >= boss_time + 600 and enemy_attack != 4:
                    enemy_health -= 1
                    boss_time = millis()
            elif position == 3:
                rect(player_pos.x + 40, player_pos.y + 35, 50, 10)
                if player_pos.x + 90 <= boss_pos.x + 100 and player_pos.x + 90 >= boss_pos.x and millis() >= boss_time + 600 and enemy_attack != 4:
                    enemy_health -= 1
                    boss_time = millis()
            elif position == 4:
                rect(player_pos.x - 50, player_pos.y + 35, 50, 10)
                if player_pos.x - 50 <= boss_pos.x + 100 and player_pos.x - 50 >= boss_pos.x and millis() >= boss_time + 600 and enemy_attack != 4:
                    enemy_health -= 1
                    boss_time = millis()

    #player movement
        if ground == True and whip_time + 600 <= millis():
            if buttons[37] == True and buttons[40] == False:
                player_pos.x -= 3
                direction = 0
            elif buttons[39] == True and buttons[40] == False:
                player_pos.x += 3
                direction = 1

        if buttons[88] == True and ground == True and buttons[40] == False:
            if buttons[37] == True:
                drift = -3
            elif buttons[39] == True:
                drift = 3
            else:
                drift = 0
            jump_time = millis()
            player_pos.y -= 1
            ground = False

    #its okay but you should fix this tyler
        if ground == False:
            player_pos.x += drift
            player_pos.y += yspeed
            if millis() <= jump_time + 250:
                yspeed = -4
            elif millis() <= jump_time + 500:
                yspeed = -2.5
            elif millis() <= jump_time + 600:
                yspeed = -.5
            elif millis() <= jump_time + 700:
                yspeed = .5
            else:
                yspeed = 5

    #stops the player from clipping into the ground
        if player_pos.y >= 560:
            player_pos.y = 560


    #extra floor code to cover attacks
        fill(180, 150, 90)
        rect(-1, 650, 902, 75)

        if enemy_health < 1: 
            boss_pos = PVector(-50, -50)
            screen = "menu"

        if health < 1:
            True
            screen = "menu"

def keyPressed():
    global buttons
    buttons[keyCode] = True
def keyReleased():
    global buttons
    buttons[keyCode] = False
