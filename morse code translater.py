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

morse_result = ""
english_text = ""
def translate_to_morse():
    english_text = input("Enter what you would like to translate to Morse code: ").upper()
    morse_result = ""
    for letter in english_text:
        if letter in morse_code_dict.keys():
            morse_result += morse_code_dict[letter] + " "
        elif letter == " ":
            morse_result = morse_result.rstrip() + "   "

    return morse_result.rstrip()



english_result = ""

def decode_morse():
    morse_code = input("Enter the morse code you want to decode: ").upper()
    morse_word = morse_code.split("   ")
    english_result =""

    for word in morse_word:
        morse_letters = word.split()
        for letter in morse_letters:
            if letter in reverse_morse_dict:
                english_result += reverse_morse_dict[letter]
        english_result += " "
    return english_result.strip()


def main_menu():
    while True: 
        print("Select an opption:")
        print("1. Encode text to Morse code")
        print("2. Decode Morse code to text")
        print("3. Exit")
        choice = input("Select wich one you would like to do: ")
        if choice == "1":
            result = translate_to_morse()
            print(result)
        elif choice == "2":
            result2 = decode_morse()
            print(result2)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("That is not a valid choice please try again.")
main_menu()

