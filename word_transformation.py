begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog",  "cog"]

temp_word = ""
count_index = 0
while True:
    count_index += 1
    if not temp_word:
        temp_word = begin_word

    word_matches = {}
    for word in word_list:
        word_matches[word] = 0
        for index, letter in enumerate(temp_word):
            if word[index] == letter:
                word_matches[word] += 1

    correct_match = [_ for _ in word_matches if word_matches[_] == len(begin_word) - 1]
    if len(correct_match) == 1:
        print(f'{temp_word} -> {correct_match[0]}')
        temp_word = correct_match[0]
        word_list.remove(correct_match[0])
    else:
        raise Exception('Zero tranforms')

    if temp_word == end_word:
        print(f'Done by {count_index} iterations')
        break
