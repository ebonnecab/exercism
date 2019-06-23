def is_pangram(sentence):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for letter in alpha:
        if letter not in sentence.lower():
            return False

    return True