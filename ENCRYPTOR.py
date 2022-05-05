from random import randint

# letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
#            'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
#            'z': 26,
#            '!': 27, '@': 28, '#': 29, '$': 30, '%': 31, '&': 32, '*': 33, '?': 34, ' ': 35}
letters = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ж': 7, 'з': 8, 'и': 9, 'й': 10, 'к': 11, 'л': 12, 'м': 13,
           'н': 14, 'о': 15, 'п': 16, 'р': 17, 'с': 18, 'т': 19, 'у': 20, 'ф': 21, 'х': 22, 'ц': 23, 'ч': 24, 'ш': 25,
           'щ': 26, 'ъ': 27, 'ы': 28, 'ь': 29, 'э': 30, 'ю': 31, 'я': 32,

           '!': 33,'0': 34, '@': 35,'1': 36, '#': 37,'2': 38, '$': 39,'3': 40, '%': 41,'4': 42, '&': 43,'5': 44, '*': 45,
           '6': 46, '7': 47,'?': 48,'8': 49, ' ': 50,'9': 51, ',': 52, '.':53, '-': 54, '\"': 55, '/': 56, '\\': 57, '+': 58,
           ';':59, '(': 60, ')': 61, '_': 62,

           'a': 63, 'b': 64, 'c': 65, 'd': 66, 'e': 67, 'f': 68, 'g': 69, 'h': 70, 'i': 71, 'j': 72, 'k': 73, 'l': 74,
           'm': 75,
           'n': 76, 'o': 77, 'p': 78, 'q': 79, 'r': 80, 's': 81, 't': 82, 'u': 83, 'v': 84, 'w': 85, 'x': 86, 'y': 87,
           'z': 88
           }

print('                     ENCRYPTOR Caesar v2.1                       ')
print('-----------------------------------------------------------------')
print("|    WARNING! Symbol : will be replaced by ; automatically      |")
print("|         Upper letters will be replaced with lower             |")
print('-----------------------------------------------------------------')

def key_word():
    xyx = randint(3, len(letters)-5)
    return xyx

def review():
    key = []
    did = 0
    global check, xyz

    while did < 1:
        x = 0
        while x != 5:
            for k, v in letters.items():
                if v == randint(1, len(letters)-5):
                    key.append(k)
                    x += 1
                    if len(key) == 5:
                        break

        checker = []
        check = ''
        for i in key:
            checker.append(letters[i])
            check += i
        xy = checker[0] + checker[1] - checker[2] + checker[3] - checker[4]
        global key_word
        xyz = key_word()
        if xy != xyz:
            review()
        elif xy == xyz:
            did += 1
        break
    return xyz, check

def test():
    global rew
    rew = review()
    sums = []
    decode_word = input("Введите предложение: ").lower()
    decode_word = decode_word.replace('\'', '"')
    decode_word = decode_word.replace(':', ';')
    decode_word = decode_word.replace('^', '')
    decode_word = decode_word.replace('ё', 'е')

    for i in decode_word:
        sums.append(letters[i])

    fin_num = []
    for i in sums:
        i += rew[0]
        fin_num.append(i)

    ffin_num = []
    for i in fin_num:

        if i > len(letters):
            i -= len(letters)
            ffin_num.append(i)
        else:
            ffin_num.append(i)

    coded_word = []
    for i in ffin_num:
        for k, v in letters.items():
            if v == i:
                coded_word.append(k)
            else:
                continue

    end = ''
    for i in coded_word[::-1]:
        end += i
    print('██████████ DECRYPTED ██████████')
    print(rew[1] + ':' + end.strip())
    print('')
    test()

test()
