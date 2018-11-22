def Verifier():
    global Message
    global G
    Remainder = mod2div(Message,G)
    if (int(Remainder)== 0):
        print("message is correct")
    else:
        print("message is not correct")