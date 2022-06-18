@namespace
class SpriteKind:
    King = SpriteKind.create()
    Zbrojir = SpriteKind.create()
    House = SpriteKind.create()
    Tree = SpriteKind.create()
    checkpoint = SpriteKind.create()
    NPC = SpriteKind.create()
    spoustec = SpriteKind.create()
    enemyTree = SpriteKind.create()
    point = SpriteKind.create()
    drevo = SpriteKind.create()
    bobr = SpriteKind.create()
    item = SpriteKind.create()
    cursor = SpriteKind.create()
    button = SpriteKind.create()
    Kostlivec = SpriteKind.create()
    button_small = SpriteKind.create()
    neznicitelny_enemy = SpriteKind.create()
    witcher = SpriteKind.create()
    projectile_koule = SpriteKind.create()
    enemy = SpriteKind.create()
@namespace
class StrProp:
    Name = StrProp.create()
    Text = StrProp.create()


pohyb_carodeje = False
ohniva_koule: Sprite = None
pocet_netopyru = 0
obrana = False
pocet_obran = 0
myEnemy: Sprite = None
button_lvl_6: Sprite = None
button_lvl_5: Sprite = None
button_lvl_4: Sprite = None
button_lvl_3: Sprite = None
button_lvl_2: Sprite = None
button_lvl_1: Sprite = None
projectile3: Sprite = None
projectile2: Sprite = None
projectile: Sprite = None
arrow: Sprite = None
cas_konec = 0
carodej: Sprite = None
duch: Sprite = None
statusbar: StatusBarSprite = None
afterFight = False
rocks: Sprite = None
Strom: Sprite = None
House1: Sprite = None
Zbrojar: Sprite = None
StromTmavy: Sprite = None
kursor: Sprite = None
button_2: Sprite = None
button_1: Sprite = None
Lucistnik: Sprite = None
swingingSword = False
netopyr: Sprite = None
fightScene = False
Kral: Sprite = None
row = 0
speed = 0
pozice = 0
vertical = 0
swingingBow = False
cas_zacatek = 0
naBobrovi = False
bobr2: Sprite = None
time = 0
spawn_bobri = False
cislo_sloupce = 0
mec = False
luk = False
dialogSkoncen2 = False
dialogSkoncen = False
BowImage: Sprite = None
SwordImage: Sprite = None
currentLevel = 0
pozice_zbrane: List[bool] = []
mySprite: Sprite = None
enemy_position: List[List[number]] = []

mySprite = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""), SpriteKind.player)

scene.camera_follow_sprite(mySprite)
pozice_zbrane = [False, False, False, False] # smery drzeni zbrane

SwordImage = sprites.create(assets.image("""
    swordUP
"""), SpriteKind.projectile)

BowImage = sprites.create(assets.image("""
    swordUP
"""), SpriteKind.projectile)

currentLevel = -1 # level (0 = MENU)
startNextLevel()



