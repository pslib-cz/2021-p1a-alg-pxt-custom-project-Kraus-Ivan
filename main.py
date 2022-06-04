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
@namespace
class StrProp:
    Name = StrProp.create()
    Text = StrProp.create()

def on_up_pressed():
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
            """)],
        100,
        False)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_hit_wall(sprite, location):
    if currentLevel == 2:
        game.splash("Měl bych jít po cestě...")
scene.on_hit_wall(SpriteKind.player, on_hit_wall)

def on_overlap_tile(sprite2, location2):
    global dialogSkoncen
    if currentLevel == 2:
        dialogSkoncen = False
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        wood
    """),
    on_overlap_tile)

def level4():
    pass

def on_b_pressed():
    pass
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

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
        """),
        SpriteKind.King)
    tiles.place_on_random_tile(Kral, assets.tile("""
        myTile0
    """))
    game.splash("Přišel jsi za králem pro jeho nabídku.")
    game.splash("Stiskem A s ním promluvíš.")

def on_a_pressed():
    global swingingSword
    if mec == True:
        if swingingSword == False:
            swingingSword = True
            if pozice_zbrane[0] == 1:
                sword.set_image(img("""
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
            elif pozice_zbrane[1] == 1:
                sword.set_image(img("""
                    1 . . . . . . . 1 . . . . . c c 
                                        . . . . . . . . . . . . . c c c 
                                        . . . . . . . . . . . c c a c . 
                                        . . . . . . . . . . c d d c . . 
                                        1 . . . . . . . . c d b d c . . 
                                        . . . . . . . . c d b d c . . . 
                                        . . . . . . . c d b d c . . . 1 
                                        1 . . . . . c d b d c . . . . . 
                                        . . . . . c d b d c . . . . . . 
                                        . . . . c d b d c . . . . . . . 
                                        . . . c d b d c . . . . . . . . 
                                        . . . c d d c . . . . . 1 . . . 
                                        . . . c c c . . . . . . . . . . 
                                        . . . . . . . . . . . . . . . . 
                                        . . . . . . . . . . . . . . . . 
                                        1 . . . . . . 1 . . . . . . . .
                """))
            elif pozice_zbrane[2] == 1:
                sword.set_image(img("""
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
            elif pozice_zbrane[3] == 1:
                sword.set_image(img("""
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
        sword.set_image(img("""
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

def on_left_pressed():
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
            """)],
        100,
        False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def level3():
    global dialogSkoncen, mec, Lucistnik
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    dialogSkoncen = False
    mec = False
    scene.set_background_color(6)
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
        """),
        SpriteKind.NPC)
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
            """)],
        100,
        False)
    tiles.place_on_tile(Lucistnik, tiles.get_tile_location(18, 10))
    tiles.place_on_tile(mySprite, tiles.get_tile_location(0, 7))
def startNextLevel():
    global currentLevel, StromTmavy
    currentLevel += 1
    if currentLevel == 1:
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
        level1()
    elif currentLevel == 2:
        tiles.set_current_tilemap(tilemap("""
            level2
        """))
        level2()
    elif currentLevel == 3:
        sprites.destroy_all_sprites_of_kind(SpriteKind.Zbrojir)
        sprites.destroy_all_sprites_of_kind(SpriteKind.House)
        sprites.destroy_all_sprites_of_kind(SpriteKind.Tree)
        sprites.destroy_all_sprites_of_kind(SpriteKind.checkpoint)
        tiles.set_current_tilemap(tilemap("""
            level0
        """))
        scene.set_background_image(img("""
            6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666
        """))
        move_lock(False)
        for value in tiles.get_tiles_by_type(assets.tile("""
            myTile9
        """)):
            StromTmavy = sprites.create(assets.image("""
                spoustec
            """), SpriteKind.enemyTree)
            tiles.place_on_tile(StromTmavy, value)
        level3()
    elif currentLevel == 4:
        tiles.set_current_tilemap(tilemap("""
            level28
        """))
        level4()
    else:
        game.over(True)

