# Returns XOR of 'a' and 'b'(both of same length)
def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)

# Performs the Division
def mod2div(appended_data, Divisor):

    pick = len(Divisor)
    tmp = appended_data[0: pick]

    while pick < len(appended_data):

        if tmp[0] == '1':
            tmp = xor(Divisor, tmp) + appended_data[pick]

        else:
            tmp = xor('0' * pick, tmp) + appended_data[pick]

        pick += 1

    if tmp[0] == '1':
        tmp = xor(Divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    remainder = tmp
    return remainder
#main function of trasmitter

def Transmitter(Data , Divisor):
    length_Divisor = len(Divisor)

    # Appends n-1 zeroes at end of data
    appended_data = Data + '0' * (length_Divisor - 1)
    remainder = mod2div(appended_data, Divisor)

    # Append remainder in the original data
    Transmission_Data = Data + remainder
    return Transmission_Data