#ovladani/
def on_up_pressed():
    if not (currentLevel == 0):
        zmena_pozice_zbrane(0)
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . . . . . . . . . . . . .
                                . . . . . . f f f f . . . . . .
                                . . . . f f e e e e f f . . . .
                                . . . f e e e f f e e e f . . .
                                . . . f f f f 2 2 f f f f . . .
                                . . f f e 2 e 2 2 e 2 e f f . .
                                . . f e 2 f 2 f f f 2 f e f . .
                                . . f f f 2 f e e 2 2 f f f . .
                                . . f e 2 f f e e 2 f e e f . .
                                . f f e f f e e e f e e e f f .
                                . f f e e e e e e e e e e f f .
                                . . . f e e e e e e e e f . . .
                                . . . e f f f f f f f f 4 e . .
                                . . . 4 f 2 2 2 2 2 e d d 4 . .
                                . . . e f f f f f f e e 4 . . .
                                . . . . f f f . . . . . . . . .
                """),
                img("""
                    . . . . . . f f f f . . . . . .
                                . . . . f f e e e e f f . . . .
                                . . . f e e e f f e e e f . . .
                                . . f f f f f 2 2 f f f f f . .
                                . . f f e 2 e 2 2 e 2 e f f . .
                                . . f e 2 f 2 f f 2 f 2 e f . .
                                . . f f f 2 2 e e 2 2 f f f . .
                                . f f e f 2 f e e f 2 f e f f .
                                . f e e f f e e e e f e e e f .
                                . . f e e e e e e e e e e f . .
                                . . . f e e e e e e e e f . . .
                                . . e 4 f f f f f f f f 4 e . .
                                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                                . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                                . . . . . f f f f f f . . . . .
                                . . . . . f f . . f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . .
                                . . . . . . f f f f . . . . . .
                                . . . . f f e e e e f f . . . .
                                . . . f e e e f f e e e f . . .
                                . . . f f f f 2 2 f f f f . . .
                                . . f f e 2 e 2 2 e 2 e f f . .
                                . . f e f 2 f f f 2 f 2 e f . .
                                . . f f f 2 2 e e f 2 f f f . .
                                . . f e e f 2 e e f f 2 e f . .
                                . f f e e e f e e e f f e f f .
                                . f f e e e e e e e e e e f f .
                                . . . f e e e e e e e e f . . .
                                . . e 4 f f f f f f f f e . . .
                                . . 4 d d e 2 2 2 2 2 f 4 . . .
                                . . . 4 e e f f f f f f e . . .
                                . . . . . . . . . f f f . . . .
                """)], 100, False)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_down_pressed():
    if not (currentLevel == 0):
        zmena_pozice_zbrane(1)
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . . . . . . . . . . . . .
                                . . . . . . f f f f . . . . . .
                                . . . . f f f 2 2 f f f . . . .
                                . . . f f f 2 2 2 2 f f f . . .
                                . . f f f e e e e e e f f f . .
                                . . f f e 2 2 2 2 2 2 e e f . .
                                . f f e 2 f f f f f f 2 e f f .
                                . f f f f f e e e e f f f f f .
                                . . f e f b f 4 4 f b f e f . .
                                . . f e 4 1 f d d f 1 4 e f . .
                                . . . f e 4 d d d d 4 e f e . .
                                . . f e f 2 2 2 2 e d d 4 e . .
                                . . e 4 f 2 2 2 2 e d d e . . .
                                . . . . f 4 4 5 5 f e e . . . .
                                . . . . f f f f f f f . . . . .
                                . . . . f f f . . . . . . . . .
                """),
                img("""
                    . . . . . . f f f f . . . . . .
                                . . . . f f f 2 2 f f f . . . .
                                . . . f f f 2 2 2 2 f f f . . .
                                . . f f f e e e e e e f f f . .
                                . . f f e 2 2 2 2 2 2 e e f . .
                                . . f e 2 f f f f f f 2 e f . .
                                . . f f f f e e e e f f f f . .
                                . f f e f b f 4 4 f b f e f f .
                                . f e e 4 1 f d d f 1 4 e e f .
                                . . f e e d d d d d d e e f . .
                                . . . f e e 4 4 4 4 e e f . . .
                                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                                . . . . . f f f f f f . . . . .
                                . . . . . f f . . f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . .
                                . . . . . . f f f f . . . . . .
                                . . . . f f f 2 2 f f f . . . .
                                . . . f f f 2 2 2 2 f f f . . .
                                . . f f f e e e e e e f f f . .
                                . . f e e 2 2 2 2 2 2 e f f . .
                                . f f e 2 f f f f f f 2 e f f .
                                . f f f f f e e e e f f f f f .
                                . . f e f b f 4 4 f b f e f . .
                                . . f e 4 1 f d d f 1 4 e f . .
                                . . e f e 4 d d d d 4 e f . . .
                                . . e 4 d d e 2 2 2 2 f e f . .
                                . . . e d d e 2 2 2 2 f 4 e . .
                                . . . . e e f 5 5 4 4 f . . . .
                                . . . . . f f f f f f f . . . .
                                . . . . . . . . . f f f . . . .
                """)], 100, False)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_right_pressed():
    if not (currentLevel == 0):
        zmena_pozice_zbrane(3)
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . . . . . . . . . . . . .
                                . . . . . . f f f f f f . . . .
                                . . . . f f e e e e f 2 f . . .
                                . . . f f e e e e f 2 2 2 f . .
                                . . . f e e e f f e e e e f . .
                                . . . f f f f e e 2 2 2 2 e f .
                                . . . f e 2 2 2 f f f f e 2 f .
                                . . f f f f f f f e e e f f f .
                                . . f f e 4 4 e b f 4 4 e e f .
                                . . f e e 4 d 4 1 f d d e f . .
                                . . . f e e e e e d d d f . . .
                                . . . . . f 4 d d e 4 e f . . .
                                . . . . . f e d d e 2 2 f . . .
                                . . . . f f f e e f 5 5 f f . .
                                . . . . f f f f f f f f f f . .
                                . . . . . f f . . . f f f . . .
                """),
                img("""
                    . . . . . . f f f f f f . . . .
                                . . . . f f e e e e f 2 f . . .
                                . . . f f e e e e f 2 2 2 f . .
                                . . . f e e e f f e e e e f . .
                                . . . f f f f e e 2 2 2 2 e f .
                                . . . f e 2 2 2 f f f f e 2 f .
                                . . f f f f f f f e e e f f f .
                                . . f f e 4 4 e b f 4 4 e e f .
                                . . f e e 4 d 4 1 f d d e f . .
                                . . . f e e e 4 d d d d f . . .
                                . . . . f f e e 4 4 4 e f . . .
                                . . . . . 4 d d e 2 2 2 f . . .
                                . . . . . e d d e 2 2 2 f . . .
                                . . . . . f e e f 4 5 5 f . . .
                                . . . . . . f f f f f f . . . .
                                . . . . . . . f f f . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . .
                                . . . . . . f f f f f f . . . .
                                . . . . f f e e e e f 2 f . . .
                                . . . f f e e e e f 2 2 2 f . .
                                . . . f e e e f f e e e e f . .
                                . . . f f f f e e 2 2 2 2 e f .
                                . . . f e 2 2 2 f f f f e 2 f .
                                . . f f f f f f f e e e f f f .
                                . . f f e 4 4 e b f 4 4 e e f .
                                . . f e e 4 d 4 1 f d d e f . .
                                . . . f e e e 4 d d d d f . . .
                                . . . . 4 d d e 4 4 4 e f . . .
                                . . . . e d d e 2 2 2 2 f . . .
                                . . . . f e e f 4 4 5 5 f f . .
                                . . . . f f f f f f f f f f . .
                                . . . . . f f . . . f f f . . .
                """)], 100, False)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_left_pressed():
    if not (currentLevel == 0):
        zmena_pozice_zbrane(2)
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . . . . . . . . . . . . .
                                . . . . f f f f f f . . . . . .
                                . . . f 2 f e e e e f f . . . .
                                . . f 2 2 2 f e e e e f f . . .
                                . . f e e e e f f e e e f . . .
                                . f e 2 2 2 2 e e f f f f . . .
                                . f 2 e f f f f 2 2 2 e f . . .
                                . f f f e e e f f f f f f f . .
                                . f e e 4 4 f b e 4 4 e f f . .
                                . . f e d d f 1 4 d 4 e e f . .
                                . . . f d d d e e e e e f . . .
                                . . . f e 4 e d d 4 f . . . . .
                                . . . f 2 2 e d d e f . . . . .
                                . . f f 5 5 f e e f f f . . . .
                                . . f f f f f f f f f f . . . .
                                . . . f f f . . . f f . . . . .
                """),
                img("""
                    . . . . f f f f f f . . . . . .
                                . . . f 2 f e e e e f f . . . .
                                . . f 2 2 2 f e e e e f f . . .
                                . . f e e e e f f e e e f . . .
                                . f e 2 2 2 2 e e f f f f . . .
                                . f 2 e f f f f 2 2 2 e f . . .
                                . f f f e e e f f f f f f f . .
                                . f e e 4 4 f b e 4 4 e f f . .
                                . . f e d d f 1 4 d 4 e e f . .
                                . . . f d d d d 4 e e e f . . .
                                . . . f e 4 4 4 e e f f . . . .
                                . . . f 2 2 2 e d d 4 . . . . .
                                . . . f 2 2 2 e d d e . . . . .
                                . . . f 5 5 4 f e e f . . . . .
                                . . . . f f f f f f . . . . . .
                                . . . . . . f f f . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . .
                                . . . . f f f f f f . . . . . .
                                . . . f 2 f e e e e f f . . . .
                                . . f 2 2 2 f e e e e f f . . .
                                . . f e e e e f f e e e f . . .
                                . f e 2 2 2 2 e e f f f f . . .
                                . f 2 e f f f f 2 2 2 e f . . .
                                . f f f e e e f f f f f f f . .
                                . f e e 4 4 f b e 4 4 e f f . .
                                . . f e d d f 1 4 d 4 e e f . .
                                . . . f d d d d 4 e e e f . . .
                                . . . f e 4 4 4 e d d 4 . . . .
                                . . . f 2 2 2 2 e d d e . . . .
                                . . f f 5 5 4 4 f e e f . . . .
                                . . f f f f f f f f f f . . . .
                                . . . f f f . . . f f . . . . .
                """)], 100, False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_b_pressed(): #mereni casu natazeni luku
    global cas_zacatek, bobr2, cas_zacatek, swingingBow, luk
    if luk:
        cas_zacatek = game.runtime()
    if currentLevel == 4 and luk:
        swingingBow = True
        if pozice_zbrane[0] == True:
            BowImage.set_image(assets.image("""
                bow
            """))
        elif pozice_zbrane[1] == True:
            BowImage.set_image(img("""
                e . . . . . . . . . . . . . e
                                    e 1 1 1 1 1 1 1 1 1 1 1 1 1 e
                                    . e . . . . . . . . . . . e .
                                    . . e . . . . . . . . . e . .
                                    . . . e . . . . . . . e . . .
                                    . . . . e . . . . . e . . . .
                                    . . . . . e . . . e . . . . .
                                    . . . . . . e e e . . . . . .
                                    . . . . . . . . . . . . . . .
                                    . . . . . . . . . . . . . . .
                                    . . . . . . . . . . . . . . .
                                    . . . . . . . . . . . . . . .
                                    . . . . . . . . . . . . . . .
                                    . . . . . . . . . . . . . . .
                                    . . . . . . . . . . . . . . .
            """))
        elif pozice_zbrane[2] == True:
            BowImage.set_image(img("""
                . . . . . . . . . . . . . e e
                                    . . . . . . . . . . . . e 1 .
                                    . . . . . . . . . . . e . 1 .
                                    . . . . . . . . . . e . . 1 .
                                    . . . . . . . . . e . . . 1 .
                                    . . . . . . . . e . . . . 1 .
                                    . . . . . . . e . . . . . 1 .
                                    . . . . . . . e . . . . . 1 .
                                    . . . . . . . e . . . . . 1 .
                                    . . . . . . . . e . . . . 1 .
                                    . . . . . . . . . e . . . 1 .
                                    . . . . . . . . . . e . . 1 .
                                    . . . . . . . . . . . e . 1 .
                                    . . . . . . . . . . . . e 1 .
                                    . . . . . . . . . . . . . e e
            """))
        else:
            BowImage.set_image(img("""
                e e . . . . . . . . . . . . .
                                    . 1 e . . . . . . . . . . . .
                                    . 1 . e . . . . . . . . . . .
                                    . 1 . . e . . . . . . . . . .
                                    . 1 . . . e . . . . . . . . .
                                    . 1 . . . . e . . . . . . . .
                                    . 1 . . . . . e . . . . . . .
                                    . 1 . . . . . e . . . . . . .
                                    . 1 . . . . . e . . . . . . .
                                    . 1 . . . . e . . . . . . . .
                                    . 1 . . . e . . . . . . . . .
                                    . 1 . . e . . . . . . . . . .
                                    . 1 . e . . . . . . . . . . .
                                    . 1 e . . . . . . . . . . . .
                                    e e . . . . . . . . . . . . .
            """))
    swingingBow = False
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed(): # seknuti mecem do ruznych smeru
    global swingingSword
    if mec == True and swingingSword == False:
        swingingSword = True
        if pozice_zbrane[0] == True:
            SwordImage.set_image(img("""
                . . . . 1 . . . . . 1 . . . .
                                    . . . . . . . . . . . . . . .
                                    . . . . . . . . . . . . . . .
                                    . . . c c c . . . . 1 . . . .
                                    . . . c d d c . . . . . . . .
                                    1 . . c d b d c . . . . . . .
                                    . . . . c d b d c . . . . . .
                                    . . . . . c d b d c . . . . .
                                    . . . . . . c d b d c . . . .
                                    . . . . . . . c d b d c . . .
                                    1 . . . 1 . . . c d b d c . .
                                    . . . . . . . . . c d d c . .
                                    . . . . . . . . . . c c a c .
                                    . . . . . . . . . . . . c c c
                                    . . . . . . . 1 . . . . . c c
            """))
        elif pozice_zbrane[1] == True:
            SwordImage.set_image(img("""
                c c . . . . . 1 . . . . . . . 1
                                    c c c . . . . . . . . . . . . .
                                    . c a c c . . . . . . . . . . .
                                    . . c d d c . . . . . . . . . .
                                    . . c d b d c . . . . . . . . 1
                                    . . . c d b d c . . . . . . . .
                                    1 . . . c d b d c . . . . . . .
                                    . . . . . c d b d c . . . . . 1
                                    . . . . . . c d b d c . . . . .
                                    . . . . . . . c d b d c . . . .
                                    . . . . . . . . c d b d c . . .
                                    . . . 1 . . . . . c d d c . . .
                                    . . . . . . . . . . c c c . . .
                                    . . . . . . . . . . . . . . . .
                                    . . . . . . . . . . . . . . . .
                                    . . . . . . . . 1 . . . . . . 1
            """))
        elif pozice_zbrane[2] == True:
            SwordImage.set_image(img("""
                1 . . . . 1 . . . . . . . 1 . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . 1 . . . .
                . . . c c c . . . . . . . . . .
                . . . c d d c . . . . . . . . .
                . . . c d b d c . . . . . . . .
                . . . . c d b d c . . . . . . .
                1 . . . . c d b d c . . . . . .
                . . . . . . c d b d c . . . . .
                . . . . . . . c d b d c . . . .
                . . . . . . . . c d b d c . . .
                . . . . . . . . . c d b d c . .
                . . . 1 . . . . . . c d d c . .
                . . . . . . . . . . . c c a c .
                . . . . . . . . . . . . . c c c
                1 . . . . . . 1 . . . . . . c c
            """))
        else:
            SwordImage.set_image(img("""
                . . . . . . . . . . 1 . . . . 1
                . . . . . . . . . . . . . . . .
                . . . 1 . . . . . . . . . . . .
                . . . . . . . . . . c c c . . .
                . . . . . . . . . c d d c . . .
                . . . . . . . . c d b d c . . .
                . . . . . . . c d b d c . . . 1
                . . . . . . c d b d c . . . . .
                1 . . . . c d b d c . . . . . .
                . . . . c d b d c . . . . . . .
                . . . c d b d c . . . . . . . .
                . . c d b d c . . . . . . . . 1
                . . c d d c . . . . . . . . . .
                . c a c c . . . . . . . . . . .
                c c c . . . . . . . . . . . . .
                c c . . . . . . 1 . . . . . . .
            """))
        pause(200)
        SwordImage.set_image(img("""
            . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
        """))
        swingingSword = False
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_b_released(): # vypocet delky casu natazeni luku
    global cas_konec, arrow, projectile, projectile2, projectile3
    if luk:
        cas_konec = game.runtime()
        BowImage.set_image(img("""
            . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
        """))
        if cas_konec - cas_zacatek > 1000:
            if pozice_zbrane[0] == True:
                arrow = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . f . . . . . . . .
                    . . . . . . f e f . . . . . . .
                    . . . . . f . e . f . . . . . .
                    . . . . . . . e . . . . . . . .
                    . . . . . . . e . . . . . . . .
                    . . . . . . . e . . . . . . . .
                    . . . . . . . e . . . . . . . .
                    . . . . . . . e . . . . . . . .
                    . . . . . . . e . . . . . . . .
                    . . . . . . . e . . . . . . . .
                    . . . . . . . e . . . . . . . .
                    . . . . . . . e . . . . . . . .
                    . . . . . . . e . . . . . . . .
                    . . . . . . 1 1 1 . . . . . . .
                    . . . . . 1 . 1 . 1 . . . . . .
                """),
                    mySprite, 0, -100)
            elif pozice_zbrane[1] == True:
                arrow = sprites.create_projectile_from_sprite(img("""
                        . . . . . 1 . 1 . 1 . . . . . .
                                            . . . . . . 1 1 1 . . . . . . .
                                            . . . . . . . e . . . . . . . .
                                            . . . . . . . e . . . . . . . .
                                            . . . . . . . e . . . . . . . .
                                            . . . . . . . e . . . . . . . .
                                            . . . . . . . e . . . . . . . .
                                            . . . . . . . e . . . . . . . .
                                            . . . . . . . e . . . . . . . .
                                            . . . . . . . e . . . . . . . .
                                            . . . . . . . e . . . . . . . .
                                            . . . . . . . e . . . . . . . .
                                            . . . . . f . e . f . . . . . .
                                            . . . . . . f e f . . . . . . .
                                            . . . . . . . f . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                    """),
                    mySprite, 0, 100)
            elif pozice_zbrane[2] == True:
                arrow = sprites.create_projectile_from_sprite(img("""
                        . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                                            . . . f . . . . . . . . . . . 1
                                            . . f . . . . . . . . . . . 1 .
                                            . f e e e e e e e e e e e e 1 1
                                            . . f . . . . . . . . . . . 1 .
                                            . . . f . . . . . . . . . . . 1
                                            . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                    """),
                    mySprite, -100, 0)
            else:
                arrow = sprites.create_projectile_from_sprite(img("""
                        . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                                            1 . . . . . . . . . . . f . . .
                                            . 1 . . . . . . . . . . . f . .
                                            1 1 e e e e e e e e e e e e f .
                                            . 1 . . . . . . . . . . . f . .
                                            1 . . . . . . . . . . . f . . .
                                            . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                    """),
                    mySprite, 100, 0)
controller.B.on_event(ControllerButtonEvent.RELEASED, on_b_released)

def on_update_pozice_zbrani(): # pozice zbrani
    if mec:
        if mySprite.vx < 0:
            SwordImage.right = mySprite.left
            SwordImage.y = mySprite.y
        elif mySprite.vx > 0:
            SwordImage.left = mySprite.right
            SwordImage.y = mySprite.y
        elif mySprite.vy > 0:
            SwordImage.top = mySprite.bottom
            SwordImage.x = mySprite.x
        elif mySprite.vy < 0:
            SwordImage.bottom = mySprite.top
            SwordImage.x = mySprite.x
    if luk:
        if mySprite.vx < 0:
            BowImage.right = mySprite.left
            BowImage.y = mySprite.y
        elif mySprite.vx > 0:
            BowImage.left = mySprite.right
            BowImage.y = mySprite.y
        elif mySprite.vy > 0:
            BowImage.top = mySprite.bottom
            BowImage.x = mySprite.x
        elif mySprite.vy < 0:
            BowImage.bottom = mySprite.top
            BowImage.x = mySprite.x
game.on_update(on_update_pozice_zbrani)
#ovladani\



#obecne funkce/
def startNextLevel(): # funkce menici levely
    global currentLevel, button_1, button_2, kursor, StromTmavy
    currentLevel += 1
    if not (currentLevel == 0):
        mySprite.set_image(img("""
            . . . . . . f f f f . . . . . .
                        . . . . f f f 2 2 f f f . . . .
                        . . . f f f 2 2 2 2 f f f . . .
                        . . f f f e e e e e e f f f . .
                        . . f f e 2 2 2 2 2 2 e e f . .
                        . . f e 2 f f f f f f 2 e f . .
                        . . f f f f e e e e f f f f . .
                        . f f e f b f 4 4 f b f e f f .
                        . f e e 4 1 f d d f 1 4 e e f .
                        . . f e e d d d d d d e e f . .
                        . . . f e e 4 4 4 4 e e f . . .
                        . . e 4 f 2 2 2 2 2 2 f 4 e . .
                        . . 4 d f 2 2 2 2 2 2 f d 4 . .
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                        . . . . . f f f f f f . . . . .
                        . . . . . f f . . f f . . . . .
        """))
        controller.move_sprite(mySprite, 80, 80)
        sprites.destroy_all_sprites_of_kind(SpriteKind.King)
        sprites.destroy_all_sprites_of_kind(SpriteKind.Zbrojir)
        sprites.destroy_all_sprites_of_kind(SpriteKind.House)
        sprites.destroy_all_sprites_of_kind(SpriteKind.Tree)
        sprites.destroy_all_sprites_of_kind(SpriteKind.checkpoint)
        sprites.destroy_all_sprites_of_kind(SpriteKind.NPC)
        sprites.destroy_all_sprites_of_kind(SpriteKind.spoustec)
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemyTree)
        sprites.destroy_all_sprites_of_kind(SpriteKind.point)
        sprites.destroy_all_sprites_of_kind(SpriteKind.drevo)
        sprites.destroy_all_sprites_of_kind(SpriteKind.bobr)
        sprites.destroy_all_sprites_of_kind(SpriteKind.item)
        sprites.destroy_all_sprites_of_kind(SpriteKind.cursor)
        sprites.destroy_all_sprites_of_kind(SpriteKind.button_small)
        sprites.destroy_all_sprites_of_kind(SpriteKind.button)
        sprites.destroy_all_sprites_of_kind(SpriteKind.Kostlivec)
        sprites.destroy_all_sprites_of_kind(SpriteKind.neznicitelny_enemy)
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
        sprites.destroy_all_sprites_of_kind(SpriteKind.witcher)
        sprites.destroy_all_sprites_of_kind(SpriteKind.projectile_koule)

    if currentLevel == 0:
        scene.set_background_image(img("""
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            66666666666666666666666666666666fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffffffffff1111fffffff1111ffff111111111fff111ffffffff111fff1111fffffffff1111ffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffffffffff111111ffff111111fff111111111fff1111fffffff111fff1111fffffffff1111ffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffffffffff1111111ff1111111fff111111111fff111111fffff111fff1111fffffffff1111ffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffffffffff1111111111111111fff111fffffffff1111111ffff111fff1111fffffffff1111ffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffffffffff1111111111111111fff111fffffffff11111111fff111fff1111fffffffff1111ffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffffffffff111f11111111f111fff11111111ffff111111111ff111fff1111fffffffff1111ffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffffffffff111ff111111ff111fff11111111ffff111f111111f111fff11111fffffff11111ffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffffffffff111ffffffffff111fff11111111ffff111ff11111f111fff111111ffffff1111fffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffffffffff111ffffffffff111fff111fffffffff111fff11111111ffff111111ffff11111fffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffffffffff111ffffffffff111fff111fffffffff111ffff1111111fffff11111fff11111ffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffffffffff111ffffffffff111fff111fffffffff111ffff1111111ffffff111111111111ffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffffffffff111ffffffffff111fff111fffffffff111fffff111111fffffff1111111111fffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffffffffff111ffffffffff111fff111111111fff111ffffff11111fffffff111111111ffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffffffffff111ffffffffff111fff111111111fff111fffffff1111fffffffff111111fffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffffffffff111ffffffffff111fff111111111fffffffffffffffffffffffffffffffffffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666661111111116666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666661111666666611116666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666611666611666666611666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666116666611666666661166666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666166666616166666666166666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666661666666166116666666116666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666661666666166616666666616666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666661666666166611666666116111166666666666666666666111661116616111166666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666661666661111111666666166616116611166111116666116161161616616616666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666661666661666661666666166616116116116616661166166111161616616616666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666661666611666661166661166611166166616616666161166111661616616616666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666661166616666666166611666616666116616616666111666161111166616616666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666166616666666666116666616666611116616666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666111666666666611166666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666661111111111116666666666666666666666666666666666666666666666666666
        """))

        button_1 = sprites.create(img("""
                .cccccccccccccccccccccccccccc...
                            .cddbbbbbbbbbbbbbbbbbbbb1bddc...
                            .cdb11bb1b111b1bbb1bbb11bbbdc...
                            .cbb1b1b1b1b1bb1b1bbb1b1bbbbc...
                            .cbb1b1b1b1b1bb1b1bb11111bbbc...
                            .cbb1bb11b111bbb1bb1bbbbb1bbc...
                            .cbbbbbbbbbbbbbbbbbbbbbbbbbbc...
                            .cbbbbbbbbbbbbbbbbbbbbbbbbbbc...
                            .cbbbbb1bb1b111bbbb1bbbbbbbbc...
                            .cbbbbb1bb1b1b1bbb1b1bbbbbbbc...
                            .cbbbbb1111b111bb1bbb1bbbbbbc...
                            .cbbbbb1bb1b11bb1111111bbbbbc...
                            .cbbbbb1bb1b1b1b1bbbbb1bbbbbc...
                            .cdbbbbbbbbbbbbbbbbbbbbbbbbdc...
                            .cddbbbbbbbbbbbbbbbbbbbbbbddc...
                            .cccccccccccccccccccccccccccc...
            """), SpriteKind.button)
        button_1.set_scale(1.75, ScaleAnchor.MIDDLE)

        button_2 = sprites.create(img("""
                .cccccccccccccccccccccccccccc...
                            .cddbbbbbbbbbbbbbbbbbbbbbbddc...
                            .cdbbbbbbbbbbbbbbbbbbbbbbbbdc...
                            .cbbbbbbbbbbbbbbbbbbbbbbbbbbc...
                            .cbbbbbbbbbbbbbbbbbbbbbbbbbbc...
                            .cb1bb11b1bbb1b11b1bb1bbb1bbc...
                            .cb1bb1bb1bbb1b1bb1bbb1b1bbbc...
                            .cb1bb11bb1b1bb11b1bbbb1bbbbc...
                            .cb1bb1bbb1b1bb1bb1bbbb1bbbbc...
                            .cb1bb1bbbb1bbb1bb1bbbb1bbbbc...
                            .cb11b11bbb1bbb11b11bbb1bbbbc...
                            .cbbbbbbbbbbbbbbbbbbbbbbbbbbc...
                            .cbbbbbbbbbbbbbbbbbbbbbbbbbbc...
                            .cdbbbbbbbbbbbbbbbbbbbbbbbbdc...
                            .cddbbbbbbbbbbbbbbbbbbbbbbddc...
                            .cccccccccccccccccccccccccccc...
            """), SpriteKind.button)
        button_2.set_scale(1.75, ScaleAnchor.MIDDLE)

        kursor = sprites.create(img("""
                . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . f . . . . . . . .
                            . . . . . . f 1 f . . . . . . .
                            . . . . . f 1 1 1 f . . . . . .
                            . . . . . f 1 1 1 1 f . . . . .
                            . . . . f 1 1 1 1 1 1 f . . . .
                            . . . . f 1 1 1 1 1 1 1 f . . .
                            . . . f 1 1 1 1 1 1 1 1 1 f . .
                            . . . f 1 1 1 1 1 1 1 1 1 1 f .
                            . . f 1 1 1 1 1 1 1 1 1 1 1 1 f
                            . . f 1 1 1 1 1 1 1 1 1 1 1 1 f
                            . f 1 1 1 1 1 1 1 1 1 1 1 1 1 f
                            . f f f f f f f f f f f f f f f
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
            """), SpriteKind.cursor)

        kursor.set_stay_in_screen(True)
        button_1.set_position(35, 65)
        button_2.set_position(120, 65)
        controller.move_sprite(kursor, 80, 80)

    elif currentLevel == 1:
        tiles.set_current_tilemap(tilemap("""level1"""))
        level1()

    elif currentLevel == 2:
        scene.set_background_image(img("""
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        """))
        tiles.set_current_tilemap(tilemap("""level2"""))
        level2()

    elif currentLevel == 3:
        tiles.set_current_tilemap(tilemap("""level0"""))
        move_lock(False)
        #sazeni stromu
        for value in tiles.get_tiles_by_type(assets.tile("""
            myTile9
        """)):
            StromTmavy = sprites.create(assets.image("""spoustec"""), SpriteKind.enemyTree)
            tiles.place_on_tile(StromTmavy, value)
        level3()

    elif currentLevel == 4:
        scene.set_background_image(img("""
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        """))
        tiles.set_current_tilemap(tilemap("""level28"""))
        level4()

    elif currentLevel == 5:
        scene.set_background_image(img("""
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        """))
        tiles.set_current_tilemap(tilemap("""level34"""))
        level5()

    elif currentLevel == 6:
        tiles.set_current_tilemap(tilemap("""level38"""))
        level6()
        
    else:
        game.over(True)

def on_overlap_cursor(sprite, otherSprite): # pri najeti v MENU kurzorem se tlacitka zvets
    otherSprite.set_scale(2, ScaleAnchor.MIDDLE)
sprites.on_overlap(SpriteKind.cursor, SpriteKind.button, on_overlap_cursor)

def move_lock(boolean: bool): # zamek pohybu postav
    if boolean:
        controller.move_sprite(mySprite, 0, 0)
    else:
        controller.move_sprite(mySprite, 80, 80)


def on_overlap_enemy(sprite, otherSprite): # odecteni zivota pri najeti na enemy
    sprite.destroy(effects.disintegrate, 200)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_overlap_enemy)

def on_overlap_neznicitelny_enemy(sprite, otherSprite): # odecteni zivota pri najeti na neznicitelny enemy
    sprite.destroy(effects.disintegrate, 200)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.neznicitelny_enemy, SpriteKind.player, on_overlap_neznicitelny_enemy)


def on_overlap_levely(sprite, otherSprite): # MENU
    global button_lvl_1, button_lvl_2, button_lvl_3, button_lvl_4, button_lvl_5, kursor, button_lvl_6

    if otherSprite == button_1 and controller.A.is_pressed():
        startNextLevel()
    elif otherSprite == button_2 and controller.A.is_pressed():
        scene.set_background_image(img("""
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            66666666666666666666666666666666fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffff111fffffff1111111ff111fffffff111ff111111ff111ffffff111ffffff111ffffff111fffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffff111fffffff1111111ff111ffffff1111ff111111ff111ffffff1111ffff1111fffff11111ffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffff111fffffff1111111ff111ffffff1111ff111111ff111ffffff1111fff11111fffff11111ffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffff111fffffff111ffffffff111fff1111fff111fffff111ffffff11111f111111fffff11111ffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffff111fffffff111ffffffff111fff111ffff111fffff111fffffff1111111111fffffff111fffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffff111fffffff1111111ffff111fff111ffff111111ff111fffffff111111111ffffffffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffff111fffffff1111111fffff111f111fffff111111ff111ffffffff1111111fffffffffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffff111fffffff1111111fffff111f111fffff111111ff111fffffffff1111fffffffffff111fffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffff111fffffff111fffffffff1111111fffff111fffff111ffffffffff111ffffffffff11111ffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffff111fffffff111ffffffffff111111fffff111fffff1111111ffffff111ffffffffff11111ffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffff111fffffff1111111ffffff111111fffff111111ff1111111ffffff111ffffffffff11111ffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffff11111111ff1111111fffffff111fffffff111111ff1111111ffffff111fffffffffff1111ffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffff11111111ff1111111fffffff111fffffff111111fffffffffffffff111fffffffffff111fffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666ffff11111111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff666666666666666666666666666666666666666
            66666666666666666666666666666666fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        """))
        sprites.destroy_all_sprites_of_kind(SpriteKind.button)
        sprites.destroy_all_sprites_of_kind(SpriteKind.cursor)
        button_lvl_1 = sprites.create(img("""
                .cccccccccccccccccccccccccccc...
                            .cddbbbbbbbbbbbbbbbbbbbbbbddc...
                            .cdbbbbbbbbbbbbbbbbbbbbbbbbdc...
                            .cbbbbbbbbbbbbbbbbbbbbbbbbbbc...
                            .cb1bbb1bbb1b1bbbbbbbbb1bbbbc...
                            .cb1bbb1bbb1b1bbbbbbbb11bbbbc...
                            .cb1bbbb1b1bb1bbbbbbb1b1bbbbc...
                            .cb1bbbb1b1bb1bbbbbb1bb1bbbbc...
                            .cb1bbbb1b1bb1bbbbbbbbb1bbbbc...
                            .cb1bbbbb1bbb1bbbbbbbbb1bbbbc...
                            .cb1bbbbb1bbb1bbbbbbbbb1bbbbc...
                            .cb1111bb1bbb1111bbbbbb1bbbbc...
                            .cbbbbbbbbbbbbbbbbbbbbbbbbbbc...
                            .cdbbbbbbbbbbbbbbbbbbbbbbbbdc...
                            .cddbbbbbbbbbbbbbbbbbbbbbbddc...
                            .cccccccccccccccccccccccccccc...
            """),
            SpriteKind.button_small)
        button_lvl_1.set_position(55, 55)
        button_lvl_2 = sprites.create(img("""
                .cccccccccccccccccccccccccccc...
                            .cddbbbbbbbbbbbbbbbbbbbbbbddc...
                            .cdbbbbbbbbbbbbbbbbbbbbbbbbdc...
                            .cbbbbbbbbbbbbbbbbbbbbbbbbbbc...
                            .cb1bbb1bbb1b1bbbbbbb11bbbbbc...
                            .cb1bbb1bbb1b1bbbbbb1bb1bbbbc...
                            .cb1bbbb1b1bb1bbbbb1bbb1bbbbc...
                            .cb1bbbb1b1bb1bbbbbbbb1bbbbbc...
                            .cb1bbbb1b1bb1bbbbbbb1bbbbbbc...
                            .cb1bbbbb1bbb1bbbbbb1bbbbbbbc...
                            .cb1bbbbb1bbb1bbbbb1bbbbbbbbc...
                            .cb1111bb1bbb1111bb111111bbbc...
                            .cbbbbbbbbbbbbbbbbbbbbbbbbbbc...
                            .cdbbbbbbbbbbbbbbbbbbbbbbbbdc...
                            .cddbbbbbbbbbbbbbbbbbbbbbbddc...
                            .cccccccccccccccccccccccccccc...
            """),
            SpriteKind.button_small)
        button_lvl_2.set_position(105, 55)
        button_lvl_3 = sprites.create(img("""
                .cccccccccccccccccccccccccccc...
                            .cddbbbbbbbbbbbbbbbbbbbbbbddc...
                            .cdbbbbbbbbbbbbbbbbbbbbbbbbdc...
                            .cbbbbbbbbbbbbbbbbbbbbbbbbbbc...
                            .cb1bbb1bbb1b1bbbbbbb111bbbbc...
                            .cb1bbb1bbb1b1bbbbbb1bbb1bbbc...
                            .cb1bbbb1b1bb1bbbbb1bbbb1bbbc...
                            .cb1bbbb1b1bb1bbbbbbbbb1bbbbc...
                            .cb1bbbb1b1bb1bbbbbbb11bbbbbc...
                            .cb1bbbbb1bbb1bbbbbbbbb11bbbc...
                            .cb1bbbbb1bbb1bbbbbbbbbb1bbbc...
                            .cb1111bb1bbb1111bbbbbbb1bbbc...
                            .cbbbbbbbbbbbbbbbbbb1111bbbbc...
                            .cdbbbbbbbbbbbbbbbbbbbbbbbbdc...
                            .cddbbbbbbbbbbbbbbbbbbbbbbddc...
                            .cccccccccccccccccccccccccccc...
            """),
            SpriteKind.button_small)
        button_lvl_3.set_position(55, 75)
        button_lvl_4 = sprites.create(img("""
                .cccccccccccccccccccccccccccc...
                            .cddbbbbbbbbbbbbbbbbbbbbbbddc...
                            .cdbbbbbbbbbbbbbbbbbbbbbbbbdc...
                            .cbbbbbbbbbbbbbbbbbbbbbbbbbbc...
                            .cb1bbb1bbb1b1bbbbbbbb1bbbbbc...
                            .cb1bbb1bbb1b1bbbbbbb1bbbbbbc...
                            .cb1bbbb1b1bb1bbbbbb1bbbbbbbc...
                            .cb1bbbb1b1bb1bbbbb1bbb1bbbbc...
                            .cb1bbbb1b1bb1bbbbb111111bbbc...
                            .cb1bbbbb1bbb1bbbbbbbbb1bbbbc...
                            .cb1bbbbb1bbb1bbbbbbbbb1bbbbc...
                            .cb1111bb1bbb1111bbbbbb1bbbbc...
                            .cbbbbbbbbbbbbbbbbbbbbbbbbbbc...
                            .cdbbbbbbbbbbbbbbbbbbbbbbbbdc...
                            .cddbbbbbbbbbbbbbbbbbbbbbbddc...
                            .cccccccccccccccccccccccccccc...
            """),
            SpriteKind.button_small)
        button_lvl_4.set_position(105, 75)
        button_lvl_5 = sprites.create(img("""
                .cccccccccccccccccccccccccccc...
                            .cddbbbbbbbbbbbbbbbbbbbbbbddc...
                            .cdbbbbbbbbbbbbbbbbbbbbbbbbdc...
                            .cbbbbbbbbbbbbbbbbbbbbbbbbbbc...
                            .cb1bbb1bbb1b1bbbbbb11111bbbc...
                            .cb1bbb1bbb1b1bbbbbb1bbbbbbbc...
                            .cb1bbbb1b1bb1bbbbbb1b11bbbbc...
                            .cb1bbbb1b1bb1bbbbbb11bb1bbbc...
                            .cb1bbbb1b1bb1bbbbbbbbbb1bbbc...
                            .cb1bbbbb1bbb1bbbbbb1bbb1bbbc...
                            .cb1bbbbb1bbb1bbbbbbb111bbbbc...
                            .cb1111bb1bbb1111bbbbbbbbbbbc...
                            .cbbbbbbbbbbbbbbbbbbbbbbbbbbc...
                            .cdbbbbbbbbbbbbbbbbbbbbbbbbdc...
                            .cddbbbbbbbbbbbbbbbbbbbbbbddc...
                            .cccccccccccccccccccccccccccc...
            """),
            SpriteKind.button_small)
        button_lvl_5.set_position(55, 95)
        button_lvl_6 = sprites.create(img("""
            .cccccccccccccccccccccccccccc...
            .cddbbbbbbbbbbbbbbbbbbbbbbddc...
            .cdbbbbbbbbbbbbbbbbbbbbbbbbdc...
            .cbbbbbbbbbbbbbbbbbbbbbbbbbbc...
            .cb1bbb1bbb1b1bbbbbbbbbb1bbbc...
            .cb1bbb1bbb1b1bbbbbbbbb1bbbbc...
            .cb1bbbb1b1bb1bbbbbbbb1bbbbbc...
            .cb1bbbb1b1bb1bbbbbbb1bbbbbbc...
            .cb1bbbb1b1bb1bbbbbb1bbb11bbc...
            .cb1bbbbb1bbb1bbbbbb1b11bb1bc...
            .cb1bbbbb1bbb1bbbbbbb1bbb1bbc...
            .cb1111bb1bbb1111bbbbb1111bbc...
            .cbbbbbbbbbbbbbbbbbbbbbbbbbbc...
            .cdbbbbbbbbbbbbbbbbbbbbbbbbdc...
            .cddbbbbbbbbbbbbbbbbbbbbbbddc...
            .cccccccccccccccccccccccccccc...
        """),
            SpriteKind.button_small)
        button_lvl_6.set_position(105, 95)
        kursor = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . f . . . . . . . .
            . . . . . . f 1 f . . . . . . .
            . . . . . f 1 1 1 f . . . . . .
            . . . . . f 1 1 1 1 f . . . . .
            . . . . f 1 1 1 1 1 1 f . . . .
            . . . . f 1 1 1 1 1 1 1 f . . .
            . . . f 1 1 1 1 1 1 1 1 1 f . .
            . . . f 1 1 1 1 1 1 1 1 1 1 f .
            . . f 1 1 1 1 1 1 1 1 1 1 1 1 f
            . . f 1 1 1 1 1 1 1 1 1 1 1 1 f
            . f 1 1 1 1 1 1 1 1 1 1 1 1 1 f
            . f f f f f f f f f f f f f f f
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
        """),
            SpriteKind.cursor)
        kursor.set_stay_in_screen(True)
        controller.move_sprite(kursor, 80, 80)
