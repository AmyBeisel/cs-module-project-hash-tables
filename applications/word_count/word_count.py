def word_count(s):
    # name = s.replace('"', '').replace(':', '').replace(';','').replace(',','').replace('.','').replace('-','').replace('+','').replace('=','').replace('/','').replace('|','').replace('[', '').replace(']','').replace('{','').replace('}','').replace('(','').replace(')','').replace('*','').replace('^','').replace('&','').replace('\\','')
    # if name == '':
    #     return {}
    # split = name.lower().split()
    # words = {i:split.count(i) for i in split}
    # return words

    dict = {}
    ignoreChars = '" : ; , . - + = / \\ | [ ] { } ( ) * ^ &'.split()
    lower_s = s.lower()
    for i in ignoreChars:
        lower_s = lower_s.replace(i, " ")
    for word in lower_s.split():
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return dict

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))