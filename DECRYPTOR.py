# letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
#            'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
#            'z': 26, '!': 27, '@': 28, '#': 29, '$': 30, '%': 31, '&': 32, '*': 33, '?': 34, ' ': 35}
import time

letters = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ж': 7, 'з': 8, 'и': 9, 'й': 10, 'к': 11, 'л': 12, 'м': 13,
           'н': 14, 'о': 15, 'п': 16, 'р': 17, 'с': 18, 'т': 19, 'у': 20, 'ф': 21, 'х': 22, 'ц': 23, 'ч': 24, 'ш': 25,
           'щ': 26, 'ъ': 27, 'ы': 28, 'ь': 29, 'э': 30, 'ю': 31, 'я': 32,

           '!': 33,'0': 34, '@': 35,'1': 36, '#': 37,'2': 38, '$': 39,'3': 40, '%': 41,'4': 42, '&': 43,'5': 44, '*': 45,
           '6': 46, '7': 47,'?': 48,'8': 49, ' ': 50,'9': 51, ',': 52, '.':53, '-': 54, '\"': 55, '/': 56, '\\': 57, '+': 58,
           ';': 59, '(': 60, ')': 61, '_': 62,

           'a': 63, 'b': 64, 'c': 65, 'd': 66, 'e': 67, 'f': 68, 'g': 69, 'h': 70, 'i': 71, 'j': 72, 'k': 73, 'l': 74, 'm': 75,
           'n': 76, 'o': 77, 'p': 78, 'q': 79, 'r': 80, 's': 81, 't': 82, 'u': 83, 'v': 84, 'w': 85, 'x': 86, 'y': 87, 'z': 88
           }


print('                     DECRYPTOR Caesar v2.1                       ')

def get_text():
    global RE_DECODE_T
    DECODE_TEXT = input("Введите текст для декода: ")
    RE_DECODE_T = ''
    for i in DECODE_TEXT:
        # print(i)
        RE_DECODE_T += i

    return RE_DECODE_T



def decode_key():
    g_text = get_text()
    decoded = g_text.split(':')
    if len(decoded[0]) != 5:
        print('')
        print('█████████████ ERROR █████████████')
        print('      Длина ключа не равна 5     ')
        print('')
        decode_text()
    else:


        dec_letter = []
        num_letter = []

        for i in decoded[0]:
            dec_letter.append(i)

        for i in dec_letter:
            for k, v in letters.items():
                if k == i:

                    num_letter.append(v)
                else:
                    continue
        decrypted_number = num_letter[0] + num_letter[1] - num_letter[2] + num_letter[3] - num_letter[4]
        return decrypted_number, decoded[1]


def decode_text():
    global decode_k

    decode_k = decode_key()

    key_word = decode_k[1]

    revers = key_word[::-1]
    dec_num = []
    for i in revers:
        for k, v in letters.items():
            if k == i:
                dec_num.append(v)

            else:
                continue
    finish = []
    for i in dec_num:
        ch = i - decode_k[0]

        if ch <= 0:
            finish.append(len(letters) + ch)
        else:
            finish.append(ch)

    end_decode = []
    end = ''
    for i in finish:
        for k, v in letters.items():
            if v == i:
                end_decode.append(k)

            else:
                continue
    for i in end_decode:
        end += i
    print('██████████ ENCRYPTED ██████████')
    print(end)
    print('')
    decode_text()

decode_text()
