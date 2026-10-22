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

english_result = ""

def decode_morse():
    morse_code = input("Enter the morse code you want to decode: ")
    morse_word = morse_code.split("   ")
    english_result =""

    for word in morse_word:
        morse_letters = word.split()
        for letter in morse_letters:
            if letter in reverse_morse_dict:
                english_result += reverse_morse_dict[letter]
        english_result += " "
    return english_result.strip()
print(decode_morse())

def main_menu(person_input):  
    print("Select an opption:")
    print("1. Encode text to Morse code")
    print("2. Decode Morse code to text")
    print("3. Exit")
