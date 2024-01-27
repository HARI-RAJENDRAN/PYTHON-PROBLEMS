import random
print("-------------------------------------")
send_msg=input("Enter the msg to change encryption:")
print("-------------------------------------")
def again():
    
    encry = ""
    keys=[]
    for  i in send_msg:
        num=random.randint(1,200)  
        funt_1 = ord(i) + num
        ench = chr(funt_1)
        encry += ench
        keys.append(num)

    print("-------------------------------------")
    print("Encryption Message is:",encry)
    print("-------------------------------------")
    print("Random keys used for encryption:", keys)
    print("-------------------------------------")
    def dec():
        decrypted_msg = ""
        for i in range(len(encry)):
            funt_1 = ord(encry[i]) - keys[i]
            dec_msg = chr(funt_1)
            decrypted_msg += dec_msg
        print("Decrypted message:", decrypted_msg)
    user_a=input("you want to see your decrypted message[yes/no]:")
    if(user_a=="yes"):
        dec()
    else:
        exit()
if(send_msg,str):
    again()
else:
    print("error")
