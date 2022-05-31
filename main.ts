namespace SpriteKind {
    export const King = SpriteKind.create()
}
namespace StrProp {
    export const Name = StrProp.create()
    export const Text = StrProp.create()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    game.setDialogFrame(img`
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
        `)
    game.showLongText("KRÁL: Zdravím, jsem rád, že si přišel.", DialogLayout.Bottom)
    game.showLongText("KRÁL: Mám pro tebe důležitý úkol.", DialogLayout.Bottom)
    game.showLongText("KRÁL: Má dcera byla unesena a nyní je na dalekém zámku.", DialogLayout.Bottom)
    game.showLongText("KRÁL: Onen zámek se nachází za černým lesem a řekou.", DialogLayout.Bottom)
    game.showLongText("KRÁL: Vězní ji tam obávaný černokněžník.", DialogLayout.Bottom)
    game.showLongText("KRÁL: Pokud ji osvobodíš, dostaneš ji a půlku království!", DialogLayout.Bottom)
    game.showLongText("JÁ: Dobrá, pokusím se ji najít a přivést.", DialogLayout.Bottom)
    game.showLongText("KRÁL: Přeji hodně štěstí a dávej na sebe pozor.", DialogLayout.Bottom)
})
function startNextLevel () {
    currentLevel += 1
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    sprites.destroyAllSpritesOfKind(SpriteKind.Food)
    if (currentLevel == 1) {
        tiles.setCurrentTilemap(tilemap`level1`)
        firstLevel()
    } else if (currentLevel == 2) {
        tiles.setCurrentTilemap(tilemap`level2`)
    } else {
        game.over(true)
    }
}
function firstLevel () {
    Kral = sprites.create(img`
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
        `, SpriteKind.Player)
    tiles.placeOnTile(mySprite, tiles.getTileLocation(5, 4))
    tiles.placeOnRandomTile(Kral, assets.tile`myTile0`)
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`dvere kral`, function (sprite, location) {
    startNextLevel()
})
let Kral: Sprite = null
let currentLevel = 0
let mySprite: Sprite = null
startNextLevel()
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 100)
scene.cameraFollowSprite(mySprite)
info.setLife(3)
