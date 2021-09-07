alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def cypher(start_text, shift_amt, Cpyher_direction):
    end_text = ''
    if Cpyher_direction == "decode":
            shift_amt *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        
        new_pos = (position + shift_amt) % 26
        end_text += alphabet[new_pos]
    
    print( f"The {direction}d text is {end_text}")

cypher(start_text = text, shift_amt = shift, Cpyher_direction = direction)