sprites.on_overlap(SpriteKind.cursor, SpriteKind.button, on_overlap_levely)

def on_overlap_levels(sprite, otherSprite):
    global currentLevel
    if otherSprite == button_lvl_1 and controller.A.is_pressed():
        currentLevel = 0
        startNextLevel()
    elif otherSprite == button_lvl_2 and controller.A.is_pressed():
        currentLevel = 1
        startNextLevel()
    elif otherSprite == button_lvl_3 and controller.A.is_pressed():
        currentLevel = 2
        startNextLevel()
    elif otherSprite == button_lvl_4 and controller.A.is_pressed():
        currentLevel = 3
        startNextLevel()
    elif otherSprite == button_lvl_5 and controller.A.is_pressed():
        currentLevel = 4
        startNextLevel()
    elif otherSprite == button_lvl_6 and controller.A.is_pressed():
        currentLevel = 5
        startNextLevel()
sprites.on_overlap(SpriteKind.cursor, SpriteKind.button_small, on_overlap_levels)


def on_overlap_enemy_zniceni(sprite, otherSprite): # zniceni enemy pri stretnuti
    otherSprite.destroy(effects.disintegrate, 200)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_overlap_enemy_zniceni)

def on_hit_wall(sprite, location): # narazeni na zed
    if currentLevel == 2:
        game.splash("Měl bych jít po cestě...")
    elif currentLevel == 4:
        game.splash("Měl bych se vrátit...")
