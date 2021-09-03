vowel_list = ['A', 'E', 'I', 'O', 'U']
consonants_list = ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M',
                   'N', 'P', 'Q', 'S', 'T', 'V', 'X', 'Z', 'H', 'R', 'W', 'Y']


def check_string(string):
    kk = 0
    for index in range(len(vowel_list)):
        pp = string.count(vowel_list[index])
        kk = kk + pp
    return kk


def alpha_string(string):
    kk = 1
    for index in range(len(vowel_list)):
        pp = string.count(vowel_list[index])
        if pp > kk:
            kk = pp
    return kk


def contt_string(string):
    kk = 1
    for index in range(len(consonants_list)):
        pp = string.count(consonants_list[index])
        if pp > kk:
            kk = pp
    return kk


number_of_strings = int(input(""))
list_strings = []
for index in range(number_of_strings):
    each_string = input("")
    list_strings.append(each_string)

for index in range(number_of_strings):
    length_of_particular_string = len(list_strings[index])
    mx = check_string(list_strings[index])
    cx = length_of_particular_string - mx
    kx = contt_string(list_strings[index])
    sx = alpha_string(list_strings[index])
    if (cx == 0 and mx == sx) or (mx == 0 and cx == kx):
        P = 0
        print(f'Case #{index+1}: {P}')
    elif (cx == 0 and mx == length_of_particular_string) or (mx == 0 and cx == length_of_particular_string):
        print(f'Case #{index+1}: {length_of_particular_string}')
    else:
        if cx > mx or cx == mx:
            if cx == kx:
                print(f'Case #{index+1}: {mx}')
            else:
                px = cx + 2*(mx-sx)
                qx = mx + 2*(cx-kx)
                print(f'Case #{index+1}: {min(px,qx)}')
        elif mx > cx:
            if mx == sx:
                print(f'Case #{index+1}: {cx}')
            else:
                px = cx + 2*(mx-sx)
                qx = mx + 2*(cx-kx)
                print(f'Case #{index+1}: {min(px,qx)}')
