import pykakasi

kks = pykakasi.kakasi()

# Define the Morse code conversion function
def convert_to_morse_code(text):
    # Add your Morse code conversion algorithm here
    morse_code = {
        # 欧文
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', #'.':'.-.-.-', ',': '--..--',
        '?': '..--..', '-': '-....-', '(': '-.--.', ')': '-.--.-', '/': '-..-.', '=': '-...-', '+': '.-.-.', 
        '*': '-..-', '@': '.--.-.', '^':'.....--', '¥': '-.----', 
        # 和文
        'あ': '--.--', 'い': '.-', 'う': '..-', 'え': '-.---', 'お': '.-...', 'か': '.-..', 'き': '-.-..', 
        'く': '...-', 'け': '-.--', 'こ': '----', 'さ': '-.-.-', 'し': '--.-.', 'す': '---.-', 'せ': '.---.', 
        'そ': '---.', 'た': '-.', 'ち': '..-.', 'つ': '.--.', 'て': '.-.--', 'と': '..-..', 'な': '.-.', 
        'に': '-.-.', 'ぬ': '....', 'ね': '--.-', 'の': '..--', 'は': '-...', 'ひ': '--..-', 'ふ': '--..', 
        'へ': '.', 'ほ': '-..', 'ま': '-..-', 'み': '..-.-', 'む':'-', 'め': '-...-', 'も': '-..-.', 
        'や': '.--', 'ゆ':'-..--', 'よ': '--', 'ら': '...', 'り': '--.', 'る':'-.--.', 'れ': '---', 'ろ': '.-.-', 
        'わ': '-.-', 'ゐ':'.-..-', 'ゑ': '.--..', 'を': '.---', 'ん': '.-.-.', 'が': '.-.. ..', 'ぎ': '-.-.. ..', 
        'ぐ': '...- ..', 'げ':'-.-- ..', 'ご': '---- ..', 'ざ': '-.-.- ..', 'じ':'--.-. ..', 'ず': '---.- ..', 
        'ぜ': '.---. ..', 'ぞ':'---. ..', 'だ': '-. ..', 'ぢ': '..-. ..', 'づ':'.--. ..', 'で': '.-.-- ..', 
        'ど': '..-.. ..', 'ば':'-... ..', 'び': '--..- ..', 'ぶ': '--.. ..', 'べ':'. ..', 'ぼ': '-.. ..', 
        'ぱ': '-... ..--.', 'ぴ':'--..- ..--.', 'ぷ': '--.. ..--.', 'ぺ': '. ..--.', 'ぽ': '-.. ..--.', 
        'ー': '.--.-', '、': '.-.-.-', '（': '-.--.-', '）': '.-..-.', '゛': '..', '゜': '..--.', '？': '-...-.', 
        '！':'.--.-' 
    }
    
    res_dict = kks.convert(text)
    result = ''.join([item['hira'] for item in res_dict])

    # かな文字から一文字ずつ取って、モールスに直す
    morse_text = ""
    for char in result:
        if char.upper() in morse_code:
            morse_text += morse_code[char.upper()] + " "
        elif char == " ":
            morse_text += "/ "
        else:
            morse_text += "[" +char+ "]"
    return morse_text