scene.on_hit_wall(SpriteKind.player, on_hit_wall)

def on_overlap_checkpoint(sprite, otherSprite): # najeti na checkpoint
    if currentLevel == 3 and dialogSkoncen:
        startNextLevel()
    else:
        startNextLevel()
sprites.on_overlap(SpriteKind.player, SpriteKind.checkpoint, on_overlap_checkpoint)

def zmena_pozice_zbrane(num: number): # zmena aktualni pozice zbrane
    for pos in range(4):
        pozice_zbrane[pos] = False
    pozice_zbrane[num] = True

def pronasledovani(boolean: bool, Pronasledovatel: Sprite, Obet: Sprite): # pronasledovani
    if boolean:
        Pronasledovatel.follow(Obet, 90)
    else:
        Pronasledovatel.follow(Obet, 0)

def on_life_zero(): # umrti hlavni postavy
    global fightScene, currentLevel
    if currentLevel == 3:
        fightScene = False
        Lucistnik.destroy()
    if currentLevel == 4:
        game.splash("Utopil jsi se.")
    else:
        game.splash("Zemřel jsi.")
    currentLevel = currentLevel - 1
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    startNextLevel()
info.on_life_zero(on_life_zero)
#obecne funkce\



#level 1/
def level1():
    global Kral
    Kral = sprites.create(img("""
            ................
                    ................
                    ................
                    ................
                    ................
                    ...5.5.555.5.5..
                    ...5f5f555f5f5..
                    ...55555555555..
                    ....55555555ff..
                    ....fdddfbddff..
                    ....fdbbf1bfff..
                    ....1bbbbddff...
                    ....111111bdf...
                    ....111111bd....
                    ....11111ddf....
                    .....111fff.....
                    .....8ffff8.....
                    .....666666.....
                    ................
                    ................
        """), SpriteKind.King)

    tiles.place_on_random_tile(Kral, assets.tile("""
        myTile0
    """))
    game.splash("Přišel jsi za králem pro jeho nabídku.")
    game.splash("Stiskem A s ním promluvíš.")

def on_overlap_kral(sprite, location): # rozhovor s kralem
    global dialogSkoncen
    if controller.A.is_pressed() and dialogSkoncen == False:
        game.set_dialog_frame(img("""
            d d d d d d d d d d d d d d d
                        d d d d d d d d d d d d d d d
                        d d d d d d d d d d d d d d d
                        d d d d d d d d d d d d d d d
                        d d d d d d d d d d d d d d d
                        d d d d d d d d d d d d d d d
                        d d d d d d d d d d d d d d d
                        d d d d d d d d d d d d d d d
                        d d d d d d d d d d d d d d d
                        d d d d d d d d d d d d d d d
                        d d d d d d d d d d d d d d d
                        d d d d d d d d d d d d d d d
                        d d d d d d d d d d d d d d d
                        d d d d d d d d d d d d d d d
                        d d d d d d d d d d d d d d d
        """))
        game.show_long_text("KRÁL: Zdravím, jsem rád, že jsi přišel.",
            DialogLayout.BOTTOM)
        game.show_long_text("KRÁL: Mám pro tebe důležitý úkol.", DialogLayout.BOTTOM)
        game.show_long_text("KRÁL: Má dcera byla unesena a nyní je na dalekém zámku.",
            DialogLayout.BOTTOM)
        game.show_long_text("KRÁL: Onen zámek se nachází za černým lesem a řekou.",
            DialogLayout.BOTTOM)
        game.show_long_text("KRÁL: Vězní ji tam obávaný černokněžník.",
            DialogLayout.BOTTOM)
        game.show_long_text("KRÁL: Pokud ji osvobodíš, dostaneš ji za ženu",
            DialogLayout.BOTTOM)
        game.show_long_text("JÁ: Dobrá, pokusím se ji najít a přivést.",
            DialogLayout.BOTTOM)
        game.show_long_text("KRÁL: Přeji hodně štěstí a dávej na sebe pozor.",
            DialogLayout.BOTTOM)
        dialogSkoncen = True
scene.on_overlap_tile(SpriteKind.player, assets.tile("""
        koberec0
    """), on_overlap_kral)

def on_overlap_dvere(sprite, location):
    if currentLevel == 1:
        if dialogSkoncen: #pokud probehl dialog, zacne novy level
            startNextLevel()
        else: # pokud dialog neprobehl, nepusti hrace k novemu levelu
            game.splash("Král po tobě něco chce.")
            if controller.A.is_pressed():
                mySprite.set_position(25, 70)
scene.on_overlap_tile(SpriteKind.player, assets.tile("""
        dvere kral
    """), on_overlap_dvere)
#level 1\



#level 2/
def level2():
    global Zbrojar, House1, Strom, rocks
    sprites.destroy_all_sprites_of_kind(SpriteKind.King)
    #spawn kamenu, stromu, baraku..
    Zbrojar = sprites.create(assets.image("""
        Lucistnik
    """), SpriteKind.Zbrojir)
    tiles.place_on_tile(Zbrojar, tiles.get_tile_location(13, 12))
    House1 = sprites.create(img("""
            ....................e2e22e2e....................
                    .................222eee22e2e222.................
                    ..............222e22e2e22eee22e222..............
                    ...........e22e22eeee2e22e2eeee22e22e...........
                    ........eeee22e22e22e2e22e2e22e22e22eeee........
                    .....222e22e22eeee22e2e22e2e22eeee22e22e222.....
                    ...22eeee22e22e22e22eee22eee22e22e22e22eeee22...
                    4cc22e22e22eeee22e22e2e22e2e22e22eeee22e22e22cc4
                    bcbeee22e22e22e22e22e2e22e2e22e22e22e22e22eeebcb
                    4bb22e22eeee22e22eeee2e22e2eeee22e22eeee22e22bb4
                    4bb22e22e22e22eeee22e2e22e2e22eeee22e22e22e22bb4
                    4cc22eeee22e22e22e22eee22eee22e22e22e22eeee22cc4
                    bcb22e22e22eeee22e22e2e22e2e22e22eeee22e22e22bcb
                    4bbeee22e22e22e22e22e2e22e2e22e22e22e22e22eeebb4
                    4bb22e22eeee22e22e22e2e22e2e22e22e22eeee22e22bb4
                    4cc22e22e22e22e22eeee2e22e2eeee22e22e22e22e22cc4
                    bcb22eeee22e22eeee22eee22eee22eeee22e22eeee22bcb
                    4bb22e22e22eeee22e22e2e22e2e22e22eeee22e22e22bb4
                    4bbeee22e22e22e22e22e2e22e2e22e22e22e22e22eeebb4
                    4cc22e22eeee22e22e22e2e22e2e22e22e22eeee22e22cc4
                    bcb22e22e22e22e22e22eee22eee22e22e22e22e22e22bcb
                    4bb22eeee22e22e22eeeccbbbbcceee22e22e22eeee22bb4
                    4bb22e22e22e22eeeccbbbbbbbbbbcceee22e22e22e22bb4
                    4cceee22e22eeeccbbbbbccccccbbbbbcceee22e22eeecc4
                    bcb22e22eeeccbbbbbccb444444bccbbbbbcceee22e22bcb
                    4bb22e22ccbbbbbccb444444444444bccbbbbbcc22e22bb4
                    4bb22ccbbbbcccb444444444444444444bcccbbbbcc22bb4
                    4cccbbbbcccb444bccbbbbbbbbbbbbccb444bcccbbbbccc4
                    ccccccccbbbbbbbcb44444444444444bcbbbbbbbcccccccc
                    b444444444444bc444444444444444444cb444444444444b
                    bbcb444444444cb411111111111111114bc444444444bcbb
                    bbbcccccccccccd1bbbbbbbbbbbbbbbb1dcccccccccccbbb
                    bbbb444444444c11beeeeeeeeeeeeeeb11c444444444bbbb
                    bbbe2222222e4c1be4e44e44e44e44eeb1c4e2222222ebbb
                    bbbeeeeeeeee4c1be4e44e44e44e44eeb1c4eeeeeeeeebbb
                    bbbeddddddde4cbbf4e4effffffe44eebbc4edddddddebbb
                    bbbedffdffde4cbbf4effffffffff4eebbc4edffdffdebbb
                    bbbedccdccde4cbbf4effffffffffeeebbc4edccdccdebbb
                    bbbeddddddde4cbbf4eeeeeeeeeeeeeebbc4edddddddebbb
                    cbbedffdffde4cbbe4e44e44e44e44eebbc4edffdffdebbc
                    cbbedccdccde4cbbe4e44e44e44e44eebbc4edccdccdebbc
                    ccbbbbbbbbbb4cbbe4e44e44e44feeeebbc4bbbbbbbbbbcc
                    .cbb444444444cbbe4e44e44e44ffffebbc444444444bbc.
                    ..cb4eee4eee4cbbf4e44e44e44f44febbc4eee4eee4bc..
                    ...c4eee4eee4cbbf4e44e44e44effeebbc4eee4eee4c...
                    ....b44444444cbbf4e44e44e44e44eebbc44444444b....
                    .....b4eee444cbbf4e44e44e44e44eebbc444eee4b.....
                    ......bcccbbbcbbe4e44e44e44e44eebbcbbbcccb......
        """), SpriteKind.House)
    tiles.place_on_tile(House1, tiles.get_tile_location(11, 11))
    Strom = sprites.create(img("""
            .............6666...............
                    ..........666667766.6666........
                    .........677777777767776........
                    ......66667775577757777666......
                    .....677666675557557776777666...
                    .....6776777775555577777766776..
                    ...66666777777775777777766666...
                    .66667767777755757555777776776..
                    6666777677775577557555777767766.
                    .6667767777777775577777777767666
                    .c6766777677777775777777677766..
                    cc77666667777777777777777666666c
                    cc76666677777777777777777766776c
                    c6666776777777777777766677666776
                    66667766667776777767767766766666
                    ccc76677677776677766767776776ccc
                    cc7766776777677677676667767766cc
                    .666c676667677766667766666666cc.
                    .ccc66676666776666677677666cccc.
                    ...ccc77c6767666676676677666ccc.
                    ...cc676c7766676677666666c666cc.
                    ....c6cc676c6677677c66c666ccc...
                    ....ccccc6c66667667cc6ccc6ccc...
                    ......ccccc66c66c66cccccccc.....
                    .......cc.cc6c6ccc6cccc.cc......
                    ...........cccccccccc...........
                    .............feeeeee............
                    ............feeeeeefe...........
                    .........eeeeefeeeffee..........
                    ............ffffeef..ee.........
                    ...............fee..............
                    ................e...............
        """), SpriteKind.Tree)
    tiles.place_on_tile(Strom, tiles.get_tile_location(17, 17))
    rocks = sprites.create(assets.image("""
        checkpoint
    """), SpriteKind.checkpoint)
    tiles.place_on_tile(rocks, tiles.get_tile_location(13, 0))
    rocks = sprites.create(assets.image("""
        checkpoint
    """), SpriteKind.checkpoint)
    tiles.place_on_tile(rocks, tiles.get_tile_location(14, 0))
    tiles.place_on_tile(mySprite, tiles.get_tile_location(30, 22))

