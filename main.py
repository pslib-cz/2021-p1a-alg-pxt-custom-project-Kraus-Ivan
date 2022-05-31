@namespace
class SpriteKind:
    King = SpriteKind.create()

def on_overlap_tile(sprite, location):
    game.show_long_text("", DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        koberec
    """),
    on_overlap_tile)

def createScript(characterName: Sprite, text: str):
    global newScript
    newScript = blockObject.create()
newScript: blockObject.BlockObject = None
mySprite = sprites.create(img("""
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
    SpriteKind.player)
controller.move_sprite(mySprite)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
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
    SpriteKind.player)
tiles.place_on_tile(mySprite, tiles.get_tile_location(5, 4))
tiles.place_on_random_tile(Kral, assets.tile("""
    myTile0
"""))