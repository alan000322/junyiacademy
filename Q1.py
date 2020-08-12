#### function
def Reverse_words(word):
    reverse = ""
    for pos in range(len(word)-1 , -1, -1):
        reverse += word[pos]
    return reverse

def f(words):
    reverse_words = ""
    if words.find(" ") != -1:
        Words_list = words.split(" ")
        for word in Words_list:
            reverse_word = Reverse_words(word)
            reverse_words += reverse_word + " "
    else:
        reverse_words += Reverse_words(words)

    return reverse_words.strip()
    

#### assertion
assert f('junyiacademy') == "ymedacaiynuj"
assert f('flipped class room is important') == "deppilf ssalc moor si tnatropmi"
assert f('I am a college student') == "I ma a egelloc tneduts"