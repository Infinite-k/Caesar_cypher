from cipherart import logo

print (logo)

def caesar(directionn,plain_text,shift_amount):
    new_message = ""
    if shift > 26:
        shift_amount = shift_amount % 26
    
    for letter in plain_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if directionn == "encode":
                new_index = index + shift_amount
                new_message += alphabet[new_index]
            elif directionn == "decode":
                new_index = index - shift_amount
                new_message += alphabet[new_index]
        else:
            new_message += letter
    
    print (new_message)


wants_to_cotinue = True


while wants_to_cotinue == True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")    
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction,text,shift)
    yes_no = input ('Do you want to continue?Type "yes" or "no".\n')
    if yes_no == "no":
        wants_to_cotinue = False

