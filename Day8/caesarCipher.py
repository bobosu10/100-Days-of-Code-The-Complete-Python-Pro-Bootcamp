import art

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesarCipher(text, shift, encode_or_decode):
    saveText = ""
    if encode_or_decode == "decode":
        shift *= -1
    for letter in text:
        if letter in letters:
            position = letters.index(letter)
            new_position = (position + shift) % 26
            saveText += letters[new_position]
        else:
            saveText += letter
    print(f"Here is the {encode_or_decode}d result: {saveText}")

print(art.logo)
continuar = True

while continuar:
    encode_or_decode = input("Type encode to encrypt or decode to decrypt:\n")
    text = input(f"Type text to be {encode_or_decode}:\n")
    shift = int(input(f"Type shift to be {encode_or_decode}:\n"))

    caesarCipher(text, shift, encode_or_decode)

    deve_continuar = input("Do you want to continue (yes/no)?\n").lower()
    if deve_continuar == "no":
        continuar = False
        print("GOODBYE!!!")

    