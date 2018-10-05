CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',   '.': '.-.-.-', ' ': ' '
        }

CODE_REVERSED = {value:key for key,value in CODE.items()}

class Solution:

        def __new__(self, morseToEnglish, textToTranslate):
                if textToTranslate == '' or textToTranslate.count('    ') == 1:
                        return 'Invalid Morse Code Or Spacing'
                results = ''
                for x in textToTranslate.split('   '):
                        results += self.morse(x, morseToEnglish)+' '
                return results.lower().rstrip()

        def morse(value, flag):
                if flag:
                        return ''.join(CODE_REVERSED.get(i) for i in value.split())
                else:
                        return ' '.join(CODE.get(i.upper()) for i in value) 

if __name__ == '__main__':
        # false to convert from string to morse
        string_to_morse = Solution(False, 'HELLO WORLD')
        # true to convert from morse to string
        morse_to_string = Solution(True, '.... . .-.. .-.. ---   .-- --- .-. .-.. -..')
        print('String to Morse: |' + string_to_morse + '|')
        print('Morse to String: |' + morse_to_string + '|')