def on_overlap_zbrojir(sprite, location):
    global mec, dialogSkoncen
    if dialogSkoncen == False:
        game.show_long_text("ZBROJÍŘ: Počkej, počkej.", DialogLayout.BOTTOM)
        game.show_long_text("ZBROJÍŘ: Povídal mi o tobě král.", DialogLayout.BOTTOM)
        game.show_long_text("ZBROJÍŘ: Jsem místní zbrojíř a mám ti dát todle.", DialogLayout.BOTTOM)
        mec = True
        game.splash("Získal jsi meč")
        game.splash("Stiskem A mečem sekáš")
        dialogSkoncen = True
scene.on_overlap_tile(SpriteKind.player, assets.tile("""
        hlina
    """), on_overlap_zbrojir)

def on_overlap_konec_cesty(sprite, location):
    if currentLevel == 2 and dialogSkoncen == False:
        game.splash("Na něco jsem zapomněl...")

        tiles.place_on_tile(mySprite, tiles.get_tile_location(15, 8))
    elif currentLevel == 3 and dialogSkoncen == False and fightScene == False:
        pronasledovani(True, Lucistnik, mySprite)

scene.on_overlap_tile(SpriteKind.player, assets.tile("""
        active2
    """), on_overlap_konec_cesty)
#level 2\



#level 3/
def level3():
    global dialogSkoncen, mec, luk, Lucistnik, pocet_netopyru
    scene.set_background_image(img("""
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    """))
    pocet_netopyru = 0
    dialogSkoncen = False
    mec = False
    luk = False
    Lucistnik = sprites.create(img("""
            . . . . f f f f . . . . .
                    . . f f f f f f f f . . .
                    . f f f f f f c f f f . .
                    f f f f f f c c f f f c .
                    f f f c f f f f f f f c .
                    c c c f f f e e f f c c .
                    f f f f f e e f f c c f .
                    f f f b f e e f b f f f .
                    . f 4 1 f 4 4 f 1 4 f . .
                    . f e 4 4 4 4 4 4 e f . .
                    . f f f e e e e f f f . .
                    f e f b 7 7 7 7 b f e f .
                    e 4 f 7 7 7 7 7 7 f 4 e .
                    e e f 6 6 6 6 6 6 f e e .
                    . . . f f f f f f . . . .
                    . . . f f . . f f . . . .
        """), SpriteKind.NPC)
    animation.run_image_animation(Lucistnik,
        [img("""
                . . . . . f f f f f . . .
                        . . . f f f f f f f f f .
                        . . f f f c f f f f f f .
                        . . f f c f f f c f f f f
                        f f c c f f f c c f f c f
                        f f f f f e f f f f c c f
                        . f f f e e f f f f f f f
                        . . f f e e f b f e e f f
                        . . . f 4 4 f 1 e 4 e f .
                        . . . f 4 4 4 4 e f f f .
                        . . . f f e e e e e f . .
                        . . . f 7 7 7 e 4 4 e . .
                        . . . f 7 7 7 e 4 4 e . .
                        . . . f 6 6 6 f e e f . .
                        . . . . f f f f f f . . .
                        . . . . . . f f f . . . .
            """),
            img("""
                . . . . . . . . . . . . .
                        . . . . f f f f f f . . .
                        . . . f f f f f f f f f .
                        . . f f f c f f f f f f .
                        . f f f c f f f c f f f f
                        f f c c f f f c c f f c f
                        f f f f f e f f f f c c f
                        . f f f e e f f f f f f f
                        . . f f e e f b f e e f f
                        . . f f 4 4 f 1 e 4 e f .
                        . . . f 4 4 4 e e f f f .
                        . . . f f e e 4 4 e f . .
                        . . . f 7 7 e 4 4 e f . .
                        . . f f 6 6 f e e f f f .
                        . . f f f f f f f f f f .
                        . . . f f f . . . f f . .
            """),
            img("""
                . . . . . . . . . . . . .
                        . . . . f f f f f f . . .
                        . . . f f f f f f f f f .
                        . . f f f c f f f f f f .
                        . f f f c f f f c f f f f
                        f f c c f f f c c f f c f
                        f f f f f e f f f f c c f
                        . f f f e e f f f f f f f
                        . f f f e e f b f e e f f
                        . . f f 4 4 f 1 e 4 e f f
                        . . . f 4 4 4 4 e f f f .
                        . . . f f e e e e 4 4 4 .
                        . . . f 7 7 7 7 e 4 4 e .
                        . . f f 6 6 6 6 f e e f .
                        . . f f f f f f f f f f .
                        . . . f f f . . . f f . .
            """)], 100, False)
    tiles.place_on_tile(Lucistnik, tiles.get_tile_location(18, 10))
    tiles.place_on_tile(mySprite, tiles.get_tile_location(0, 7))
    
def on_overlap_cesta_level(sprite102, location62): # pusti novy level jen po dokonceni levelu
    if dialogSkoncen2 == True or currentLevel == 4:
        startNextLevel()
    elif currentLevel == 3:
        game.splash("Na něco jsem zapomněl...")
        tiles.place_on_tile(mySprite, tiles.get_tile_location(53, 9))
scene.on_overlap_tile(SpriteKind.player, assets.tile("""
        active
    """), on_overlap_cesta_level)

def on_created_netopyr(sprite):
    global pocet_netopyru
    pocet_netopyru += 1
sprites.on_created(SpriteKind.enemy, on_created_netopyr)

def on_destroyed_netopyr(sprite):
    global pocet_netopyru
    pocet_netopyru -= 1
sprites.on_destroyed(SpriteKind.enemy, on_destroyed_netopyr)

def on_overlap_lucistnik(sprite, otherSprite): # rozhovor s lucistnikem
    global dialogSkoncen2, dialogSkoncen, fightScene, mec, luk
    luk = False
    if currentLevel == 3:
        if afterFight == True and dialogSkoncen2 == False:
            pronasledovani(False, Lucistnik, mySprite)
            game.show_long_text("LUČIŠTNÍK:  Zachránil si mě", DialogLayout.BOTTOM)
            game.show_long_text("LUČIŠTNÍK:  Za to ti věnuji můj luk", DialogLayout.BOTTOM)
            game.splash("Získal jsi luk")
            luk = True
            dialogSkoncen2 = True

        elif dialogSkoncen == False:
            pronasledovani(False, Lucistnik, mySprite)
            game.show_long_text("LUČIŠTNÍK:  Bože zachraň mne!", DialogLayout.BOTTOM)
            game.show_long_text("LUČIŠTNÍK:  Šel jsem lesem a napadli mě obří netopýři", DialogLayout.BOTTOM)
            game.show_long_text("LUČIŠTNÍK:  Vylétavají ze začarovaných stromů kolem cesty", DialogLayout.BOTTOM)
            game.show_long_text("LUČIŠTNÍK:  Pokus se zničit ty modré stromy, jinak zhynem!!", DialogLayout.BOTTOM)
            game.show_long_text("JÁ:  Co?!", DialogLayout.BOTTOM)
            dialogSkoncen = True
            dialogSkoncen2 = False
            fightScene = True
            mec = True
            info.set_life(3)
            pronasledovani(False, Lucistnik, mySprite)
            pause(1500)
sprites.on_overlap(SpriteKind.NPC, SpriteKind.player, on_overlap_lucistnik)

def on_overlap_strom(sprite, otherSprite): # zniceni stromu
    animation.run_image_animation(otherSprite,
        [img("""
                ........................
                        ...........88...........
                        ..........8668..........
                        ..........8668..........
                        .........f6666f.........
                        ........f866668f........
                        .......8666666668.......
                        ......866866668668......
                        ......f8866666688f......
                        .....f886686686688f.....
                        ....f88ff88688fff88f....
                        ....ffff88fff88f8fff....
                        .....f8f8ff8ff8f88f.....
                        ....f88fff88fffff8f.....
                        ....f8ffff8fffffffff....
                        ....fff88ffffff88fff....
                        ....f868ffff8fff868f....
                        ...f666ff8f86f8ff668....
                        ..f6666866866f6686668...
                        .f66686666666866668668..
                        .ff8866666666666666866f.
                        .f8866686686866686668ff.
                        ..ff668868f88f66888688f.
                        ..f8ff88fff88ff8f88ff88f
                        .f88ff8ff8f8f88fff8fffff
                        f88ff8ff88ffff88ffff8f..
                        ffff88f88ffffff8f8ff88f.
                        .f8ffffffffffffff88ff8f.
                        .ff6fffff8ff8ff6ff8f6ff.
                        .f668f6686ff66f6668866ff
                        f668666866f666868666866f
                        fff666f6688666666f666ff.
                        ..ffff86f866688668ffff..
                        .....f8ff66f888ff8f.....
                        ......fff8fff88ffff.....
                        .........ffeeff.........
                        .........feeeef.........
                        .........feeeef.........
                        ........feeefeef........
                        ........fefeffef........
            """),
            img("""
                ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ...........88...........
                        ..........8668..........
                        ..........8668..........
                        .........f6666f.........
                        ........f866668f........
                        .......8666666668.......
                        .....f886686686688f.....
                        ....f88ff88688fff88f....
                        ....ffff88fff88f8fff....
                        .....f8f8ff8ff8f88f.....
                        ....f88fff88fffff8f.....
                        ....f868ffff8fff868f....
                        ...f666ff8f86f8ff668....
                        ..f6666866866f6686668...
                        .f66686666666866668668..
                        .ff8866666666666666866f.
                        ..f8ff88fff88ff8f88ff88f
                        .f88ff8ff8f8f88fff8fffff
                        f88ff8ff88ffff88ffff8f..
                        ffff88f88ffffff8f8ff88f.
                        .f668f6686ff66f6668866ff
                        f668666866f666868666866f
                        fff666f6688666666f666ff.
                        ......fff8fff88ffff.....
                        .........ffeeff.........
                        .........feeeef.........
                        .........feeeef.........
                        ........feeefeef........
                        ........fefeffef........
            """),
            img("""
                ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ...........66...........
                        ..........6776..........
                        ..........6776..........
                        .........877778.........
                        ........86777768........
                        .......6777777776.......
                        .....86677677677668.....
                        ....8668866766888668....
                        ....8888668886686888....
                        .....86868868868668.....
                        ....8886688888866888....
                        ....8676888868886768....
                        ...87778868678688776....
                        ..8777767767787767778...
                        .877767777777677776778..
                        ..887766768668776667668.
                        ..8688668886688686688668
                        .86688688686866888688888
                        .8688888888888888668868.
                        .8878888868868878868788.
                        .87768776788778777667788
                        877677767787776767776778
                        .....86887786668868.....
                        ......8886888668888.....
                        .........88ee88.........
                        .........feeeef.........
                        .........feeeef.........
                        ........feeefeef........
                        ........fefeffef........
            """),
            img("""
                ........................
                        ...........66...........
                        ..........6776..........
                        ..........6776..........
                        .........877778.........
                        ........86777768........
                        .......6777777776.......
                        ......677677776776......
                        ......866777777668......
                        .....86677677677668.....
                        ....8668866766888668....
                        ....8888668886686888....
                        .....86868868868668.....
                        ....866888668888868.....
                        ....8688886888888888....
                        ....8886688888866888....
                        ....8676888868886768....
                        ...87778868678688776....
                        ..8777767767787767778...
                        .877767777777677776778..
                        .8866777777777777776778.
                        .8667776776767776777688.
                        ..887766768668776667668.
                        ..8688668886688686688668
                        .86688688686866888688888
                        8668868866888866888868..
                        88886686688888868688668.
                        .8688888888888888668868.
                        .8878888868868878868788.
                        .87768776788778777667788
                        877677767787776767776778
                        88877787766777777877788.
                        ..88886786777667768888..
                        .....86887786668868.....
                        ......8886888668888.....
                        .........88ee88.........
                        .........feeeef.........
                        .........feeeef.........
                        ........feeefeef........
                        ........fefeffef........
            """)], 100, False)
    scene.camera_shake(4, 500)
    otherSprite.set_kind(SpriteKind.Tree)
    tiles.set_tile_at(otherSprite.tilemap_location(), assets.tile("""
            spawner
        """))
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemyTree, on_overlap_strom)

