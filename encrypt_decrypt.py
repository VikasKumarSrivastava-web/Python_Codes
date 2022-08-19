alphabets =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(text,shift):
    encrypted_msg=''
    for item in text:
        pos = alphabets.index(item)
        n_pos = pos + shift
        new_letter =alphabets[n_pos]
        encrypted_msg +=new_letter
               
    print(f" the encrypted msg is {encrypted_msg}")

def decrypt(text,shift):
    derypted_msg=''
    for item in text:
        pos = alphabets.index(item)
        n_pos = pos - shift
        new_letter =alphabets[n_pos]
        derypted_msg +=new_letter
    print(f"the decrypted msg is : {derypted_msg}")           
       
def want_more():
    input_to_continue=input("want to continue, Y/N : ").upper()
    if input_to_continue =='Y':
        return False
    elif input_to_continue =='N':
        return True
    else:
        return -1
    

is_end= False

while not is_end:
    direction=input("encrypt or decrypt ?").lower()
    if direction == "encrypt":
        user_input=input("Give the word for encryption: ").lower()
        shift=int(input("please provide the shift: "))
        encrypt(text=user_input,shift=shift)
        is_end=want_more()
        if is_end==-1:
            print("invalid entry ,try again")
            is_end=True
    elif direction =="decrypt":
        user_input=input("Give the word for decryption: ").lower()
        shift=int(input("please provide the shift: "))
        decrypt(text=user_input,shift=shift)
        is_end=want_more()
        if is_end==-1:
            print("invalid entry, try again")
            is_end=True
    else:
        print("Invalid entry")
    
