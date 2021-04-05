import base64
from os import system
from colorama import init, deinit, Fore, Back, Style
init(autoreset=True)
"""for colored output run from command prompt on windows"""

banner = """"██████╗  █████╗ ███████╗███████╗ ██████╗ ██╗  ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██║  ██║
██████╔╝███████║███████╗█████╗  ███████╗ ███████║
██╔══██╗██╔══██║╚════██║██╔══╝  ██╔═══██╗╚════██║
██████╔╝██║  ██║███████║███████╗╚██████╔╝     ██║
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝      ╚═╝"""

print(Fore.RED+banner)

def encode(txt):
    encoded = base64.b64encode(encode_txt)
    print("your encoded text for '{}' is : ".format(encode_txt.decode("utf-8")),encoded.decode("utf-8"))

def decode(txt2):
    decoded = base64.b64decode(decode_txt)
    print("your decoded text for '{}' is : ".format(decode_txt.decode("utf-8")),decoded.decode("utf-8"))


print(Fore.YELLOW + "*****************************************************\n*      Simple Program for Base64 Conversion         *\n*****************************************************\n")
print(Fore.WHITE + "Type 1,2 or 3 to quit\n1] covert to base64\n2] conver from base64\n")

try:
    while True:
        option = input("enter option option[1,2,3] : ")
        if option == "1":
            in_enco  = input("enetr txt to encode : ")
            encode_txt =  in_enco.encode()
            encode(encode_txt)
        elif option == "2":
            in_deco = input("enetr txt to decode : ")
            decode_txt = in_deco.encode()
            decode(decode_txt)
        elif option == "3":
            break
        else:
            pass
except:
    print(Fore.RED + "something went wrong, it maybe because text you enterd is wrong try again.")

"""created by Atul"""
