try:
    from colorama import Fore, Style ;
    green = Style.BRIGHT+Fore.LIGHTGREEN_EX
    cyan = Style.BRIGHT+Fore.CYAN
    red = Style.BRIGHT+Fore.RED
    yellow = Style.BRIGHT+Fore.YELLOW
    white = Style.BRIGHT+Fore.WHITE
    reset = Style.RESET_ALL
    magenta = Style.BRIGHT+Fore.MAGENTA
except ImportError or NameError:
    green = cyan = red = yellow = white = magenta = reset = ""
from os import system ; import time as t

chars = [
'a' , '.-','b','-...',
'c','-.-.','d','-..',
'e' , '.','f','..-.',
'g','--.','h','....',
'i','..','j','.---',
'k','-.-','l','.-..',
'm','--','n','-.',
'o','---','p','.--.',
'q','--.-','r','.-.',
's','...','t','-',
'u','..-','v','...-',
'w','.--','x','-..-',
'y','-.--','z','--..'
]

class convert:
    def morse_to_english(code):
        if not "  " in code:
            string = str(code).split(" ")
            result = ""
            print(f"\n{cyan}STRING -> {reset}",end="")
            for i in string:
                result += chars[chars.index(i)-1]  
            print(green+result)
        else:
            string = str(code).split("  ")
            result = ""
            print(f"\n{cyan}STRING -> ",end="")
            for i in string:
                breakdown = str(i).split(" ")
                for i in breakdown:
                    result += chars[chars.index(i)-1]  
                result += " "
            print(green+result)

    def english_to_morse(string):
        if not " " in string:
            result= ""
            print(f"\n{cyan}CODE -> ",end = " ")
            for i in string:
                result += chars[chars.index(i)+1]+" "
            print(result)
        else:
            code = str(string).split(" ")
            result = ""
            print("\n{cyan}CODE -> ",end = " ")
            for i in code:
                for j in i:
                    result += chars[chars.index(j)+1]+" "
                result += " "
            print(result)

while True:
    print(f"{cyan}              MORSE CONVERTER : \n")
    print(f"{magenta}1. ENG --> MORSE           {red}2. MORSE --> ENGLISH{reset}")
    try:
        choice = int(input(F"\n{green}OPTION [ 1 ] | [ 2 ] : {white}"))
        if choice > 2:
            system('cls')
            print(F"{red}# RETRY")
            t.sleep(1)
            system('cls')
            continue
    except ValueError:
        system('cls')
        print(F"{red}# RETRY")
        t.sleep(1)
        system('cls')
        continue
    if choice == 1:
        system('cls')
        try:
            string = str(input(f"{green}STRING : {white}"))
            convert.english_to_morse(string)
            print(reset+"\n\n\n\n\n\n")
        except ValueError:
            system('cls')
            print(F"{red}# RETRY")
            t.sleep(1)
            system('cls')
            continue
    elif choice == 2:
        system('cls')
        try:
            code = str(input(f"{cyan}CODE : {green}"))
            convert.morse_to_english(code)
            print(reset+"\n\n\n\n\n\n")
        except ValueError:
            system('cls')
            print(F"{red}# RETRY")
            t.sleep(1)
            system('cls')
            continue
    input("press enter to quit...")
    quit()
