def add(num):
    return num + 1

def sub(num):
    return num - 1

num_to_word = { 1 : "one",
                2 : "two",
                3 : "three",
                4 : "four",
                5 : "five",
                6 : "six",
                7 : "seven",
                8 : "eight",
                9 : "nine",
                0 : "zero" }

def word_to_num(word):
    return { v : k for (k, v) in num_to_word.items() }[word]

def say(num):
    return [ num_to_word(int(x)) for x in str(num) ]

def count(words):
    num_str = ""
    for word in words:
        num_str.append(word_to_num[word])
    return int(num_str)


def shout(words):
    return [ word.upper() for word in words ]


def whisper():
    return [ word.lower() for word in words ]
