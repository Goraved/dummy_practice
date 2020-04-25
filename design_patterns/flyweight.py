class Sentence:
    def __init__(self, plain_text):
        self.words = plain_text.split(' ')
        self.tokens = {}

    def __getitem__(self, item):
        wd = self.WordToken()
        self.tokens[item] = wd
        return self.tokens[item]

    class WordToken:
        def __init__(self, capitalize=False):
            self.capitalize = capitalize

    def __str__(self):
        result = []
        for w in range(len(self.words)):
            word = self.words[w]
            if w in self.tokens and self.tokens[w].capitalize:
                result.append(word.upper())
            else:
                result.append(word)
        return ' '.join(result)


sentence = Sentence('hello world for this fucking year')
sentence[6].capitalize = True
print(sentence)