def on_overlap_tile2(sprite3, location3):
    global mec, dialogSkoncen
    if dialogSkoncen == False:
        game.show_long_text("ZBROJÍŘ: Počkej, počkej.", DialogLayout.BOTTOM)
        game.show_long_text("ZBROJÍŘ: Povídal mi o tobě král.", DialogLayout.BOTTOM)
        game.show_long_text("ZBROJÍŘ: Jsem místní zbrojíř a mám ti dát todle.",
            DialogLayout.BOTTOM)
        mec = True
        game.splash("Získal jsi meč")
        game.splash("Stiskem A mečem sekáš")
        dialogSkoncen = True
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        hlina
    """),
    on_overlap_tile2)

def on_on_overlap(sprite4, otherSprite):
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
            """)],
        50,
        False)
    scene.camera_shake(4, 500)
    otherSprite.set_kind(SpriteKind.Tree)
    tiles.set_tile_at(otherSprite.tilemap_location(),
        assets.tile("""
            spawner
        """))
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemyTree, on_on_overlap)

def level2():
    global Zbrojar, House1, Strom, rocks
    sprites.destroy_all_sprites_of_kind(SpriteKind.King)
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
        """),
        SpriteKind.House)
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
        """),
        SpriteKind.Tree)
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

def on_right_pressed():
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
            """)],
        100,
        False)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def zmena_pozice_zbrane(num: number):
    pozice_zbrane[0] = 0
    pozice_zbrane[1] = 0
    pozice_zbrane[2] = 0
    pozice_zbrane[3] = 0
    pozice_zbrane[num] = 1

def on_on_overlap2(sprite5, otherSprite2):
    sprite5.destroy(effects.disintegrate, 100)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap2)

def on_overlap_tile3(sprite6, location4):
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
        game.show_long_text("KRÁL: Zdravím, jsem rád, že si přišel.",
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
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        koberec0
    """),
    on_overlap_tile3)

def on_on_overlap3(sprite7, otherSprite3):
    if currentLevel == 3 and dialogSkoncen == True:
        startNextLevel()
    else:
        startNextLevel()
sprites.on_overlap(SpriteKind.player, SpriteKind.checkpoint, on_on_overlap3)

def on_overlap_tile4(sprite8, location5):
    if currentLevel == 2:
        if dialogSkoncen == False:
            game.splash("Na něco jsem zapomněl...")
            tiles.place_on_tile(mySprite, tiles.get_tile_location(15, 8))
    elif currentLevel == 3:
        if dialogSkoncen == False and fightScene == False:
            pronasledovani(True, Lucistnik, mySprite)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        active2
    """),
    on_overlap_tile4)

def pronasledovani(bool2: bool, Pronasledovatel: Sprite, Obet: Sprite):
    if bool2 == True:
        Pronasledovatel.follow(Obet, 90)
    else:
        Pronasledovatel.follow(Obet, 0)

def on_down_pressed():
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
            """)],
        100,
        False)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_life_zero():
    global fightScene, currentLevel
    if currentLevel == 3:
        fightScene = False
        Lucistnik.destroy()
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    currentLevel = currentLevel - 1
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    startNextLevel()
info.on_life_zero(on_life_zero)