def on_update_interval(): # spawn netopyru
    global myEnemy, fightScene, afterFight, pocet_netopyru
    if currentLevel == 3 and fightScene and pocet_netopyru < 5:
        if len(tiles.get_tiles_by_type(assets.tile("""
            myTile9
        """))) > 0:
            myEnemy = sprites.create(img("""
                . . f f f . . . . . . . . . . .
                f f f c c . . . . . . . . f f f
                f f c c . . c c . . . f c b b c
                f f c 3 c c 3 c c f f b b b c .
                f f b 3 b c 3 b c f b b c c c .
                . c b b b b b b c f b c b c c .
                . c b b b b b b c b b c b b c .
                c b 1 b b b 1 b b b c c c b c .
                c b b b b b b b b c c c c c . .
                f b c b b b c b b b b f c . . .
                f b 1 f f f 1 b b b b f c c . .
                . f b b b b b b b b c f . . . .
                . . f b b b b b b c f . . . . .
                . . . f f f f f f f . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
            """), SpriteKind.enemy)
            animation.run_image_animation(myEnemy,
                [img("""
                        . . f f f . . . . . . . . f f f
                                            . f f c c . . . . . . f c b b c
                                            f f c c . . . . . . f c b b c .
                                            f c f c . . . . . . f b c c c .
                                            f f f c c . c c . f c b b c c .
                                            f f c 3 c c 3 c c f b c b b c .
                                            f f b 3 b c 3 b c f b c c b c .
                                            . c 1 b b b 1 b c b b c c c . .
                                            . c 1 b b b 1 b b c c c c . . .
                                            c b b b b b b b b b c c . . . .
                                            c b 1 f f 1 c b b b b f . . . .
                                            f f 1 f f 1 f b b b b f c . . .
                                            f f 2 2 2 2 f b b b b f c c . .
                                            . f 2 2 2 2 b b b b c f . . . .
                                            . . f b b b b b b c f . . . . .
                                            . . . f f f f f f f . . . . . .
                    """),
                    img("""
                        . . f f f . . . . . . . . . . .
                                            f f f c c . . . . . . . . f f f
                                            f f c c c . c c . . . f c b b c
                                            f f c 3 c c 3 c c f f b b b c .
                                            f f c 3 b c 3 b c f b b c c c .
                                            f c b b b b b b c f b c b c c .
                                            c c 1 b b b 1 b c b b c b b c .
                                            c b b b b b b b b b c c c b c .
                                            c b 1 f f 1 c b b c c c c c . .
                                            c f 1 f f 1 f b b b b f c . . .
                                            f f f f f f f b b b b f c . . .
                                            f f 2 2 2 2 f b b b b f c c . .
                                            . f 2 2 2 2 2 b b b c f . . . .
                                            . . f 2 2 2 b b b c f . . . . .
                                            . . . f f f f f f f . . . . . .
                                            . . . . . . . . . . . . . . . .
                    """),
                    img("""
                        . . . . . . . . . . . . . . . .
                                            . . . . . . . . . . . . . . . .
                                            . . . c c . c c . . . . . . . .
                                            . . f 3 c c 3 c c c . . . . . .
                                            . f c 3 b c 3 b c c c . . . . .
                                            f c b b b b b b b b f f . . . .
                                            c c 1 b b b 1 b b b f f . . . .
                                            c b b b b b b b b c f f f . . .
                                            c b 1 f f 1 c b b f f f f . . .
                                            f f 1 f f 1 f b c c b b b . . .
                                            f f f f f f f b f c c c c . . .
                                            f f 2 2 2 2 f b f b b c c c . .
                                            . f 2 2 2 2 2 b c c b b c . . .
                                            . . f 2 2 2 b f f c c b b c . .
                                            . . . f f f f f f f c c c c c .
                                            . . . . . . . . . . . . c c c c
                    """),
                    img("""
                        . f f f . . . . . . . . f f f .
                                            f f c . . . . . . . f c b b c .
                                            f c c . . . . . . f c b b c . .
                                            c f . . . . . . . f b c c c . .
                                            c f f . . . . . f f b b c c . .
                                            f f f c c . c c f b c b b c . .
                                            f f f c c c c c f b c c b c . .
                                            . f c 3 c c 3 b c b c c c . . .
                                            . c b 3 b c 3 b b c c c c . . .
                                            c c b b b b b b b b c c . . . .
                                            c 1 1 b b b 1 1 b b b f c . . .
                                            f b b b b b b b b b b f c c . .
                                            f b c b b b c b b b b f . . . .
                                            . f 1 f f f 1 b b b c f . . . .
                                            . . f b b b b b b c f . . . . .
                                            . . . f f f f f f f . . . . . .
                    """)], 250, True)
            tiles.place_on_tile(myEnemy, tiles.get_tiles_by_type(assets.tile("""
                    myTile9
                """))._pick_random())
            myEnemy.follow(mySprite, randint(20, 40))

        else:
            fightScene = False
            pronasledovani(True, Lucistnik, mySprite)
            afterFight = True
game.on_update_interval(3000, on_update_interval)
#level 3\



#level 4/
def level4():
    global dialogSkoncen, dialogSkoncen2, luk, mec, cislo_sloupce, spawn_bobri, time, bobr2
    info.set_life(3)
    dialogSkoncen = False
    dialogSkoncen2 = False
    tiles.place_on_tile(mySprite, tiles.get_tile_location(0, 7))
    luk = False
    mec = False
    cislo_sloupce = -1
    spawn_bobri = False
    time = 3000
    bobr2 = sprites.create(assets.image("""
        bobr
    """), SpriteKind.bobr)

def on_overlap_molo(sprite2, location2): # slapnuti na molo
    global dialogSkoncen, spawn_bobri, dialogSkoncen2, luk
    if currentLevel == 2:
        dialogSkoncen = False

    if currentLevel == 4 and dialogSkoncen == False:
        dialogSkoncen = True
        game.show_long_text("Sakra, neumím plavat. Musím nějak přebrodit řeku", DialogLayout.BOTTOM)
        spawn_bobri = True
        zmena_sloupce()

    if currentLevel == 4 and (bobr2.tile_kind_at(TileDirection.LEFT, assets.tile("""
        wood
    """)) or bobr2.tile_kind_at(TileDirection.RIGHT, assets.tile("""
        wood
    """))):
        if dialogSkoncen2 == False:
            game.show_long_text("Proč tu sviští bobři?!", DialogLayout.BOTTOM)
            game.splash("Podržením natáhneš luk, puštěním s ním vystřelíš.")
            luk = True
            dialogSkoncen2 = True
scene.on_overlap_tile(SpriteKind.player, assets.tile("""
        wood
    """), on_overlap_molo)

def on_overlap_voda(sprite3, location3): # pri najeti na vodu hrac zemre
    if naBobrovi == False:
        info.set_life(0)
scene.on_overlap_tile(SpriteKind.player, assets.tile("""
        myTile12
    """), on_overlap_voda)

def on_update_pozice_hrace(): # hlida, zda je hrac na bobrovi/molu nebo na vode
    global naBobrovi
    if currentLevel == 4:
        if tiles.tile_at_location_equals(mySprite.tilemap_location(), assets.tile("""
                myTile11
            """)) or tiles.tile_at_location_equals(mySprite.tilemap_location(), assets.tile("""
            wood
        """)):
            naBobrovi = True
        elif tiles.tile_at_location_equals(mySprite.tilemap_location(), sprites.castle.tile_grass1) or tiles.tile_at_location_equals(mySprite.tilemap_location(), sprites.castle.tile_path4):
            naBobrovi = True
        else:
            naBobrovi = False
game.on_update(on_update_pozice_hrace)

def on_forever(): # spawn bobru
    global bobr2, cas_zacatek, swingingBow, luk
    if controller.B.is_pressed() and luk== True and swingingBow == False and not currentLevel == 4:
        swingingBow = True
        if pozice_zbrane[0] == True:
            BowImage.set_image(assets.image("""
                bow
            """))
        elif pozice_zbrane[1] == True:
            BowImage.set_image(img("""
                e . . . . . . . . . . . . . e
                                    e 1 1 1 1 1 1 1 1 1 1 1 1 1 e
                                    . e . . . . . . . . . . . e .
                                    . . e . . . . . . . . . e . .
                                    . . . e . . . . . . . e . . .
                                    . . . . e . . . . . e . . . .
                                    . . . . . e . . . e . . . . .
                                    . . . . . . e e e . . . . . .
                                    . . . . . . . . . . . . . . .
                                    . . . . . . . . . . . . . . .
                                    . . . . . . . . . . . . . . .
                                    . . . . . . . . . . . . . . .
                                    . . . . . . . . . . . . . . .
                                    . . . . . . . . . . . . . . .
                                    . . . . . . . . . . . . . . .
            """))
        elif pozice_zbrane[2] == True:
            BowImage.set_image(img("""
                . . . . . . . . . . . . . e e
                                    . . . . . . . . . . . . e 1 .
                                    . . . . . . . . . . . e . 1 .
                                    . . . . . . . . . . e . . 1 .
                                    . . . . . . . . . e . . . 1 .
                                    . . . . . . . . e . . . . 1 .
                                    . . . . . . . e . . . . . 1 .
                                    . . . . . . . e . . . . . 1 .
                                    . . . . . . . e . . . . . 1 .
                                    . . . . . . . . e . . . . 1 .
                                    . . . . . . . . . e . . . 1 .
                                    . . . . . . . . . . e . . 1 .
                                    . . . . . . . . . . . e . 1 .
                                    . . . . . . . . . . . . e 1 .
                                    . . . . . . . . . . . . . e e
            """))
        else:
            BowImage.set_image(img("""
                e e . . . . . . . . . . . . .
                                    . 1 e . . . . . . . . . . . .
                                    . 1 . e . . . . . . . . . . .
                                    . 1 . . e . . . . . . . . . .
                                    . 1 . . . e . . . . . . . . .
                                    . 1 . . . . e . . . . . . . .
                                    . 1 . . . . . e . . . . . . .
                                    . 1 . . . . . e . . . . . . .
                                    . 1 . . . . . e . . . . . . .
                                    . 1 . . . . e . . . . . . . .
                                    . 1 . . . e . . . . . . . . .
                                    . 1 . . e . . . . . . . . . .
                                    . 1 . e . . . . . . . . . . .
                                    . 1 e . . . . . . . . . . . .
                                    e e . . . . . . . . . . . . .
            """))
        swingingBow = False

    if currentLevel == 4 and spawn_bobri:
        zmena_bobra()
        bobr2 = sprites.create(assets.image("""bobr"""), SpriteKind.bobr)
        tiles.place_on_tile(bobr2, tiles.get_tile_location(cislo_sloupce + 10, row))
        bobr2.ay = speed
        bobr2.set_flag(SpriteFlag.DESTROY_ON_WALL, True)
        pause(time)
    elif currentLevel == 0 and not (kursor.overlaps_with(button_1)): # zmenseni tlacitek v menu
        if not (kursor.overlaps_with(button_2)):
            button_1.set_scale(1.75, ScaleAnchor.MIDDLE)
            button_2.set_scale(1.75, ScaleAnchor.MIDDLE)
forever(on_forever)


def zmena_bobra(): # meni rychlost a smer bobra
    global time, vertical, speed, row
    time = randint(2500, 5000)
    vertical = randint(0, 1)
    if vertical == 0:
        speed = randint(150, 400)
        row = 0
    else:
        speed = randint(-150, -400)
        row = 15

def zmena_sloupce(): # meni aktualni sloupec bobru
    global cislo_sloupce
    if cislo_sloupce == 9:
        sprites.destroy_all_sprites_of_kind(SpriteKind.bobr)
        spawn_bobri = False
    else:
        cislo_sloupce = cislo_sloupce + 1

