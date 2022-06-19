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
    export const drevo = SpriteKind.create()
    export const bobr = SpriteKind.create()
    export const item = SpriteKind.create()
    export const cursor = SpriteKind.create()
    export const button = SpriteKind.create()
    export const Kostlivec = SpriteKind.create()
    export const button_small = SpriteKind.create()
    export const neznicitelny_enemy = SpriteKind.create()
    export const witcher = SpriteKind.create()
    export const projectile_koule = SpriteKind.create()
    export const enemy = SpriteKind.create()
}

namespace StrProp {
    export const Name = StrProp.create()
    export const Text = StrProp.create()
}

let pohyb_carodeje = false
let ohniva_koule : Sprite = null
let pocet_netopyru = 0
let obrana = false
let pocet_obran = 0
let myEnemy : Sprite = null
let button_lvl_6 : Sprite = null
let button_lvl_5 : Sprite = null
let button_lvl_4 : Sprite = null
let button_lvl_3 : Sprite = null
let button_lvl_2 : Sprite = null
let button_lvl_1 : Sprite = null
let projectile3 : Sprite = null
let projectile2 : Sprite = null
let projectile : Sprite = null
let arrow : Sprite = null
let cas_konec = 0
let carodej : Sprite = null
let duch : Sprite = null
let statusbar : StatusBarSprite = null
let afterFight = false
let rocks : Sprite = null
let Strom : Sprite = null
let House1 : Sprite = null
let Zbrojar : Sprite = null
let StromTmavy : Sprite = null
let kursor : Sprite = null
let button_2 : Sprite = null
let button_1 : Sprite = null
let Lucistnik : Sprite = null
let swingingSword = false
let netopyr : Sprite = null
let fightScene = false
let Kral : Sprite = null
let row = 0
let speed = 0
let pozice = 0
let vertical = 0
let swingingBow = false
let cas_zacatek = 0
let naBobrovi = false
let bobr2 : Sprite = null
let time = 0
let spawn_bobri = false
let cislo_sloupce = 0
let mec = false
let luk = false
let dialogSkoncen2 = false
let dialogSkoncen = false
let BowImage : Sprite = null
let SwordImage : Sprite = null
let currentLevel = 0
let pozice_zbrane : boolean[] = []
let mySprite : Sprite = null
let enemy_position : number[][][] = []
mySprite = sprites.create(img`
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
`, SpriteKind.Player)
scene.cameraFollowSprite(mySprite)
pozice_zbrane = [false, false, false, false]
//  smery drzeni zbrane
SwordImage = sprites.create(assets.image`
    swordUP
`, SpriteKind.Projectile)
BowImage = sprites.create(assets.image`
    swordUP
`, SpriteKind.Projectile)
currentLevel = -1
//  level (0 = MENU)
startNextLevel()
// ovladani/
controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    if (!(currentLevel == 0)) {
        zmena_pozice_zbrane(0)
        animation.runImageAnimation(mySprite, [img`
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
                `, img`
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
                `, img`
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
                `], 100, false)
    }
    
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    if (!(currentLevel == 0)) {
        zmena_pozice_zbrane(1)
        animation.runImageAnimation(mySprite, [img`
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
                `, img`
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
                `, img`
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
                `], 100, false)
    }
    
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    if (!(currentLevel == 0)) {
        zmena_pozice_zbrane(3)
        animation.runImageAnimation(mySprite, [img`
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
                `, img`
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
                `, img`
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
                `], 100, false)
    }
    
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    if (!(currentLevel == 0)) {
        zmena_pozice_zbrane(2)
        animation.runImageAnimation(mySprite, [img`
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
                `, img`
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
                `, img`
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
                `], 100, false)
    }
    
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    // mereni casu natazeni luku
    
    if (luk) {
        cas_zacatek = game.runtime()
    }
    
    if (currentLevel == 4 && luk) {
        swingingBow = true
        if (pozice_zbrane[0] == true) {
            BowImage.setImage(assets.image`
                bow
            `)
        } else if (pozice_zbrane[1] == true) {
            BowImage.setImage(img`
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
            `)
        } else if (pozice_zbrane[2] == true) {
            BowImage.setImage(img`
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
            `)
        } else {
            BowImage.setImage(img`
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
            `)
        }
        
    }
    
    swingingBow = false
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    //  seknuti mecem do ruznych smeru
    
    if (mec == true && swingingSword == false) {
        swingingSword = true
        if (pozice_zbrane[0] == true) {
            SwordImage.setImage(img`
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
        } else if (pozice_zbrane[1] == true) {
            SwordImage.setImage(img`
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
            `)
        } else if (pozice_zbrane[2] == true) {
            SwordImage.setImage(img`
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
        } else {
            SwordImage.setImage(img`
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
        
        pause(200)
        SwordImage.setImage(img`
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
controller.B.onEvent(ControllerButtonEvent.Released, function on_b_released() {
    //  vypocet delky casu natazeni luku
    
    if (luk) {
        cas_konec = game.runtime()
        BowImage.setImage(img`
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
        if (cas_konec - cas_zacatek > 1000) {
            if (pozice_zbrane[0] == true) {
                arrow = sprites.createProjectileFromSprite(img`
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
                `, mySprite, 0, -100)
            } else if (pozice_zbrane[1] == true) {
                arrow = sprites.createProjectileFromSprite(img`
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
                    `, mySprite, 0, 100)
            } else if (pozice_zbrane[2] == true) {
                arrow = sprites.createProjectileFromSprite(img`
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
                    `, mySprite, -100, 0)
            } else {
                arrow = sprites.createProjectileFromSprite(img`
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
                    `, mySprite, 100, 0)
            }
            
        }
        
    }
    
})
game.onUpdate(function on_update_pozice_zbrani() {
    //  pozice zbrani
    if (mec) {
        if (mySprite.vx < 0) {
            SwordImage.right = mySprite.left
            SwordImage.y = mySprite.y
        } else if (mySprite.vx > 0) {
            SwordImage.left = mySprite.right
            SwordImage.y = mySprite.y
        } else if (mySprite.vy > 0) {
            SwordImage.top = mySprite.bottom
            SwordImage.x = mySprite.x
        } else if (mySprite.vy < 0) {
            SwordImage.bottom = mySprite.top
            SwordImage.x = mySprite.x
        }
        
    }
    
    if (luk) {
        if (mySprite.vx < 0) {
            BowImage.right = mySprite.left
            BowImage.y = mySprite.y
        } else if (mySprite.vx > 0) {
            BowImage.left = mySprite.right
            BowImage.y = mySprite.y
        } else if (mySprite.vy > 0) {
            BowImage.top = mySprite.bottom
            BowImage.x = mySprite.x
        } else if (mySprite.vy < 0) {
            BowImage.bottom = mySprite.top
            BowImage.x = mySprite.x
        }
        
    }
    
})
// ovladani\
// obecne funkce/
function startNextLevel() {
    //  funkce menici levely
    
    currentLevel += 1
    if (!(currentLevel == 0)) {
        mySprite.setImage(img`
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
        `)
        controller.moveSprite(mySprite, 80, 80)
        sprites.destroyAllSpritesOfKind(SpriteKind.King)
        sprites.destroyAllSpritesOfKind(SpriteKind.Zbrojir)
        sprites.destroyAllSpritesOfKind(SpriteKind.House)
        sprites.destroyAllSpritesOfKind(SpriteKind.Tree)
        sprites.destroyAllSpritesOfKind(SpriteKind.checkpoint)
        sprites.destroyAllSpritesOfKind(SpriteKind.NPC)
        sprites.destroyAllSpritesOfKind(SpriteKind.spoustec)
        sprites.destroyAllSpritesOfKind(SpriteKind.enemyTree)
        sprites.destroyAllSpritesOfKind(SpriteKind.point)
        sprites.destroyAllSpritesOfKind(SpriteKind.drevo)
        sprites.destroyAllSpritesOfKind(SpriteKind.bobr)
        sprites.destroyAllSpritesOfKind(SpriteKind.item)
        sprites.destroyAllSpritesOfKind(SpriteKind.cursor)
        sprites.destroyAllSpritesOfKind(SpriteKind.button_small)
        sprites.destroyAllSpritesOfKind(SpriteKind.button)
        sprites.destroyAllSpritesOfKind(SpriteKind.Kostlivec)
        sprites.destroyAllSpritesOfKind(SpriteKind.neznicitelny_enemy)
        sprites.destroyAllSpritesOfKind(SpriteKind.enemy)
        sprites.destroyAllSpritesOfKind(SpriteKind.witcher)
        sprites.destroyAllSpritesOfKind(SpriteKind.projectile_koule)
    }
    
    if (currentLevel == 0) {
        scene.setBackgroundImage(img`
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
        `)
        button_1 = sprites.create(img`
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
            `, SpriteKind.button)
        button_1.setScale(1.75, ScaleAnchor.Middle)
        button_2 = sprites.create(img`
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
            `, SpriteKind.button)
        button_2.setScale(1.75, ScaleAnchor.Middle)
        kursor = sprites.create(img`
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
            `, SpriteKind.cursor)
        kursor.setStayInScreen(true)
        button_1.setPosition(35, 65)
        button_2.setPosition(120, 65)
        controller.moveSprite(kursor, 80, 80)
    } else if (currentLevel == 1) {
        tiles.setCurrentTilemap(tilemap`level1`)
        level1()
    } else if (currentLevel == 2) {
        scene.setBackgroundImage(img`
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
        `)
        tiles.setCurrentTilemap(tilemap`level2`)
        level2()
    } else if (currentLevel == 3) {
        tiles.setCurrentTilemap(tilemap`level0`)
        move_lock(false)
        // sazeni stromu
        for (let value of tiles.getTilesByType(assets.tile`
            myTile9
        `)) {
            StromTmavy = sprites.create(assets.image`spoustec`, SpriteKind.enemyTree)
            tiles.placeOnTile(StromTmavy, value)
        }
        level3()
    } else if (currentLevel == 4) {
        scene.setBackgroundImage(img`
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
        `)
        tiles.setCurrentTilemap(tilemap`level28`)
        level4()
    } else if (currentLevel == 5) {
        scene.setBackgroundImage(img`
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
        `)
        tiles.setCurrentTilemap(tilemap`level34`)
        level5()
    } else if (currentLevel == 6) {
        tiles.setCurrentTilemap(tilemap`level38`)
        level6()
    } else {
        game.over(true)
    }
    
}

sprites.onOverlap(SpriteKind.cursor, SpriteKind.button, function on_overlap_cursor(sprite: Sprite, otherSprite: Sprite) {
    //  pri najeti v MENU kurzorem se tlacitka zvets
    otherSprite.setScale(2, ScaleAnchor.Middle)
})
function move_lock(boolean: boolean) {
    //  zamek pohybu postav
    if (boolean) {
        controller.moveSprite(mySprite, 0, 0)
    } else {
        controller.moveSprite(mySprite, 80, 80)
    }
    
}

sprites.onOverlap(SpriteKind.enemy, SpriteKind.Player, function on_overlap_enemy(sprite: Sprite, otherSprite: Sprite) {
    //  odecteni zivota pri najeti na enemy
    sprite.destroy(effects.disintegrate, 200)
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.neznicitelny_enemy, SpriteKind.Player, function on_overlap_neznicitelny_enemy(sprite: Sprite, otherSprite: Sprite) {
    //  odecteni zivota pri najeti na neznicitelny enemy
    sprite.destroy(effects.disintegrate, 200)
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.cursor, SpriteKind.button, function on_overlap_levely(sprite: Sprite, otherSprite: Sprite) {
    //  MENU
    
    if (otherSprite == button_1 && controller.A.isPressed()) {
        startNextLevel()
    } else if (otherSprite == button_2 && controller.A.isPressed()) {
        scene.setBackgroundImage(img`
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
        `)
        sprites.destroyAllSpritesOfKind(SpriteKind.button)
        sprites.destroyAllSpritesOfKind(SpriteKind.cursor)
        button_lvl_1 = sprites.create(img`
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
            `, SpriteKind.button_small)
        button_lvl_1.setPosition(55, 55)
        button_lvl_2 = sprites.create(img`
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
            `, SpriteKind.button_small)
        button_lvl_2.setPosition(105, 55)
        button_lvl_3 = sprites.create(img`
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
            `, SpriteKind.button_small)
        button_lvl_3.setPosition(55, 75)
        button_lvl_4 = sprites.create(img`
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
            `, SpriteKind.button_small)
        button_lvl_4.setPosition(105, 75)
        button_lvl_5 = sprites.create(img`
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
            `, SpriteKind.button_small)
        button_lvl_5.setPosition(55, 95)
        button_lvl_6 = sprites.create(img`
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
        `, SpriteKind.button_small)
        button_lvl_6.setPosition(105, 95)
        kursor = sprites.create(img`
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
        `, SpriteKind.cursor)
        kursor.setStayInScreen(true)
        controller.moveSprite(kursor, 80, 80)
    }
    
})
sprites.onOverlap(SpriteKind.cursor, SpriteKind.button_small, function on_overlap_levels(sprite: Sprite, otherSprite: Sprite) {
    
    if (otherSprite == button_lvl_1 && controller.A.isPressed()) {
        currentLevel = 0
        startNextLevel()
    } else if (otherSprite == button_lvl_2 && controller.A.isPressed()) {
        currentLevel = 1
        startNextLevel()
    } else if (otherSprite == button_lvl_3 && controller.A.isPressed()) {
        currentLevel = 2
        startNextLevel()
    } else if (otherSprite == button_lvl_4 && controller.A.isPressed()) {
        currentLevel = 3
        startNextLevel()
    } else if (otherSprite == button_lvl_5 && controller.A.isPressed()) {
        currentLevel = 4
        startNextLevel()
    } else if (otherSprite == button_lvl_6 && controller.A.isPressed()) {
        currentLevel = 5
        startNextLevel()
    }
    
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.enemy, function on_overlap_enemy_zniceni(sprite: Sprite, otherSprite: Sprite) {
    //  zniceni enemy pri stretnuti
    otherSprite.destroy(effects.disintegrate, 200)
})
scene.onHitWall(SpriteKind.Player, function on_hit_wall(sprite: Sprite, location: tiles.Location) {
    //  narazeni na zed
    if (currentLevel == 2) {
        game.splash("Měl bych jít po cestě...")
    } else if (currentLevel == 4) {
        game.splash("Měl bych se vrátit...")
    }
    
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.checkpoint, function on_overlap_checkpoint(sprite: Sprite, otherSprite: Sprite) {
    //  najeti na checkpoint
    if (currentLevel == 3 && dialogSkoncen) {
        startNextLevel()
    } else {
        startNextLevel()
    }
    
})
function zmena_pozice_zbrane(num: number) {
    //  zmena aktualni pozice zbrane
    for (let pos = 0; pos < 4; pos++) {
        pozice_zbrane[pos] = false
    }
    pozice_zbrane[num] = true
}

function pronasledovani(boolean: boolean, Pronasledovatel: Sprite, Obet: Sprite) {
    //  pronasledovani
    if (boolean) {
        Pronasledovatel.follow(Obet, 90)
    } else {
        Pronasledovatel.follow(Obet, 0)
    }
    
}

info.onLifeZero(function on_life_zero() {
    //  umrti hlavni postavy
    
    if (currentLevel == 3) {
        fightScene = false
        Lucistnik.destroy()
    }
    
    if (currentLevel == 4) {
        game.splash("Utopil jsi se.")
    } else {
        game.splash("Zemřel jsi.")
    }
    
    currentLevel = currentLevel - 1
    sprites.destroyAllSpritesOfKind(SpriteKind.enemy)
    startNextLevel()
})
// obecne funkce\
// level 1/
function level1() {
    
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
    tiles.placeOnRandomTile(Kral, assets.tile`
        myTile0
    `)
    game.splash("Přišel jsi za králem pro jeho nabídku.")
    game.splash("Stiskem A s ním promluvíš.")
}

scene.onOverlapTile(SpriteKind.Player, assets.tile`
        koberec0
    `, function on_overlap_kral(sprite: Sprite, location: tiles.Location) {
    //  rozhovor s kralem
    
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
        game.showLongText("KRÁL: Zdravím, jsem rád, že jsi přišel.", DialogLayout.Bottom)
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
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        dvere kral
    `, function on_overlap_dvere(sprite: Sprite, location: tiles.Location) {
    if (currentLevel == 1) {
        if (dialogSkoncen) {
            // pokud probehl dialog, zacne novy level
            startNextLevel()
        } else {
            //  pokud dialog neprobehl, nepusti hrace k novemu levelu
            game.splash("Král po tobě něco chce.")
            if (controller.A.isPressed()) {
                mySprite.setPosition(25, 70)
            }
            
        }
        
    }
    
})
// level 1\
// level 2/
function level2() {
    
    sprites.destroyAllSpritesOfKind(SpriteKind.King)
    // spawn kamenu, stromu, baraku..
    Zbrojar = sprites.create(assets.image`
        Lucistnik
    `, SpriteKind.Zbrojir)
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
    rocks = sprites.create(assets.image`
        checkpoint
    `, SpriteKind.checkpoint)
    tiles.placeOnTile(rocks, tiles.getTileLocation(13, 0))
    rocks = sprites.create(assets.image`
        checkpoint
    `, SpriteKind.checkpoint)
    tiles.placeOnTile(rocks, tiles.getTileLocation(14, 0))
    tiles.placeOnTile(mySprite, tiles.getTileLocation(30, 22))
}

scene.onOverlapTile(SpriteKind.Player, assets.tile`
        hlina
    `, function on_overlap_zbrojir(sprite: Sprite, location: tiles.Location) {
    
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
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        active2
    `, function on_overlap_konec_cesty(sprite: Sprite, location: tiles.Location) {
    if (currentLevel == 2 && dialogSkoncen == false) {
        game.splash("Na něco jsem zapomněl...")
        tiles.placeOnTile(mySprite, tiles.getTileLocation(15, 8))
    } else if (currentLevel == 3 && dialogSkoncen == false && fightScene == false) {
        pronasledovani(true, Lucistnik, mySprite)
    }
    
})
// level 2\
// level 3/
function level3() {
    
    scene.setBackgroundImage(img`
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
    `)
    pocet_netopyru = 0
    dialogSkoncen = false
    mec = false
    luk = false
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
    animation.runImageAnimation(Lucistnik, [img`
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
            `, img`
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
            `, img`
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
            `], 100, false)
    tiles.placeOnTile(Lucistnik, tiles.getTileLocation(18, 10))
    tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 7))
}

scene.onOverlapTile(SpriteKind.Player, assets.tile`
        active
    `, function on_overlap_cesta_level(sprite102: Sprite, location62: tiles.Location) {
    //  pusti novy level jen po dokonceni levelu
    if (dialogSkoncen2 == true || currentLevel == 4) {
        startNextLevel()
    } else if (currentLevel == 3) {
        game.splash("Na něco jsem zapomněl...")
        tiles.placeOnTile(mySprite, tiles.getTileLocation(53, 9))
    }
    
})
sprites.onCreated(SpriteKind.enemy, function on_created_netopyr(sprite: Sprite) {
    
    pocet_netopyru += 1
})
sprites.onDestroyed(SpriteKind.enemy, function on_destroyed_netopyr(sprite: Sprite) {
    
    pocet_netopyru -= 1
})
sprites.onOverlap(SpriteKind.NPC, SpriteKind.Player, function on_overlap_lucistnik(sprite: Sprite, otherSprite: Sprite) {
    //  rozhovor s lucistnikem
    
    luk = false
    if (currentLevel == 3) {
        if (afterFight == true && dialogSkoncen2 == false) {
            pronasledovani(false, Lucistnik, mySprite)
            game.showLongText("LUČIŠTNÍK:  Zachránil si mě", DialogLayout.Bottom)
            game.showLongText("LUČIŠTNÍK:  Za to ti věnuji můj luk", DialogLayout.Bottom)
            game.splash("Získal jsi luk")
            luk = true
            dialogSkoncen2 = true
        } else if (dialogSkoncen == false) {
            pronasledovani(false, Lucistnik, mySprite)
            game.showLongText("LUČIŠTNÍK:  Bože zachraň mne!", DialogLayout.Bottom)
            game.showLongText("LUČIŠTNÍK:  Šel jsem lesem a napadli mě obří netopýři", DialogLayout.Bottom)
            game.showLongText("LUČIŠTNÍK:  Vylétavají ze začarovaných stromů kolem cesty", DialogLayout.Bottom)
            game.showLongText("LUČIŠTNÍK:  Pokus se zničit ty modré stromy, jinak zhynem!!", DialogLayout.Bottom)
            game.showLongText("JÁ:  Co?!", DialogLayout.Bottom)
            dialogSkoncen = true
            dialogSkoncen2 = false
            fightScene = true
            mec = true
            info.setLife(3)
            pronasledovani(false, Lucistnik, mySprite)
            pause(1500)
        }
        
    }
    
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.enemyTree, function on_overlap_strom(sprite: Sprite, otherSprite: Sprite) {
    //  zniceni stromu
    animation.runImageAnimation(otherSprite, [img`
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
            `, img`
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
            `, img`
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
            `, img`
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
            `], 100, false)
    scene.cameraShake(4, 500)
    otherSprite.setKind(SpriteKind.Tree)
    tiles.setTileAt(otherSprite.tilemapLocation(), assets.tile`
            spawner
        `)
})
game.onUpdateInterval(3000, function on_update_interval() {
    //  spawn netopyru
    
    if (currentLevel == 3 && fightScene && pocet_netopyru < 5) {
        if (tiles.getTilesByType(assets.tile`
            myTile9
        `).length > 0) {
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
            `, SpriteKind.enemy)
            animation.runImageAnimation(myEnemy, [img`
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
                    `, img`
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
                    `, img`
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
                    `, img`
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
                    `], 250, true)
            tiles.placeOnTile(myEnemy, tiles.getTilesByType(assets.tile`
                    myTile9
                `)._pickRandom())
            myEnemy.follow(mySprite, randint(20, 40))
        } else {
            fightScene = false
            pronasledovani(true, Lucistnik, mySprite)
            afterFight = true
        }
        
    }
    
})
// level 3\
// level 4/
function level4() {
    
    info.setLife(3)
    dialogSkoncen = false
    dialogSkoncen2 = false
    tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 7))
    luk = false
    mec = false
    cislo_sloupce = -1
    spawn_bobri = false
    time = 3000
    bobr2 = sprites.create(assets.image`
        bobr
    `, SpriteKind.bobr)
}

scene.onOverlapTile(SpriteKind.Player, assets.tile`
        wood
    `, function on_overlap_molo(sprite2: Sprite, location2: tiles.Location) {
    //  slapnuti na molo
    
    if (currentLevel == 2) {
        dialogSkoncen = false
    }
    
    if (currentLevel == 4 && dialogSkoncen == false) {
        dialogSkoncen = true
        game.showLongText("Sakra, neumím plavat. Musím nějak přebrodit řeku", DialogLayout.Bottom)
        spawn_bobri = true
        zmena_sloupce()
    }
    
    if (currentLevel == 4 && (bobr2.tileKindAt(TileDirection.Left, assets.tile`
        wood
    `) || bobr2.tileKindAt(TileDirection.Right, assets.tile`
        wood
    `))) {
        if (dialogSkoncen2 == false) {
            game.showLongText("Proč tu sviští bobři?!", DialogLayout.Bottom)
            game.splash("Podržením natáhneš luk, puštěním s ním vystřelíš.")
            luk = true
            dialogSkoncen2 = true
        }
        
    }
    
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile12
    `, function on_overlap_voda(sprite3: Sprite, location3: tiles.Location) {
    //  pri najeti na vodu hrac zemre
    if (naBobrovi == false) {
        info.setLife(0)
    }
    
})
game.onUpdate(function on_update_pozice_hrace() {
    //  hlida, zda je hrac na bobrovi/molu nebo na vode
    
    if (currentLevel == 4) {
        if (tiles.tileAtLocationEquals(mySprite.tilemapLocation(), assets.tile`
                myTile11
            `) || tiles.tileAtLocationEquals(mySprite.tilemapLocation(), assets.tile`
            wood
        `)) {
            naBobrovi = true
        } else if (tiles.tileAtLocationEquals(mySprite.tilemapLocation(), sprites.castle.tileGrass1) || tiles.tileAtLocationEquals(mySprite.tilemapLocation(), sprites.castle.tilePath4)) {
            naBobrovi = true
        } else {
            naBobrovi = false
        }
        
    }
    
})
forever(function on_forever() {
    //  spawn bobru
    
    if (controller.B.isPressed() && luk == true && swingingBow == false && !(currentLevel == 4)) {
        swingingBow = true
        if (pozice_zbrane[0] == true) {
            BowImage.setImage(assets.image`
                bow
            `)
        } else if (pozice_zbrane[1] == true) {
            BowImage.setImage(img`
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
            `)
        } else if (pozice_zbrane[2] == true) {
            BowImage.setImage(img`
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
            `)
        } else {
            BowImage.setImage(img`
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
            `)
        }
        
        swingingBow = false
    }
    
    if (currentLevel == 4 && spawn_bobri) {
        zmena_bobra()
        bobr2 = sprites.create(assets.image`bobr`, SpriteKind.bobr)
        tiles.placeOnTile(bobr2, tiles.getTileLocation(cislo_sloupce + 10, row))
        bobr2.ay = speed
        bobr2.setFlag(SpriteFlag.DestroyOnWall, true)
        pause(time)
    } else if (currentLevel == 0 && !kursor.overlapsWith(button_1)) {
        //  zmenseni tlacitek v menu
        if (!kursor.overlapsWith(button_2)) {
            button_1.setScale(1.75, ScaleAnchor.Middle)
            button_2.setScale(1.75, ScaleAnchor.Middle)
        }
        
    }
    
})
function zmena_bobra() {
    //  meni rychlost a smer bobra
    
    time = randint(2500, 5000)
    vertical = randint(0, 1)
    if (vertical == 0) {
        speed = randint(150, 400)
        row = 0
    } else {
        speed = randint(-150, -400)
        row = 15
    }
    
}

function zmena_sloupce() {
    let spawn_bobri: boolean;
    //  meni aktualni sloupec bobru
    
    if (cislo_sloupce == 9) {
        sprites.destroyAllSpritesOfKind(SpriteKind.bobr)
        spawn_bobri = false
    } else {
        cislo_sloupce = cislo_sloupce + 1
    }
    
}

sprites.onOverlap(SpriteKind.Projectile, SpriteKind.bobr, function on_overlap_zniceni_bobra(sprite: Sprite, otherSprite: Sprite) {
    //  znici bobra pri zastreleni sipem
    otherSprite.destroy(effects.coolRadial, 1)
    sprite.destroy()
    tiles.setTileAt(otherSprite.tilemapLocation(), assets.tile`
            myTile11
        `)
    if (otherSprite.tileKindAt(TileDirection.Left, assets.tile`
        myTile11
    `) || otherSprite.tileKindAt(TileDirection.Left, assets.tile`
        wood
    `)) {
        sprites.destroyAllSpritesOfKind(SpriteKind.bobr)
        zmena_sloupce()
    }
    
})
// level 4\
// level 5/
function level5() {
    
    pohyb_carodeje = false
    pocet_obran = 0
    dialogSkoncen = false
    dialogSkoncen2 = false
    tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 8))
    fightScene = false
    luk = true
    mec = true
}

scene.onOverlapTile(SpriteKind.Player, assets.tile`
        active2
    `, function on_overlap_brana(sprite: Sprite, location: tiles.Location) {
    //  zavrena brana
    if (currentLevel == 5) {
        game.splash("Brána je zařená, musím najít jiný vchod")
        tiles.placeOnTile(mySprite, tiles.getTileLocation(19, 8))
    }
    
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        active_black
    `, function on_overlap_strop(sprite: Sprite, location: tiles.Location) {
    //  spadnuti stropu
    if (currentLevel == 5) {
        game.splash("Bohužel, spadl na tebe strop")
        game.splash("Zemřel jsi.")
        info.setLife(0)
    }
    
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestClosed, function on_overlap_treasure(sprite: Sprite, location: tiles.Location) {
    //  ziskani zivota navic z truhly
    
    if (currentLevel == 5) {
        tiles.setTileAt(location, sprites.dungeon.chestOpen)
        effects.hearts.startScreenEffect(500)
        game.splash("Získal jsi život navíc")
        info.changeLifeBy(1)
    }
    
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile26
    `, function on_overlap_dira(sprite: Sprite, location: tiles.Location) {
    
    if (currentLevel == 5) {
        game.showLongText("Mohl bych tam zkusit vlézt", DialogLayout.Bottom)
        scene.setBackgroundImage(img`
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
        `)
        info.setLife(3)
        luk = true
        mec = true
        tiles.setCurrentTilemap(tilemap`level36`)
        tiles.placeOnTile(mySprite, tiles.getTileLocation(15, 31))
        tiles.setTileAt(tiles.getTileLocation(5, 11), sprites.dungeon.chestClosed)
        tiles.setTileAt(tiles.getTileLocation(17, 6), sprites.dungeon.chestClosed)
        tiles.setTileAt(tiles.getTileLocation(21, 30), sprites.dungeon.chestClosed)
        tiles.setTileAt(tiles.getTileLocation(18, 6), sprites.dungeon.chestClosed)
        tiles.setTileAt(tiles.getTileLocation(16, 20), sprites.dungeon.chestClosed)
        enemy_position = [[[7, 17], [0, 60]], [[19, 16], [0, 60]], [[17, 26], [60, 0]]]
        fightScene = true
        for (let pos of enemy_position) {
            duch = sprites.create(img`
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
                `, SpriteKind.neznicitelny_enemy)
            tiles.placeOnTile(duch, tiles.getTileLocation(pos[0][0], pos[0][1]))
            duch.setVelocity(pos[1][0], pos[1][1])
        }
    }
    
})
scene.onHitWall(SpriteKind.neznicitelny_enemy, function on_hit_wall_duchove(sprite: Sprite, location: tiles.Location) {
    //  otaci duchy pri narazeni na zed
    if (sprite.isHittingTile(CollisionDirection.Bottom)) {
        sprite.setVelocity(0, -60)
    } else if (sprite.isHittingTile(CollisionDirection.Top)) {
        sprite.setVelocity(0, 60)
    } else if (sprite.isHittingTile(CollisionDirection.Right)) {
        sprite.setVelocity(-60, 0)
    } else if (sprite.isHittingTile(CollisionDirection.Left)) {
        sprite.setVelocity(60, 0)
    }
    
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.stairEast, function on_overlap_schody(sprite: Sprite, location: tiles.Location) {
    
    startNextLevel()
})
//  Level 6 #
function level6() {
    
    luk = true
    mec = true
    tiles.setTileAt(tiles.getTileLocation(17, 3), sprites.dungeon.chestClosed)
    fightScene = false
    tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 22))
    carodej = sprites.create(img`
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
    `, SpriteKind.witcher)
    tiles.setTileAt(tiles.getTileLocation(16, 20), assets.tile`
            transparency16
        `)
    statusbar = statusbars.create(20, 4, StatusBarKind.Health)
    statusbar.attachToSprite(carodej)
    tiles.placeOnTile(carodej, tiles.getTileLocation(13, 1))
    carodej.setScale(1.7, ScaleAnchor.Middle)
    console.log(currentLevel)
}

statusbars.onZero(StatusBarKind.Health, function on_zero(status: StatusBarSprite) {
    //  zabije carodeje pri life bar = 0
    
    pohyb_carodeje = false
    carodej.destroy(effects.fire, 2000)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        active_kamen
    `, function on_overlap_kamen(sprite: Sprite, location: tiles.Location) {
    //  carodej prijde
    info.setLife(3)
    scene.followPath(carodej, scene.aStar(tiles.getTileLocation(13, 1), tiles.getTileLocation(13, 8)))
})
game.onUpdateInterval(3000, function on_update_interval_koule() {
    //  strili koule
    
    if (pohyb_carodeje == true && obrana == false) {
        ohniva_koule = sprites.create(img`
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
            `, SpriteKind.projectile_koule)
        ohniva_koule.setPosition(carodej.x, carodej.y)
        ohniva_koule.setBounceOnWall(true)
        scene.followPath(ohniva_koule, scene.aStar(carodej.tilemapLocation(), mySprite.tilemapLocation()))
    }
    
})
scene.onPathCompletion(SpriteKind.projectile_koule, function on_path_completion_ohniva_koule(sprite: Sprite, location: tiles.Location) {
    sprite.destroy(effects.warmRadial, 1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Player, function on_overlap_sword_carodej(sprite: Sprite, otherSprite: Sprite) {
    info.changeScoreBy(-1)
})
scene.onPathCompletion(SpriteKind.witcher, function on_path_completion_carodej(sprite: Sprite, location: tiles.Location) {
    
    game.showLongText("ČERNOKNĚŽNÍK: Konečně se potkáváme, snad ukážeš, co v tobě je!", DialogLayout.Bottom)
    pohyb_carodeje = true
    obrana = false
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.projectile_koule, function on_overlap_projectile_koule(sprite: Sprite, otherSprite: Sprite) {
    //  zniceni koule pomoci projectile
    
    otherSprite.destroy(effects.warmRadial, 1)
    if (sprite == arrow) {
        sprite.destroy(effects.disintegrate, 1)
    }
    
})
sprites.onOverlap(SpriteKind.projectile_koule, SpriteKind.Player, function on_overlap_koule_mySprite(sprite: Sprite, otherSprite: Sprite) {
    sprite.destroy()
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.witcher, function on_overlap_projectile_carodej(sprite: Sprite, otherSprite: Sprite) {
    //  zasazeni carodeje
    
    if (obrana == false && sprite == arrow) {
        statusbar.value -= 0.5
    } else if (obrana == false && sprite == SwordImage) {
        info.changeLifeBy(-1)
        game.splash("Meč na něj nepůsobí!")
    }
    
})
game.onUpdateInterval(3000, function on_update_interval_netopyri() {
    let netopyr_boss: Sprite;
    
    if (pohyb_carodeje && obrana == true && pocet_obran == 1) {
        netopyr_boss = sprites.create(img`
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
        `, SpriteKind.enemy)
        tiles.placeOnRandomTile(netopyr_boss, img`
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
        `)
        netopyr_boss.follow(mySprite, 35)
    } else if (pohyb_carodeje && obrana == true && pocet_obran == 2) {
        netopyr_boss = sprites.create(img`
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
            `, SpriteKind.enemy)
        tiles.placeOnRandomTile(netopyr_boss, img`
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
            `)
        netopyr_boss.follow(mySprite, 50)
    } else if (pohyb_carodeje && obrana == true && pocet_obran == 3) {
        netopyr_boss = sprites.create(img`
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
                `, SpriteKind.enemy)
        tiles.placeOnRandomTile(netopyr_boss, img`
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
                `)
        netopyr_boss.follow(mySprite, 70)
    }
    
})
statusbars.onStatusReached(StatusBarKind.Health, statusbars.StatusComparison.LTE, statusbars.ComparisonType.Percentage, 25, function on_status_reached_lte_percentage(status: StatusBarSprite) {
    let zivot: number;
    
    pocet_obran += 1
    if (pocet_obran == 1) {
        obrana = true
        carodej.setImage(img`
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
        `)
        for (zivot = 0; zivot < 6; zivot++) {
            statusbar.value += 5
            pause(3000)
        }
        obrana = false
        carodej.setImage(img`
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
        `)
    } else if (pocet_obran == 2) {
        obrana = true
        carodej.setImage(img`
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
        `)
        for (zivot = 0; zivot < 4; zivot++) {
            statusbar.value += 5
            pause(5000)
        }
        obrana = false
        carodej.setImage(img`
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
        `)
    } else if (pocet_obran == 3) {
        obrana = true
        carodej.setImage(img`
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
        `)
        for (zivot = 0; zivot < 2; zivot++) {
            statusbar.value += 5
            pause(10000)
        }
        obrana = false
        carodej.setImage(img`
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
        `)
    }
    
})
scene.onOverlapTile(SpriteKind.Player, img`
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
`, function on_overlap_schody_princezna(sprite: Sprite, location: tiles.Location) {
    let princezna: Sprite;
    if (pohyb_carodeje == false) {
        scene.setBackgroundColor(10)
        tiles.setCurrentTilemap(tilemap`level44`)
        tiles.placeOnTile(mySprite, tiles.getTileLocation(7, 15))
        princezna = sprites.create(img`
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
        `, SpriteKind.Player)
        tiles.placeOnTile(princezna, tiles.getTileLocation(10, 8))
    }
    
})
scene.onOverlapTile(SpriteKind.Player, img`
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
`, function on_overlap_koberec_princezna(sprite: Sprite, location: tiles.Location) {
    if (sprite == mySprite) {
        game.showLongText("PRINCEZNA: Dokázal jsi to, zachránil si mě!", DialogLayout.Bottom)
        startNextLevel()
    }
    
})
