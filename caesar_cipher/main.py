from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    end_text = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if direction == "encode":
                new_index = index + shift
                if new_index > 25:
                    new_index = new_index - 26
                end_text += alphabet[new_index]
            elif direction == "decode":
                new_index = index - shift
                if new_index < 0:
                    new_index = new_index + 26
                end_text += alphabet[new_index]
        else:
            end_text += letter

    print(f"The {direction}d text is: {end_text}")
        

print(logo)

is_play = True

while is_play:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if shift > 26:
        shift = shift % 26
    
    caesar(text, shift, direction)
    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if play_again == "no":
        is_play = False