def on_overlap_zniceni_bobra(sprite, otherSprite): # znici bobra pri zastreleni sipem
    otherSprite.destroy(effects.cool_radial, 1)
    sprite.destroy()
    tiles.set_tile_at(otherSprite.tilemap_location(), assets.tile("""
            myTile11
        """))
    if otherSprite.tile_kind_at(TileDirection.LEFT, assets.tile("""
        myTile11
    """)) or otherSprite.tile_kind_at(TileDirection.LEFT, assets.tile("""
        wood
    """)):
        sprites.destroy_all_sprites_of_kind(SpriteKind.bobr)
        zmena_sloupce()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.bobr, on_overlap_zniceni_bobra)
#level 4\



#level 5/
def level5():
    global dialogSkoncen, dialogSkoncen2, fightScene, pohyb_carodeje, luk, mec, pocet_obran
    pohyb_carodeje = False
    pocet_obran = 0
    dialogSkoncen = False
    dialogSkoncen2 = False
    tiles.place_on_tile(mySprite, tiles.get_tile_location(0, 8))
    fightScene = False
    luk = True
    mec = True

def on_overlap_brana(sprite, location): # zavrena brana
    if currentLevel == 5:
        game.splash("Brána je zařená, musím najít jiný vchod")
        tiles.place_on_tile(mySprite, tiles.get_tile_location(19, 8))
scene.on_overlap_tile(SpriteKind.player, assets.tile("""
        active2
    """), on_overlap_brana)

def on_overlap_strop(sprite, location): # spadnuti stropu
    if currentLevel == 5:
        game.splash("Bohužel, spadl na tebe strop")
        game.splash("Zemřel jsi.")
        info.set_life(0)
scene.on_overlap_tile(SpriteKind.player, assets.tile("""
        active_black
    """), on_overlap_strop)

def on_overlap_treasure(sprite, location): # ziskani zivota navic z truhly
    global currentLevel
    if currentLevel == 5:
        tiles.set_tile_at(location, sprites.dungeon.chest_open)
        effects.hearts.start_screen_effect(500)
        game.splash("Získal jsi život navíc")
        info.change_life_by(1)
scene.on_overlap_tile(SpriteKind.player, sprites.dungeon.chest_closed, on_overlap_treasure)

def set_duchove(num: number, num2: number): # funkce nastavujici duchy
    global duch
    duch = sprites.create(img("""
            ........................
                    ........................
                    ........................
                    ........................
                    ..........ffff..........
                    ........ff1111ff........
                    .......fb111111bf.......
                    .......f11111111f.......
                    ......fd11111111df......
                    ......fd11111111df......
                    ......fddd1111dddf......
                    ......fbdbfddfbdbf......
                    ......fcdcf11fcdcf......
                    .......fb111111bf.......
                    ......fffcdb1bdffff.....
                    ....fc111cbfbfc111cf....
                    ....f1b1b1ffff1b1b1f....
                    ....fbfbffffffbfbfbf....
                    .........ffffff.........
                    ...........fff..........
                    ........................
                    ........................
                    ........................
                    ........................
        """), SpriteKind.neznicitelny_enemy)

    animation.run_image_animation(duch,
        [img("""
                ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ......fd11111111df......
                        ......fddd1111dddf......
                        ......fbdbfddfbdbf......
                        ......fcdcf11fcdcf......
                        .......fb111111bf.......
                        ......fffcdb1bdffff.....
                        ....fc111cbfbfc111cf....
                        ....f1b1b1ffff1b1b1f....
                        ....fbfbffffffbfbfbf....
                        .........ffffff.........
                        ...........fff..........
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ......fd11111111df......
                        ......fddd1111dddf......
                        ......fbdbfddfbdbf......
                        ......fcdcf11fcdcf......
                        .......fb111111ffff.....
                        ......fffcdb1bc111cf....
                        ....fc111cbfbf1b1b1f....
                        ....f1b1b1ffffbfbfbf....
                        ....fbfbfffffff.........
                        .........fffff..........
                        ..........fff...........
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ......fd11111111df......
                        ......fddd1111dddf......
                        ......fbdbfddfbdbf......
                        ......fcdcf11fcdcf......
                        .......fb111111bf.......
                        ......fffcdb1bdffff.....
                        ....fc111cbfbfc111cf....
                        ....f1b1b1ffff1b1b1f....
                        ....fbfbffffffbfbfbf....
                        .........ffffff.........
                        ...........fff..........
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ......fd11111111df......
                        ......fddd1111dddf......
                        ......fbdbfddfbdbf......
                        ......fcdcf11fcdcf......
                        .....ffff111111bf.......
                        ....fc111cdb1bdfff......
                        ....f1b1bcbfbfc111cf....
                        ....fbfbfbffff1b1b1f....
                        .........fffffffbfbf....
                        ..........fffff.........
                        ...........fff..........
                        ........................
                        ........................
                        ........................
                        ........................
            """)], 300, True)
    tiles.place_on_tile(duch, tiles.get_tile_location(num, num2))

def spawn_duchove(num: number, num2: number): # funkce spawnujici duchy
    scene.follow_path(duch,
        scene.a_star(duch.tilemap_location(),
            tiles.get_tile_location(num, num2)), 60)

