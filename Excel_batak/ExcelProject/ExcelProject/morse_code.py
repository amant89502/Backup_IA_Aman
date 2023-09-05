
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ',': '--..--', ':': '---...', "'": '.----.', '!': '-.-.--',
    '.': '.-.-.-', '?': '..--..', ' ': '/'
}


def text_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char in morse_dict:
            morse_code.append(morse_dict[char])
        else:
            morse_code.append(' ')

    return ' '.join(morse_code)



input_text = "Aman Tiwari"
translated_text = text_to_morse(input_text)
print(translated_text)
