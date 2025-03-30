num = int(input())

for i in range(num):
    sentence = input()
    word_list = sentence.split()

    for i,word in enumerate(word_list):
        word = list(word)
        word.reverse()
        new_word = "".join(word)

        if i == 0:
            new_sentence = new_word
        else:
            new_sentence = new_sentence + ' ' + new_word
        
    print(new_sentence)