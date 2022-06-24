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

















#TODO-1: Import and print the logo from art.py when the program starts. 
#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).
# TODO-3: What happens if the user enters a number/symbol/space?
# Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
# e.g. start_text = "meet me at 3"
# end_text = "•••• •• •• 3"
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.