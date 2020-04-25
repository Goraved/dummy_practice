import os

logo = [
    '            ______              '
    , '       .d$$$******$$$$c.        '
    , '    .d$P"            "$$c      '
    , '   $$$$$.           .$$$*$.    '
    , ' .$$ 4$L*$$.     .$$Pd$  \'$b   '
    , ' $F   *$. "$$e.e$$" 4$F   ^$b  '
    , 'd$     $$   z$$$e   $$     \'$. '
    , '$P     `$L$$P` `"$$d$"      $$ '
    , '$$     e$$F       4$$b.     $$ '
    , '$b  .$$" $$   O  .$$ "4$b.  $$ '
    , '$$e$P"    $b     d$`    "$$c$F '
    , '$P$$$$$$$$$$$$$$$$$$$$$$$$$$  '
    , ' "$c.      4$.  $$       .$$   '
    , '  ^$$.      $$ d$"      d$P    '
    , '    "$$c.   `$b$F    .d$P"     '
    , '      `4$$$c.$$$..e$$P"        '
    , '          `^^^^^^^`'
    , '      ']


def print_logo():
    text = ''
    for row in logo:
        os.system('cls' if os.name == 'nt' else 'clear')
        text += f'\n{row}'
        print(text)
    print('"GUESS F𖤐CKING NUMBER" game!\n\n')


def play_music():
    import pyglet

    music = pyglet.resource.media('doom.wav')
    music.play()
    pyglet.app.run()
