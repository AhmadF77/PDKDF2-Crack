################################################################################################
                                                                                                #
# Author  : Ahmad faiz alnajada                                                                  #
#                                                                                                 #
# python script for cracking PDKDF2-HMAC-SHA256 hash                                               #
#                                                                                                 #
# how to use : python pdkdf2_crack.py -hash <hash file> -wordlist <wordlist>                     #
                                                                                                #
################################################################################################

from werkzeug.security import check_password_hash
import argparse

##### help menu and take arguments from the user #####
help = argparse.ArgumentParser(description="python script for cracking PDKDF2-HMAC-SHA256 hash")
help.add_argument("-hash",help="enter the hash file",required=True)
help.add_argument("-wordlist",help="enter your wordlist wordlist",required=True)
args = help.parse_args()

wordlist = f"{args.wordlist}"
hash = args.hash

##### open the hash file and take the hash #####
with open(hash , "r") as p_hash :
    hash = p_hash.read().strip()
    print(hash)

print("start cracking .........")

##### open the wordlist file and start cracking #####
with open(wordlist , "r" , encoding="utf-8" , errors="ignore") as file :
    for password in file :
        password = password.strip()
        if check_password_hash(hash , password) :
            print(f"it is your lucky day, here is your password: {password}")
            exit()
    print("you are not lucky today, nothing was found")





