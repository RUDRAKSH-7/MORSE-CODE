try:
    from colorama import Fore, Style ;
    green = Style.BRIGHT+Fore.LIGHTGREEN_EX
    cyan = Style.BRIGHT+Fore.CYAN
    red = Style.BRIGHT+Fore.RED
    yellow = Style.BRIGHT+Fore.YELLOW
    white = Style.BRIGHT+Fore.WHITE
    reset = Style.RESET_ALL
    magenta = Style.BRIGHT+Fore.MAGENTA
    grey = Style.BRIGHT+Fore.BLACK
except ImportError or NameError:
    green = cyan = red = yellow = white = magenta = reset = ""
from os import system ; import time as t

chars = [
'a','.-',       'b','-...',     'c','-.-.',    'd','-..',
'e','.',        'f','..-.',     'g','--.',     'h','....',
'i','..',       'j','.---',     'k','-.-',     'l','.-..',
'm','--',       'n','-.',       'o','---',     'p','.--.',
'q','--.-',     'r','.-.',      's','...',     't','-',
'u','..-',      'v','...-',     'w','.--',     'x','-..-',
'y','-.--',     'z','--..',     '1','.----',   '2',"..---",
'3','...--',    '4','....-',    '5','.....',   '6','-....',
'7','--...',    '8','---..',    '9','----.',   '0','-----'
]

class convert:
    def morse_to_english(code):
        if not "  " in code:
            string = str(code).split(" ")
            result = ""
            print(f"\n{cyan}STRING -> {reset}",end="")
            for i in string:
                result += chars[chars.index(i)-1]  
            print(green+result.capitalize())
        else:
            string = str(code).split("  ")
            result = ""
            print(f"\n{cyan}STRING -> ",end="")
            for i in string:
                breakdown = str(i).split(" ")
                for i in breakdown:
                    result += chars[chars.index(i)-1]  
                result += " "
            print(green+result.capitalize())

    def english_to_morse(string):
        if not " " in string:
            result= ""
            print(f"\n{cyan}CODE -> ",end = " ")
            for i in string.lower():
                result += chars[chars.index(i)+1]+" "
            print(result)
        else:
            code = str(string.lower()).split(" ")
            result = ""
            print(f"\n{cyan}CODE -> ",end = " ")
            for i in code:
                for j in i:
                    result += chars[chars.index(j)+1]+" "
                result += " "
            print(result)

def instructions():
    system('cls')
    print(white+"\n\n\n\n\n\n\n1. String should only be numbers or English Letters.")
    print("2. Morse code should be for numbers and alphabets.")
    print("3. Morse code letters are seperated using one space.")
    print("4. Morse code Words are separated using double spaces.")
    print("5. String should not contain any punctuations.")
    input("\n\n                 press enter...")
    return

system('cls')
while True:
    print("\n\n\n\n\n\n")
    print(f"{cyan}                MORSE CONVERTER : \n")
    print(f"{magenta}[1] ENG --> MORSE           {red}[2] MORSE --> ENGLISH{reset}\n\n                  [3] EXIT")
    print(f"{grey}\n             [i] for instructions")
    choice = str(input(F"\n{green}                  OPTION : {white}"))
    if choice not in ['1','2','3','i']:
        print(F"{red}\t\t\t# RETRY")
        t.sleep(1)
        system('cls')
        continue
    if choice == '1':
        system('cls')
        try:
            string = str(input(f"{green}STRING : {white}"))
            convert.english_to_morse(string)
            print(reset)
        except ValueError:
            system('cls')
            print(F"{red}\t\t\t# RETRY")
            t.sleep(1)
            system('cls')
            continue
    elif choice == '2':
        system('cls')
        try:
            code = str(input(f"{cyan}CODE : {green}"))
            convert.morse_to_english(code)
            print(reset)
        except ValueError:
            system('cls')
            print(F"{red}\t\t\t\t# RETRY")
            t.sleep(1)
            system('cls')
            continue
    elif choice == '3':
        break
    elif choice == 'i':
        system('cls')
        instructions()
        system('cls')
quit()
