from translate import Translator

translator = Translator(to_lang="ru")
with open('eng.txt', 'w') as f:
    f.write('Hello world')

with open('eng.txt', 'r') as eng_f:
    with open('ru.txt', 'w') as f:
        f.write(translator.translate(eng_f.read()))
