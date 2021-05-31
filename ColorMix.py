def ColorMix(color1, color2):
    '''
    This functions takes two hex colors codes in parameters and return the hex code of these two colors mixed
    Example:
    ColorMix("0000ff","ffff00") #blue + yellow
    >>>'7f7f7f' #Dark Green
    '''
    color1L = []
    color2L = []
    colorF = []
    for i in range(3):
        color1L.append(color1[2*i:2*i+2])
        color2L.append(color2[2*i:2*i+2])
    for i in range(3):
        value1 =int("0x"+color1L[i], 16)
        value2 =int("0x"+color2L[i], 16)
        if(value1 + value2)/2 < 16:
            number = hex(int((value1 + value2)/2))
            number+=number[2]
            number = list(number)
            number[2] = "0"
            number = "".join(number[0:])
            colorF.append(number)
        else:
            colorF.append(hex(int((value1 + value2)/2)))
    return str(colorF[0][2:] + colorF[1][2:] + colorF[2][2:])