def on_on_overlap4(sprite9, otherSprite4):
    global dialogSkoncen2, dialogSkoncen, fightScene, mec
    if currentLevel == 3:
        if afterFight == True and dialogSkoncen2 == False:
            pronasledovani(False, Lucistnik, mySprite)
            game.show_long_text("LUČIŠTNÍK:  Zachránil si mě", DialogLayout.BOTTOM)
            game.show_long_text("JÁ:  To ano, ale co můj ztupený meč?", DialogLayout.BOTTOM)
            game.show_long_text("LUČIŠTNÍK:  Nevadí, věnuji ti můj luk", DialogLayout.BOTTOM)
            game.splash("Získal jsi luk")
            dialogSkoncen2 = True
        elif dialogSkoncen == False:
            pronasledovani(False, Lucistnik, mySprite)
            game.show_long_text("LUČIŠTNÍK:  Bože zachraň mne!", DialogLayout.BOTTOM)
            game.show_long_text("LUČIŠTNÍK:  Šel jsem lesem a napadli mě obří netopýři",
                DialogLayout.BOTTOM)
            game.show_long_text("LUČIŠTNÍK:  Vylétavají ze začarovaných stromů kolem cesty",
                DialogLayout.BOTTOM)
            game.show_long_text("LUČIŠTNÍK:  Pokus se zničit ty modré stromy, jinak zhynem!!",
                DialogLayout.BOTTOM)
            game.show_long_text("JÁ:  Co?!", DialogLayout.BOTTOM)
            dialogSkoncen = True
            dialogSkoncen2 = False
            fightScene = True
            mec = True
            info.set_life(3)
            pronasledovani(False, Lucistnik, mySprite)
sprites.on_overlap(SpriteKind.NPC, SpriteKind.player, on_on_overlap4)

def move_lock(bool3: bool):
    if bool3 == True:
        controller.move_sprite(mySprite, 0, 0)
    else:
        controller.move_sprite(mySprite, 80, 80)

def on_overlap_tile5(sprite10, location6):
    if dialogSkoncen2 == True:
        startNextLevel()
    else:
        game.splash("Na něco jsem zapomněl...")
        tiles.place_on_tile(mySprite, tiles.get_tile_location(53, 9))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        active
    """),
    on_overlap_tile5)

def on_on_overlap5(sprite11, otherSprite5):
    otherSprite5.destroy(effects.disintegrate, 1000)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap5)

def on_overlap_tile6(sprite12, location7):
    if currentLevel == 1:
        if dialogSkoncen == True:
            startNextLevel()
        else:
            game.splash("Král po tobě něco chce.")
            if controller.A.is_pressed():
                mySprite.set_position(25, 70)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        dvere kral
    """),
    on_overlap_tile6)

myEnemy: Sprite = None
dialogSkoncen2 = False
afterFight = False
fightScene = False
rocks: Sprite = None
Strom: Sprite = None
House1: Sprite = None
Zbrojar: Sprite = None
StromTmavy: Sprite = None
Lucistnik: Sprite = None
swingingSword = False
mec = False
Kral: Sprite = None
dialogSkoncen = False
sword: Sprite = None
currentLevel = 0
pozice_zbrane: List[number] = []
mySprite: Sprite = None
mySprite = sprites.create(img("""
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
    SpriteKind.player)
controller.move_sprite(mySprite, 80, 80)
scene.camera_follow_sprite(mySprite)
pozice_zbrane = [0, 0, 0, 0]
currentLevel = 3
sword = sprites.create(assets.image("""
    swordUP
"""), SpriteKind.projectile)
startNextLevel()

def on_on_update():
    if mySprite.vx < 0:
        sword.right = mySprite.left
        sword.y = mySprite.y
    elif mySprite.vx > 0:
        sword.left = mySprite.right
        sword.y = mySprite.y
    elif mySprite.vy > 0:
        sword.top = mySprite.bottom
        sword.x = mySprite.x
    elif mySprite.vy < 0:
        sword.bottom = mySprite.top
        sword.x = mySprite.x
game.on_update(on_on_update)

def on_update_interval():
    global myEnemy, fightScene, afterFight
    if fightScene == True:
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
                """),
                SpriteKind.enemy)
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
                    """)],
                250,
                True)
            tiles.place_on_tile(myEnemy,
                tiles.get_tiles_by_type(assets.tile("""
                    myTile9
                """))._pick_random())
            myEnemy.follow(mySprite, randint(20, 40))
        else:
            fightScene = False
            pronasledovani(True, Lucistnik, mySprite)
            afterFight = True
game.on_update_interval(3000, on_update_interval)


