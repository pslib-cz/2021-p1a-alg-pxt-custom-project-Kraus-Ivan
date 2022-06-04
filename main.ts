namespace SpriteKind {
    export const King = SpriteKind.create()
    export const Zbrojir = SpriteKind.create()
    export const House = SpriteKind.create()
    export const Tree = SpriteKind.create()
    export const checkpoint = SpriteKind.create()
    export const NPC = SpriteKind.create()
    export const spoustec = SpriteKind.create()
    export const enemyTree = SpriteKind.create()
    export const point = SpriteKind.create()
}
namespace StrProp {
    export const Name = StrProp.create()
    export const Text = StrProp.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    zmena_pozice_zbrane(0)
    animation.runImageAnimation(
    mySprite,
    [img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    false
    )
})
scene.onHitWall(SpriteKind.Player, function (sprite, location) {
    if (currentLevel == 2) {
        game.splash("Měl bych jít po cestě...")
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`wood`, function (sprite, location) {
    if (currentLevel == 2) {
        dialogSkoncen = false
    }
})
function level1 () {
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
        `, SpriteKind.King)
    tiles.placeOnRandomTile(Kral, assets.tile`myTile0`)
    game.splash("Přišel jsi za králem pro jeho nabídku.")
    game.splash("Stiskem A s ním promluvíš.")
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mec == true) {
        if (swingingSword == false) {
            swingingSword = true
            if (pozice_zbrane[0] == 1) {
                sword.setImage(img`
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
                    `)
            } else if (pozice_zbrane[1] == 1) {
                sword.setImage(img`
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
                    `)
            } else if (pozice_zbrane[2] == 1) {
                sword.setImage(img`
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
                    `)
            } else if (pozice_zbrane[3] == 1) {
                sword.setImage(img`
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
                    `)
            }
        }
        pause(200)
        sword.setImage(img`
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
            `)
        swingingSword = false
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    zmena_pozice_zbrane(2)
    animation.runImageAnimation(
    mySprite,
    [img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    false
    )
})
function level3 () {
    dialogSkoncen = false
    mec = false
    scene.setBackgroundColor(6)
    Lucistnik = sprites.create(img`
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
        `, SpriteKind.NPC)
    animation.runImageAnimation(
    Lucistnik,
    [img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    false
    )
    tiles.placeOnTile(Lucistnik, tiles.getTileLocation(18, 10))
    tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 7))
}
function startNextLevel () {
    currentLevel += 1
    if (currentLevel == 1) {
        tiles.setCurrentTilemap(tilemap`level1`)
        level1()
    } else if (currentLevel == 2) {
        tiles.setCurrentTilemap(tilemap`level2`)
        level2()
    } else if (currentLevel == 3) {
        sprites.destroyAllSpritesOfKind(SpriteKind.Zbrojir)
        sprites.destroyAllSpritesOfKind(SpriteKind.House)
        sprites.destroyAllSpritesOfKind(SpriteKind.Tree)
        sprites.destroyAllSpritesOfKind(SpriteKind.checkpoint)
        tiles.setCurrentTilemap(tilemap`level0`)
        scene.setBackgroundImage(img`
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
            `)
        move_lock(false)
        for (let value of tiles.getTilesByType(assets.tile`myTile9`)) {
            StromTmavy = sprites.create(assets.image`spoustec`, SpriteKind.enemyTree)
            tiles.placeOnTile(StromTmavy, value)
        }
        level3()
    } else if (currentLevel == 4) {
        tiles.setCurrentTilemap(tilemap`level28`)
    } else {
        game.over(true)
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`hlina`, function (sprite, location) {
    if (dialogSkoncen == false) {
        game.showLongText("ZBROJÍŘ: Počkej, počkej.", DialogLayout.Bottom)
        game.showLongText("ZBROJÍŘ: Povídal mi o tobě král.", DialogLayout.Bottom)
        game.showLongText("ZBROJÍŘ: Jsem místní zbrojíř a mám ti dát todle.", DialogLayout.Bottom)
        mec = true
        game.splash("Získal jsi meč")
        game.splash("Stiskem A mečem sekáš")
        dialogSkoncen = true
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.enemyTree, function (sprite, otherSprite) {
    animation.runImageAnimation(
    otherSprite,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    50,
    false
    )
    scene.cameraShake(4, 500)
    otherSprite.setKind(SpriteKind.Tree)
    tiles.setTileAt(otherSprite.tilemapLocation(), assets.tile`spawner`)
})
function level2 () {
    sprites.destroyAllSpritesOfKind(SpriteKind.King)
    Zbrojar = sprites.create(assets.image`Lucistnik`, SpriteKind.Zbrojir)
    tiles.placeOnTile(Zbrojar, tiles.getTileLocation(13, 12))
    House1 = sprites.create(img`
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
        `, SpriteKind.House)
    tiles.placeOnTile(House1, tiles.getTileLocation(11, 11))
    Strom = sprites.create(img`
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
        `, SpriteKind.Tree)
    tiles.placeOnTile(Strom, tiles.getTileLocation(17, 17))
    rocks = sprites.create(assets.image`checkpoint`, SpriteKind.checkpoint)
    tiles.placeOnTile(rocks, tiles.getTileLocation(13, 0))
    rocks = sprites.create(assets.image`checkpoint`, SpriteKind.checkpoint)
    tiles.placeOnTile(rocks, tiles.getTileLocation(14, 0))
    tiles.placeOnTile(mySprite, tiles.getTileLocation(30, 22))
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    zmena_pozice_zbrane(3)
    animation.runImageAnimation(
    mySprite,
    [img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    false
    )
})
function zmena_pozice_zbrane (num: number) {
    pozice_zbrane[0] = 0
    pozice_zbrane[1] = 0
    pozice_zbrane[2] = 0
    pozice_zbrane[3] = 0
    pozice_zbrane[num] = 1
}
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    sprite.destroy(effects.disintegrate, 100)
    info.changeLifeBy(-1)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`koberec0`, function (sprite, location) {
    if (controller.A.isPressed() && dialogSkoncen == false) {
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
        game.showLongText("KRÁL: Pokud ji osvobodíš, dostaneš ji za ženu", DialogLayout.Bottom)
        game.showLongText("JÁ: Dobrá, pokusím se ji najít a přivést.", DialogLayout.Bottom)
        game.showLongText("KRÁL: Přeji hodně štěstí a dávej na sebe pozor.", DialogLayout.Bottom)
        dialogSkoncen = true
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.checkpoint, function (sprite, otherSprite) {
    if (currentLevel == 3 && dialogSkoncen == true) {
        startNextLevel()
    } else {
        startNextLevel()
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`active2`, function (sprite, location) {
    if (currentLevel == 2) {
        if (dialogSkoncen == false) {
            game.splash("Na něco jsem zapomněl...")
            tiles.placeOnTile(mySprite, tiles.getTileLocation(15, 8))
        }
    } else if (currentLevel == 3) {
        if (dialogSkoncen == false && fightScene == false) {
            pronasledovani(true, Lucistnik, mySprite)
        }
    }
})
function pronasledovani (bool: boolean, Pronasledovatel: Sprite, Obet: Sprite) {
    if (bool == true) {
        Pronasledovatel.follow(Obet, 90)
    } else {
        Pronasledovatel.follow(Obet, 0)
    }
}
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    zmena_pozice_zbrane(1)
    animation.runImageAnimation(
    mySprite,
    [img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    false
    )
})
info.onLifeZero(function () {
    if (currentLevel == 3) {
        fightScene = false
        Lucistnik.destroy()
        sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
    }
    currentLevel = currentLevel - 1
    startNextLevel()
})
sprites.onOverlap(SpriteKind.NPC, SpriteKind.Player, function (sprite, otherSprite) {
    if (currentLevel == 3) {
        if (afterFight == true && dialogSkoncen2 == false) {
            pronasledovani(false, Lucistnik, mySprite)
            game.showLongText("LUČIŠTNÍK:  Zachránil si mě", DialogLayout.Bottom)
            game.showLongText("JÁ:  To ano, ale co můj ztupený meč?", DialogLayout.Bottom)
            game.showLongText("LUČIŠTNÍK:  Nevadí, věnuji ti můj luk", DialogLayout.Bottom)
            game.splash("Získal jsi luk")
            dialogSkoncen2 = true
        } else if (dialogSkoncen == false) {
            pronasledovani(false, Lucistnik, mySprite)
            game.showLongText("LUČIŠTNÍK:  Bože zachraň mne!", DialogLayout.Bottom)
            game.showLongText("LUČIŠTNÍK:  Šel jsem lesem a napadli mě obří netopýři", DialogLayout.Bottom)
            game.showLongText("LUČIŠTNÍK:  Vylétavají ze začarovaných stromů!", DialogLayout.Bottom)
            game.showLongText("JÁ:  Co?!", DialogLayout.Bottom)
            dialogSkoncen = true
            dialogSkoncen2 = false
            fightScene = true
            mec = true
            info.setLife(3)
            pronasledovani(false, Lucistnik, mySprite)
        }
    }
})
function move_lock (bool: boolean) {
    if (bool == true) {
        controller.moveSprite(mySprite, 0, 0)
    } else {
        controller.moveSprite(mySprite, 80, 80)
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`active`, function (sprite, location) {
    if (dialogSkoncen2 == true) {
        startNextLevel()
    } else {
        game.splash("Na něco jsem zapomněl...")
        tiles.placeOnTile(mySprite, tiles.getTileLocation(53, 9))
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy(effects.disintegrate, 1000)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`dvere kral`, function (sprite, location) {
    if (currentLevel == 1) {
        if (dialogSkoncen == true) {
            startNextLevel()
        } else {
            game.splash("Král po tobě něco chce.")
            if (controller.A.isPressed()) {
                mySprite.setPosition(25, 70)
            }
        }
    }
})
let myEnemy: Sprite = null
let dialogSkoncen2 = false
let afterFight = false
let fightScene = false
let rocks: Sprite = null
let Strom: Sprite = null
let House1: Sprite = null
let Zbrojar: Sprite = null
let StromTmavy: Sprite = null
let Lucistnik: Sprite = null
let swingingSword = false
let mec = false
let Kral: Sprite = null
let dialogSkoncen = false
let sword: Sprite = null
let currentLevel = 0
let pozice_zbrane: number[] = []
let mySprite: Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 80, 80)
scene.cameraFollowSprite(mySprite)
pozice_zbrane = [
0,
0,
0,
0
]
currentLevel = 2
sword = sprites.create(assets.image`swordUP`, SpriteKind.Projectile)
startNextLevel()
game.onUpdate(function () {
    if (mySprite.vx < 0) {
        sword.right = mySprite.left
        sword.y = mySprite.y
    } else if (mySprite.vx > 0) {
        sword.left = mySprite.right
        sword.y = mySprite.y
    } else if (mySprite.vy > 0) {
        sword.top = mySprite.bottom
        sword.x = mySprite.x
    } else if (mySprite.vy < 0) {
        sword.bottom = mySprite.top
        sword.x = mySprite.x
    }
})
game.onUpdateInterval(3000, function () {
    if (fightScene == true) {
        if (tiles.getTilesByType(assets.tile`myTile9`).length > 0) {
            myEnemy = sprites.create(img`
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
                `, SpriteKind.Enemy)
            animation.runImageAnimation(
            myEnemy,
            [img`
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
                `,img`
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
                `,img`
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
                `,img`
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
                `],
            250,
            true
            )
            tiles.placeOnTile(myEnemy, tiles.getTilesByType(assets.tile`myTile9`)._pickRandom())
            myEnemy.follow(mySprite, randint(15, 60))
        } else {
            fightScene = false
            pronasledovani(true, Lucistnik, mySprite)
            afterFight = true
        }
    }
})