def on_overlap_dira(sprite, location):
    global luk, mec, enemy_position, fightScene, duch
    if currentLevel == 5:
        game.show_long_text("Mohl bych tam zkusit vlézt", DialogLayout.BOTTOM)
        scene.set_background_image(img("""
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        """))
        info.set_life(3)
        luk = True
        mec = True
        tiles.set_current_tilemap(tilemap("""level36"""))

        tiles.place_on_tile(mySprite, tiles.get_tile_location(15, 31))
        tiles.set_tile_at(tiles.get_tile_location(5, 11), sprites.dungeon.chest_closed)
        tiles.set_tile_at(tiles.get_tile_location(17, 6), sprites.dungeon.chest_closed)
        tiles.set_tile_at(tiles.get_tile_location(21, 30), sprites.dungeon.chest_closed)
        tiles.set_tile_at(tiles.get_tile_location(18, 6), sprites.dungeon.chest_closed)
        tiles.set_tile_at(tiles.get_tile_location(16, 20), sprites.dungeon.chest_closed)

        enemy_position = [
            [16,18],
            [11,27],
            [24,6],
            [25,26],
            [28,1],
            [31,17],
            [0,3],
            [1,31],
            [4,9],
            [14,14],
            [27,16],
            [8,23]]
        fightScene = True
        duch = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ..........ffff..........
                            ........ff1111ff........
                            .......fb111111bf.......
                            .......f11111111f.......
                            ......fd11111111df......
                            ......fd11111111df......
                            ......fddd1111dddf......
                            ......fbdbfddfbdbf......
                            ......fcdcf11fcdcf......
                            .......fb111111bf.......
                            ......fffcdb1bdffff.....
                            ....fc111cbfbfc111cf....
                            ....f1b1b1ffff1b1b1f....
                            ....fbfbffffffbfbfbf....
                            .........ffffff.........
                            ...........fff..........
                            ........................
                            ........................
                            ........................
                            ........................
            """), SpriteKind.neznicitelny_enemy)

        for value in enemy_position:
            if (enemy_position.index(value) + 1) % 2 == 0:
                spawn_duchove(value[0], value[1])
            else:
                set_duchove(value[0], value[1])
scene.on_overlap_tile(SpriteKind.player, assets.tile("""
        myTile26
    """), on_overlap_dira)

def on_path_completion(sprite, location): # pri dokonceni cesty enemy se otoci
    global pozice
    if currentLevel == 5 and fightScene == True:
        for value3 in enemy_position:
            if location.column == value3[0] and location.row == value3[1]:
                pozice = enemy_position.index(value3)
                if (pozice + 1) % 2 == 0:
                    scene.follow_path(sprite,
                        scene.a_star(location,
                            tiles.get_tile_location(enemy_position[pozice - 1][0], enemy_position[pozice - 1][1])),
                        40)
                else:
                    scene.follow_path(sprite,
                        scene.a_star(location,
                            tiles.get_tile_location(enemy_position[pozice + 1][0], enemy_position[pozice + 1][1])),
                        40)
scene.on_path_completion(SpriteKind.neznicitelny_enemy, on_path_completion)

def on_overlap_schody(sprite, location):
    global currentLevel
    startNextLevel()
scene.on_overlap_tile(SpriteKind.player, sprites.dungeon.stair_east, on_overlap_schody)



# Level 6 #
def level6():
    global fightScene, carodej, statusbar, obrana
    tiles.set_tile_at(tiles.get_tile_location(17, 3), sprites.dungeon.chest_closed)
    fightScene = False
    tiles.place_on_tile(mySprite, tiles.get_tile_location(0, 22))
    carodej = sprites.create(img("""
        . . . . . . . c c c . . . . . .
        . . . . . . c b 5 c . . . . . .
        . . . . c c c 5 5 c c c . . . .
        . . c c b c 5 5 5 5 c c c c . .
        . c b b 5 b 5 5 5 5 b 5 b b c .
        . c b 5 5 b b 5 5 b b 5 5 b c .
        . . f 5 5 5 b b b b 5 5 5 c . .
        . . f f 5 5 5 5 5 5 5 5 f f . .
        . . f f f b f e e f b f f f . .
        . . f f f 1 f b b f 1 f f f . .
        . . . f f b b b b b b f f . . .
        . . . e e f e e e e f e e . . .
        . . e b c b 5 b b 5 b f b e . .
        . . e e f 5 5 5 5 5 5 f e e . .
        . . . . c b 5 5 5 5 b c . . . .
        . . . . . f f f f f f . . . . .
    """), SpriteKind.witcher)
    tiles.set_tile_at(tiles.get_tile_location(16, 20), assets.tile("""
            transparency16
        """))
    statusbar = statusbars.create(20, 4, StatusBarKind.health)
    statusbar.attach_to_sprite(carodej)
    tiles.place_on_tile(carodej, tiles.get_tile_location(13, 1))
    carodej.set_scale(1.7, ScaleAnchor.MIDDLE)
    print(currentLevel)

def on_zero(status): # zabije carodeje pri life bar = 0
    global pohyb_carodeje
    pohyb_carodeje = False
    carodej.destroy(effects.fire, 2000)
statusbars.on_zero(StatusBarKind.health, on_zero)

def on_overlap_kamen(sprite, location): # carodej prijde
    info.set_life(3)
    scene.follow_path(carodej, scene.a_star(tiles.get_tile_location(13, 1), tiles.get_tile_location(13, 8)))
scene.on_overlap_tile(SpriteKind.player, assets.tile("""
        active_kamen
    """), on_overlap_kamen)

def on_update_interval_koule(): # strili koule
    global ohniva_koule, obrana, pohyb_carodeje
    if pohyb_carodeje == True and obrana == False:
        ohniva_koule = sprites.create(img("""
                . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . 4 4 4 4 4 . . . . . .
                            . . . 4 4 4 5 5 5 d 4 4 4 4 . .
                            . . 4 d 5 d 5 5 5 d d d 4 4 . .
                            . . 4 5 5 1 1 1 d d 5 5 5 4 . .
                            . 4 5 5 5 1 1 1 5 1 1 5 5 4 4 .
                            . 4 d d 1 1 5 5 5 1 1 5 5 d 4 .
                            . 4 5 5 1 1 5 1 1 5 5 d d d 4 .
                            . 2 5 5 5 d 1 1 1 5 1 1 5 5 2 .
                            . 2 d 5 5 d 1 1 1 5 1 1 5 5 2 .
                            . . 2 4 d d 5 5 5 5 d d 5 4 . .
                            . . . 2 2 4 d 5 5 d d 4 4 . . .
                            . . . 2 2 2 2 4 4 4 2 2 2 . . .
                            . . . . . 4 4 4 4 4 4 2 . . . .
                            . . . . . . . . . . . . . . . .
            """), SpriteKind.projectile_koule)
        ohniva_koule.set_position(carodej.x, carodej.y)
        ohniva_koule.set_bounce_on_wall(True)
        scene.follow_path(ohniva_koule, scene.a_star(carodej.tilemap_location(), mySprite.tilemap_location()))
game.on_update_interval(3000, on_update_interval_koule)

def on_path_completion_ohniva_koule(sprite, location):
    sprite.destroy(effects.warm_radial, 1)
scene.on_path_completion(SpriteKind.projectile_koule, on_path_completion_ohniva_koule)

def on_overlap_sword_carodej(sprite, otherSprite):
    info.change_score_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.player, on_overlap_sword_carodej)

def on_path_completion_carodej(sprite, location):
    global pohyb_carodeje, obrana
    game.show_long_text("ČERNOKNĚŽNÍK: Konečně se potkáváme, snad ukážeš, co v tobě je!", DialogLayout.BOTTOM)
    pohyb_carodeje = True
    obrana = False
scene.on_path_completion(SpriteKind.witcher, on_path_completion_carodej)

def on_overlap_projectile_koule(sprite, otherSprite): # zniceni koule pomoci projectile
    global swingingBow
    otherSprite.destroy(effects.warm_radial, 1)
    if sprite == arrow:
        sprite.destroy(effects.disintegrate, 1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.projectile_koule, on_overlap_projectile_koule)

def on_overlap_koule_mySprite(sprite, otherSprite):
    sprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.projectile_koule, SpriteKind.player, on_overlap_koule_mySprite)

def on_overlap_projectile_carodej(sprite, otherSprite): # zasazeni carodeje
    global obrana
    if obrana == False and sprite == arrow:
        statusbar.value -= 0.5
    elif obrana == False and sprite == SwordImage:
        info.change_life_by(-1)
        game.splash("Meč na něj nepůsobí!")
sprites.on_overlap(SpriteKind.projectile, SpriteKind.witcher, on_overlap_projectile_carodej)

def on_update_interval_netopyri():
    global obrana, pohyb_carodeje
    if pohyb_carodeje and obrana == True and pocet_obran == 1:
        netopyr_boss = sprites.create(img("""
            . . f f f . . . . . . . . . . .
            f f f c c . . . . . . . . f f f
            f f c c c . c c . . . f c b b c
            f f c 3 c c 3 c c f f b b b c .
            f f c 3 b c 3 b c f b b c c c .
            f c b b b b b b c f b c b c c .
            c c 1 b b b 1 b c b b c b b c .
            c b b b b b b b b b c c c b c .
            c b 1 f f 1 c b b c c c c c . .
            c f 1 f f 1 f b b b b f c . . .
            f f f f f f f b b b b f c . . .
            f f 2 2 2 2 f b b b b f c c . .
            . f 2 2 2 2 2 b b b c f . . . .
            . . f 2 2 2 b b b c f . . . . .
            . . . f f f f f f f . . . . . .
            . . . . . . . . . . . . . . . .
        """), SpriteKind.enemy)
        tiles.place_on_random_tile(netopyr_boss, img("""
            c c c c c c c c c c c c c c c c
            c c c c c c c c c b c c c c b c
            c c b c c c c c c c c c c c c c
            c c c c c c c c c c c c c c c c
            c c c c c c c c c c c c c c c c
            c c c b c c b c c c c b c c c c
            c c c c c c c c c c c c c c c c
            c b c c c c c c c c c c c c c c
            c c c c c c c c c c c c c c c c
            c c c c c b c c c c c b c c c c
            c c c c c c c c c c c c c c c c
            c c c c c c c c c c c c c c c c
            c c c c c c c c c c c c c c c c
            c c b c c c c c c c c c c c c c
            c c c c c c c b c c c c c c b b
            c c c c c c c c c c c c c c b c
        """))
        netopyr_boss.follow(mySprite, 35)

    elif pohyb_carodeje and obrana == True and pocet_obran == 2:
            netopyr_boss = sprites.create(img("""
                . . f f f . . . . . . . . . . .
                f f f c c . . . . . . . . f f f
                f f c c c . c c . . . f c b b c
                f f c 3 c c 3 c c f f b b b c .
                f f c 3 b c 3 b c f b b c c c .
                f c b b b b b b c f b c b c c .
                c c 1 b b b 1 b c b b c b b c .
                c b b b b b b b b b c c c b c .
                c b 1 f f 1 c b b c c c c c . .
                c f 1 f f 1 f b b b b f c . . .
                f f f f f f f b b b b f c . . .
                f f 2 2 2 2 f b b b b f c c . .
                . f 2 2 2 2 2 b b b c f . . . .
                . . f 2 2 2 b b b c f . . . . .
                . . . f f f f f f f . . . . . .
                . . . . . . . . . . . . . . . .
            """), SpriteKind.enemy)
            tiles.place_on_random_tile(netopyr_boss, img("""
                c c c c c c c c c c c c c c c c
                c c c c c c c c c b c c c c b c
                c c b c c c c c c c c c c c c c
                c c c c c c c c c c c c c c c c
                c c c c c c c c c c c c c c c c
                c c c b c c b c c c c b c c c c
                c c c c c c c c c c c c c c c c
                c b c c c c c c c c c c c c c c
                c c c c c c c c c c c c c c c c
                c c c c c b c c c c c b c c c c
                c c c c c c c c c c c c c c c c
                c c c c c c c c c c c c c c c c
                c c c c c c c c c c c c c c c c
                c c b c c c c c c c c c c c c c
                c c c c c c c b c c c c c c b b
                c c c c c c c c c c c c c c b c
            """))
            netopyr_boss.follow(mySprite, 50)

    elif pohyb_carodeje and obrana == True and pocet_obran == 3:
                netopyr_boss = sprites.create(img("""
                    . . f f f . . . . . . . . . . .
                    f f f c c . . . . . . . . f f f
                    f f c c c . c c . . . f c b b c
                    f f c 3 c c 3 c c f f b b b c .
                    f f c 3 b c 3 b c f b b c c c .
                    f c b b b b b b c f b c b c c .
                    c c 1 b b b 1 b c b b c b b c .
                    c b b b b b b b b b c c c b c .
                    c b 1 f f 1 c b b c c c c c . .
                    c f 1 f f 1 f b b b b f c . . .
                    f f f f f f f b b b b f c . . .
                    f f 2 2 2 2 f b b b b f c c . .
                    . f 2 2 2 2 2 b b b c f . . . .
                    . . f 2 2 2 b b b c f . . . . .
                    . . . f f f f f f f . . . . . .
                    . . . . . . . . . . . . . . . .
                """), SpriteKind.enemy)
                tiles.place_on_random_tile(netopyr_boss, img("""
                    c c c c c c c c c c c c c c c c
                    c c c c c c c c c b c c c c b c
                    c c b c c c c c c c c c c c c c
                    c c c c c c c c c c c c c c c c
                    c c c c c c c c c c c c c c c c
                    c c c b c c b c c c c b c c c c
                    c c c c c c c c c c c c c c c c
                    c b c c c c c c c c c c c c c c
                    c c c c c c c c c c c c c c c c
                    c c c c c b c c c c c b c c c c
                    c c c c c c c c c c c c c c c c
                    c c c c c c c c c c c c c c c c
                    c c c c c c c c c c c c c c c c
                    c c b c c c c c c c c c c c c c
                    c c c c c c c b c c c c c c b b
                    c c c c c c c c c c c c c c b c
                """))
                netopyr_boss.follow(mySprite, 70)
game.on_update_interval(3000, on_update_interval_netopyri)

def on_status_reached_lte_percentage(status):
    global obrana, pocet_obran
    pocet_obran += 1
    if pocet_obran == 1:
        obrana = True
        carodej.set_image(img("""
            ....................
            .........ccc........
            ........cb5c........
            ......ccc55ccc......
            ....ccbc5555cccc....
            ...cbb5b5555b5bbc...
            ...cb55bb55bb55bc...
            ....f555bbbb555c....
            ....ff55555555ff....
            ....fffb7ee7bfff....
            ....fff93bb39fff....
            .....ffbbbbbbff.....
            ....beefeeeefee7....
            ...77bcb5bb5bfb37...
            ...3eef555555fee7...
            ...77.cb5555bc.7b...
            ....b7.ffffff.777...
            .....73776777773....
            ........777977......
            ....................
        """))
        for zivot in range(6):
            statusbar.value += 5
            pause(3000)
        obrana = False
        carodej.set_image(img("""
            . . . . . . . c c c . . . . . .
            . . . . . . c b 5 c . . . . . .
            . . . . c c c 5 5 c c c . . . .
            . . c c b c 5 5 5 5 c c c c . .
            . c b b 5 b 5 5 5 5 b 5 b b c .
            . c b 5 5 b b 5 5 b b 5 5 b c .
            . . f 5 5 5 b b b b 5 5 5 c . .
            . . f f 5 5 5 5 5 5 5 5 f f . .
            . . f f f b f e e f b f f f . .
            . . f f f 1 f b b f 1 f f f . .
            . . . f f b b b b b b f f . . .
            . . . e e f e e e e f e e . . .
            . . e b c b 5 b b 5 b f b e . .
            . . e e f 5 5 5 5 5 5 f e e . .
            . . . . c b 5 5 5 5 b c . . . .
            . . . . . f f f f f f . . . . .
        """))

    elif pocet_obran == 2:
        obrana = True
        carodej.set_image(img("""
            ....................
            .........ccc........
            ........cb5c........
            ......ccc55ccc......
            ....ccbc5555cccc....
            ...cbb5b5555b5bbc...
            ...cb55bb55bb55bc...
            ....f555bbbb555c....
            ....ff55555555ff....
            ....fffb7ee7bfff....
            ....fff93bb39fff....
            .....ffbbbbbbff.....
            ....beefeeeefee7....
            ...77bcb5bb5bfb37...
            ...3eef555555fee7...
            ...77.cb5555bc.7b...
            ....b7.ffffff.777...
            .....73776777773....
            ........777977......
            ....................
        """))
        for zivot in range(4):
            statusbar.value += 5
            pause(5000)
        obrana = False
        carodej.set_image(img("""
            . . . . . . . c c c . . . . . .
            . . . . . . c b 5 c . . . . . .
            . . . . c c c 5 5 c c c . . . .
            . . c c b c 5 5 5 5 c c c c . .
            . c b b 5 b 5 5 5 5 b 5 b b c .
            . c b 5 5 b b 5 5 b b 5 5 b c .
            . . f 5 5 5 b b b b 5 5 5 c . .
            . . f f 5 5 5 5 5 5 5 5 f f . .
            . . f f f b f e e f b f f f . .
            . . f f f 1 f b b f 1 f f f . .
            . . . f f b b b b b b f f . . .
            . . . e e f e e e e f e e . . .
            . . e b c b 5 b b 5 b f b e . .
            . . e e f 5 5 5 5 5 5 f e e . .
            . . . . c b 5 5 5 5 b c . . . .
            . . . . . f f f f f f . . . . .
        """))

    elif pocet_obran == 3:
        obrana = True
        carodej.set_image(img("""
            ....................
            .........ccc........
            ........cb5c........
            ......ccc55ccc......
            ....ccbc5555cccc....
            ...cbb5b5555b5bbc...
            ...cb55bb55bb55bc...
            ....f555bbbb555c....
            ....ff55555555ff....
            ....fffb7ee7bfff....
            ....fff93bb39fff....
            .....ffbbbbbbff.....
            ....beefeeeefee7....
            ...77bcb5bb5bfb37...
            ...3eef555555fee7...
            ...77.cb5555bc.7b...
            ....b7.ffffff.777...
            .....73776777773....
            ........777977......
            ....................
        """))
        for zivot in range(2):
            statusbar.value += 5
            pause(10000)
        obrana = False
        carodej.set_image(img("""
            . . . . . . . c c c . . . . . .
            . . . . . . c b 5 c . . . . . .
            . . . . c c c 5 5 c c c . . . .
            . . c c b c 5 5 5 5 c c c c . .
            . c b b 5 b 5 5 5 5 b 5 b b c .
            . c b 5 5 b b 5 5 b b 5 5 b c .
            . . f 5 5 5 b b b b 5 5 5 c . .
            . . f f 5 5 5 5 5 5 5 5 f f . .
            . . f f f b f e e f b f f f . .
            . . f f f 1 f b b f 1 f f f . .
            . . . f f b b b b b b f f . . .
            . . . e e f e e e e f e e . . .
            . . e b c b 5 b b 5 b f b e . .
            . . e e f 5 5 5 5 5 5 f e e . .
            . . . . c b 5 5 5 5 b c . . . .
            . . . . . f f f f f f . . . . .
        """))
statusbars.on_status_reached(StatusBarKind.health, statusbars.StatusComparison.LTE, statusbars.ComparisonType.PERCENTAGE, 25, on_status_reached_lte_percentage)

def on_overlap_schody_princezna(sprite, location):
    if pohyb_carodeje == False:
        scene.set_background_color(10)
        tiles.set_current_tilemap(tilemap("""level44"""))
        tiles.place_on_tile(mySprite, tiles.get_tile_location(7, 15))
        princezna = sprites.create(img("""
            . . . . . . 5 . 5 . . . . . . .
            . . . . . f 5 5 5 f f . . . . .
            . . . . f 1 5 2 5 1 6 f . . . .
            . . . f 1 6 6 6 6 6 1 6 f . . .
            . . . f 6 6 f f f f 6 1 f . . .
            . . . f 6 f f d d f f 6 f . . .
            . . f 6 f d f d d f d f 6 f . .
            . . f 6 f d 3 d d 3 d f 6 f . .
            . . f 6 6 f d d d d f 6 6 f . .
            . f 6 6 f 3 f f f f 3 f 6 6 f .
            . . f f d 3 5 3 3 5 3 d f f . .
            . . f d d f 3 5 5 3 f d d f . .
            . . . f f 3 3 3 3 3 3 f f . . .
            . . . f 3 3 5 3 3 5 3 3 f . . .
            . . . f f f f f f f f f f . . .
            . . . . . f f . . f f . . . . .
        """), SpriteKind.player)
        tiles.place_on_tile(princezna, tiles.get_tile_location(10, 8))
scene.on_overlap_tile(SpriteKind.player, img("""
    d d c c c c c c c c c c c c d d
    d d c b b b b b b b b b b c d d
    d d b d d d d d d d d d d b d d
    d d c c c c c c c c c c c c d d
    d d c b b b b b b b b b b c d d
    d d b d d d d d d d d d d b d d
    d d c c c c c c c c c c c c d d
    d d c b b b b b b b b b b c d d
    d d b d d d d d d d d d d b d d
    d d c c c c c c c c c c c c d d
    d d c b b b b b b b b b b c d d
    d d b d d d d d d d d d d b d d
    d d c c c c c c c c c c c c d d
    d d c b b b b b b b b b b c d d
    b b b d d d d d d d d d d b b b
    c c c c c c c c c c c c c c c c
"""), on_overlap_schody_princezna)

def on_overlap_koberec_princezna(sprite, location):
    if sprite == mySprite:
        game.show_long_text("PRINCEZNA: Dokázal jsi to, zachránil si mě!", DialogLayout.BOTTOM)
        startNextLevel()
scene.on_overlap_tile(SpriteKind.player, img("""
    a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a
    a a a a a a a a a a a a a a a a
"""), on_overlap_koberec_princezna)
#level 5\

