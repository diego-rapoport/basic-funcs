def convert_hex_to_dec(hexa):
    '''
        A hexadecimal to decimal converter. For now just converts the hexadecimals
        like 0x0b34.

        So the basic is that we take the reversed hexadecimal up to 0x, ex: 0x0b34 turns into
        43b0, and each number is multiplied by 16 in the power of it's index. Then we have
        4 * 16 ** 0, 3 * 16 ** 1 and so on. Finally we add all the values.

        Remembering that those letters take integers values:
            A = 10
            B = 11
            C = 12
            D = 13
            E = 14
            F = 15
    '''

    # First we set a dictionary with dict comprehension to easily convert a to 10, b to 11 and so on
    array = {key:index+10 for index, key in enumerate('abcdef')}

    # Then we return the sum of the conversion according to the basic hexadecimal to decimal conversion
    return sum([int(val)*16**index if val not in array.keys() else int(array[val])*16**index for index, val in enumerate(hexa[:hexa.find('x'):-1])])
