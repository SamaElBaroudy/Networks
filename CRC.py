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


# main function of trasmitter

def Transmitter(Data, Divisor):
    length_Divisor = len(Divisor)

    # Appends n-1 zeroes at end of data
    appended_data = Data + '0' * (length_Divisor - 1)
    remainder = mod2div(appended_data, Divisor)

    # Append remainder in the original data
    Transmission_Data = Data + remainder
    return Transmission_Data


G = 0
Message = 0


def readmessage(filename):
    text_file = open(filename, "r")
    lines = text_file.readlines()
    text_file.close()
    lines[0] = lines[0].replace("\n", "")
    msg = lines[0]
    Gen = lines[1]
    return msg, Gen


def Generator(path):
    Msg, Generator = readmessage(path)
    global G
    G = Generator
    Transmission_Data = Transmitter(Msg, Generator)
    global Message
    Message = Transmission_Data
    # return Transmission_Data


def Verifier():
    global Message
    global G
    Remainder = mod2div(Message, G)
    if (int(Remainder) == 0):
        print("message is correct")
    else:
        print("message is not correct")


def alter(index):
    global Message

    if (Message[index - 1] == "0"):
        Message_List = list(Message)
        Message_List[index - 1] = "1"
        Message = str(Message_List)
    else:
        Message_List = list(Message)
        Message_List[index - 1] = "0"
        Message = str(Message_List)


def Gen_Verf(path):
    Generator(path)
    Verifier()


def Gen_Alt_Verf(path, index):
    Generator(path)
    alter(index)
    Verifier()


Command = input()

if Command.find("alter") != -1:
    parsed = Command.split(" ")
    path = parsed[2]
    index = parsed[5]
    Gen_Alt_Verf(path, int(index))

else:
    parsed = Command.split(" ")
    path = parsed[2]

    Gen_Verf(path)
k = input("press any key to close")