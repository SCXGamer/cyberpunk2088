def on_button_pressed_a():
    if input.temperature() > 30:
        for index in range(10):
            music.play_tone(988, music.beat(BeatFraction.HALF))
        basic.show_number(input.temperature())
    else:
        music.play_tone(988, music.beat(BeatFraction.WHOLE))
        music.play_tone(698, music.beat(BeatFraction.WHOLE))
        basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 255)
input.on_button_pressed(Button.B, on_button_pressed_b)

Random = 0
Length = 0
music.start_melody(music.built_in_melody(Melodies.JUMP_UP), MelodyOptions.ONCE)

def on_forever():
    global Length
    Length = maqueen.ultrasonic(PingUnit.CENTIMETERS)
basic.forever(on_forever)

def on_forever2():
    global Random
    if Length == 30:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 0)
        Random = randint(1, 3)
        if Random == 1:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 255)
        if Random == 2:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 130)
        if Random == 3:
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 130)
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 255)
basic.forever(on_forever2)

def on_forever3():
    if input.compass_heading() == 0:
        basic.show_arrow(ArrowNames.NORTH)
    if input.compass_heading() == 45:
        basic.show_arrow(ArrowNames.NORTH_WEST)
    if input.compass_heading() == 90:
        basic.show_arrow(ArrowNames.WEST)
    if input.compass_heading() == 135:
        basic.show_arrow(ArrowNames.SOUTH_WEST)
    if input.compass_heading() == 180:
        basic.show_arrow(ArrowNames.SOUTH)
    if input.compass_heading() == 270:
        basic.show_arrow(ArrowNames.EAST)
    if input.compass_heading() == 225:
        basic.show_arrow(ArrowNames.SOUTH_EAST)
    if input.compass_heading() == 315:
        basic.show_arrow(ArrowNames.NORTH_EAST)
basic.forever(on_forever3)
