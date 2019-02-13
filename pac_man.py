def load_map(add):
    f = open(add, "r")
    line=[]
    for x in f:
        line.append(x)
    return (line)

# pacman_map = load_map("map/level1.amap")
# for line in pacman_map:
#     print (line)

def simplify_map(array):
    new_array= []
    for i in array:
        l_sym=['═', '║', '╔', '╗', '╚', '╝']
        for sym in l_sym:
            i = i.replace(sym, '*')
            i = i.replace('·','.')
        new_array.append(i)
    return new_array

# pacman_map = load_map('map/level1.amap')
# simplified_map = simplify_map(pacman_map)
# for line in simplified_map:
#     print(line)



def prettify_map(array):
    converted_array1 = []
    for l in array:
        new_l = ''
        for i in l:
            i = i.replace('*', '═')
            i = i.replace('.','·' )   
            new_l += i
        converted_array1.append(new_l)
    converted_array2=[]
    for l in range(len(converted_array1)):
        converted_line = ''
        if l == len(converted_array1) -1:
            new_l = ''
            for i in converted_array2[l-1]:
                i = i.replace('*', '═')
                i = i.replace('.','·' )   
                new_l += i
            converted_array2.append(new_l)
        else:
            b = len(converted_array1[l])
            c = len(converted_array1[l+1])
            if b != 29:
                converted_array1[l] = converted_array1[l].replace('\n','')
                converted_array1[l] += ' '*(29-b)
            if c != 29:
                converted_array1[l+1] = converted_array1[l+1].replace('\n','')
                converted_array1[l+1] += ' '*(29-c)
            for i in range (b-1):
                a = converted_array1[l][i]
                if i == (b-1):
                    break
                elif a == '.':
                    a = a.replace('.','·' )
                elif converted_array1[l+1][i] == '═' and converted_array1[l-1][i] == '═':
                    a = a.replace('═', '║')
                converted_line += a
            converted_array2.append(converted_line)
    converted_array = []
    for l in range(len(converted_array2)):
        converted_line = ''
        if l == len(converted_array2) -1:
            for i in range (len(converted_array2[l])):
                a = converted_array2[l][i]
                if i == (len(converted_array2[l])-1):
                    pass
                elif a == '║' and converted_array2[l-1][i] == '║':
                    a = a.replace('║', '╚')
                elif a == '·' and converted_array2[l-1][i] == '·':
                    a = a.replace('·', '═')
                converted_line += a
            converted_array.append(converted_line)
        else:
            for i in range (len(converted_array2[l])):
                a = converted_array2[l][i]
                if i == (len(converted_array2[l])-1):
                    pass
                elif a == '═' and converted_array2[l][i+1] == '═' and converted_array2[l+1][i] == '═' and converted_array2[l][i-1] == '·':
                    a = a.replace('═', '╔')
                elif a == '═' and converted_array2[l][i-1] == '═' and converted_array2[l+1][i] == '═' and converted_array2[l][i+1] == '·':
                    a = a.replace('═', '╗')
                elif a == '═' and converted_array2[l][i+1] == '═' and converted_array2[l-1][i] == '═' and converted_array2[l][i-1] == '·':
                    a = a.replace('═', '╚')
                elif a == '═' and converted_array2[l][i-1] == '═' and converted_array2[l-1][i] == '═' and converted_array2[l][i+1] == '·':
                    a = a.replace('═', '╝')
                elif a == '║' and converted_array2[l][i+1] == '═' and converted_array2[l+1][i] == '║' and converted_array2[l][i-1] != '═':
                    a = a.replace('║', '╔')
                elif a == '═' and converted_array2[l][i+1] == '═' and converted_array2[l+1][i] == '║' and converted_array2[l][i-1] != '═' :
                    a = a.replace('═', '╔')
                elif a == '═' and converted_array2[l][i-1] == '═' and converted_array2[l+1][i] == '║' and converted_array2[l][i+1] != '═' :
                    a = a.replace('═', '╗')
                elif a == '║' and converted_array2[l][i-1] == '═' and converted_array2[l+1][i] == '║' and converted_array2[l][i+1] != '═':
                    a = a.replace('║', '╗')
                elif a == '═' and converted_array2[l][i+1] == '═' and converted_array2[l-1][i] == '║' and converted_array2[l][i-1] != '═':
                    a = a.replace('═', '╚')
                elif a == '═' and converted_array2[l][i-1] == '═' and converted_array2[l-1][i] == '║' and converted_array2[l][i+1] != '═':
                    a = a.replace('═', '╝')
                elif a == '═' and converted_array2[l+1][i] == ' ' and converted_array2[l-1][i] == '║' and converted_array2[l][i+1] == '═':
                    a = a.replace('═', '╚')
                elif a == '═' and converted_array2[l-1][i] == ' ' and converted_array2[l+1][i] == '║' and converted_array2[l][i+1] == '═':
                    a = a.replace('═', '╔')
                converted_line += a
            converted_array.append(converted_line)

    # final_array = []
    # for l in range(len(converted_array)):
    #     converted_line = ''
    #     if l == len(converted_array) -1:
    #         for i in range (len(converted_array[l])):
    #             a = converted_array[l]
    #             if i == (len(converted_array[l])-1):
    #                 if a == '║' and converted_array[l-1][i] == '║':
    #                     a = a.replace('║', '╝')
    #             converted_line += a
    #         final_array.append(converted_line)
    #     elif l == 0:
    #         for i in range (len(converted_array[l])):
    #             a = converted_array[l]
    #             if i == (len(converted_array[l])-1):
    #                     if a == '║' and converted_array[l][i-1] == '═' and converted_array[l+1][i] == '║':
    #                         a = a.replace('║', '╗')
    #             converted_line += a
    #         final_array.append(converted_line)
    #     else:
    #         for i in range (len(converted_array[l])):
    #             a = converted_array[l][i]
    #             if i == (len(converted_array[l])-1):
    #                 if a == '═' and converted_array[l][i-1] == '═' and converted_array[l-1][i] == '║' and converted_array[l+1][i] != '║':
    #                     a = a.replace('═', '╝')
    #                 elif a == '═' and converted_array[l][i-1] == '═' and converted_array[l+1][i] == '║' and converted_array[l-1][i] != '║':
    #                     a = a.replace('═', '╗')
    #                 elif a == '║' and converted_array[l][i-1] == '═' and converted_array[l-1][i] == '║':
    #                     a = a.replace('║', '╝')
    #                 # elif a == '║' and converted_array2[l][i-1] == '═' and converted_array2[l-1][i] == '║' and converted_array2[l+1][i] == '║':
    #                 #     a = a.replace('║', '╗')
    #             converted_line += a
    #         final_array.append(converted_line)
    return converted_array


pacman_map = load_map('map/level1.map')
prettified_map = prettify_map(pacman_map)
for line in prettified_map:
    print(line)


def compress_map_with_rle(array):
    new_array = []
    for line in array:
        line = line.replace('\n','')
        new_line = ''
        count = 1
        for i in range(len(line)):
            b = line[i]
            if i == (len(line)-1):
                if b == line[i-1]:
                    new_line = new_line + str(count) + b
                    count = 1
                else:
                    new_line = new_line + str(count) + b
                    count = 1
            elif line[i+1] == b:
                count+=1
            else:
                new_line = new_line + str(count) + line[i]
                count = 1
        new_array.append(new_line)
    return new_array

# pacman_map = load_map('./map/level1.map')
# compressed_map = compress_map_with_rle(pacman_map)
# for line in compressed_map:
#     print(line)
