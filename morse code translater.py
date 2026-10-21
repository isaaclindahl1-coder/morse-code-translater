morse_code_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----"
    } 

reverse_morse_dict = {}

for key, value in morse_code_dict.items():
    reverse_morse_dict[value] = key

english_text = input("Enter what you would like to translate: ").upper()
morse_result = ""

def translate_to_morse(english_text):
    morse_result = ""
    for letter in english_text:
        if letter in morse_code_dict:
            morse_result += morse_code_dict[letter] + " "
        elif letter == " ":
            morse_result = morse_result.rstrip() + "   "

    return morse_result.rstrip()

print(translate_to_morse(english_text))


morse_code = input("Enter the morse code you want to decode: ")
english_result = ""

def decode_morse():





# for letter in english_text:
#     print(letter)

# for letter in english_text:
#     if letter in morse_code_dict:
#         print(morse_code_dict[letter])



# morse_code = input("Enter what you would like to be translated to morse code: ")
# morse_word = morse_code.split("   ")
# morse_letter = morse_word.split(" ")
