def reverseWordsInString(string):
    word = ''
    final_string = ''
    for i in range(len(string)-1, -1, -1):
        if string[i] != ' ':
            word = string[i] + word
        if string[i] == ' ':
            final_string += word + string[i]
            word = ''
        if i == 0:
            final_string += word

    return final_string
