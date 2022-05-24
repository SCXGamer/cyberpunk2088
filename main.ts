input.onButtonPressed(Button.A, function () {
    if (input.temperature() > 30) {
        for (let index = 0; index < 10; index++) {
            music.playTone(988, music.beat(BeatFraction.Half))
        }
        basic.showNumber(input.temperature())
    } else {
        music.playTone(988, music.beat(BeatFraction.Whole))
        music.playTone(698, music.beat(BeatFraction.Whole))
        basic.showNumber(input.temperature())
    }
})
input.onButtonPressed(Button.B, function () {
    maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 255)
})
let Random = 0
let Length = 0
music.startMelody(music.builtInMelody(Melodies.JumpUp), MelodyOptions.Once)
basic.forever(function () {
    Length = maqueen.Ultrasonic(PingUnit.Centimeters)
})
basic.forever(function () {
    if (input.compassHeading() == 0) {
        basic.showArrow(ArrowNames.North)
    }
    if (input.compassHeading() == 45) {
        basic.showArrow(ArrowNames.NorthWest)
    }
    if (input.compassHeading() == 90) {
        basic.showArrow(ArrowNames.West)
    }
    if (input.compassHeading() == 135) {
        basic.showArrow(ArrowNames.SouthWest)
    }
    if (input.compassHeading() == 180) {
        basic.showArrow(ArrowNames.South)
    }
    if (input.compassHeading() == 270) {
        basic.showArrow(ArrowNames.East)
    }
    if (input.compassHeading() == 225) {
        basic.showArrow(ArrowNames.SouthEast)
    }
    if (input.compassHeading() == 315) {
        basic.showArrow(ArrowNames.NorthEast)
    }
})
basic.forever(function () {
    if (Length == 30) {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 0)
        Random = randint(1, 3)
        if (Random == 1) {
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 255)
        }
        if (Random == 2) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 130)
        }
        if (Random == 3) {
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 130)
        }
    }
    maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 255)
})
