alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def encryption(text,shift_key):
    cipher_text=" "
    for char in text:
        position=alphabets.index(char)
        new_position=(position+shift_key)%26
        cipher_text +=alphabets[new_position]
    print(f"here is the text after encryption: {cipher_text}")
def decryption(cipher_text,shift_key):
    plain_text=" "
    for char in cipher_text:
        position=alphabets.index(char)
        new_position=(position-shift_key)%26
        plain_text+=alphabets[new_position]
    print(f"here is the text after decryption: {plain_text}")
want = True
while(want==True):
    choice=input("Type Encrypt for encryption & Type Decrypt for Decryption: ")
    text=input("enter the message")
    shift_key=int(input("enter the shift key"))
    if choice=="Encrypt":
        encryption(text,shift_key)
    elif choice=="Decrypt":
        decryption(text,shift_key)
    if(want==False):
        print("ok good bye")
    f=input("you want to continue: ")
    if(f == "yes"):
        want = True
    else:
        want = False