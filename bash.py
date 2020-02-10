# author : @HUNTERTIK_
# -*- coding: utf-8 -*-

import os
import sys
import fileinput

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '√' + G + '] '
eror = R + '[' + W + '!' + R + ']'

banner = """
{}         _nnnn_{}        _________________
{}        dGGGGMMb{}      |                 |
{}       @p~qp~~qMb{}   ._| {}Bash Oubfuscate {}|
{}       M{}({}@{})({}@{}) {}M|{}  /  |_________________|
{}       @,{}----.{}JM|{}_/
{}      JS^{}\__/{}  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM    {}COEDED BY {}: {}ARIYAN
{}   FqM            MMMM    {}FB       {}: {}fb.com/HunterTheAriyan
{} __|'\ .        |\{}dS qML
{} |    `.       | `' \{}Zq
{}_)      \.{}___.{},|     .'
\____   ){}MMMMMP{}|   .'
     `-'       `--'
""".format(D,W,D,W,D,W,Y,W,D,W,D,W,D,W,D,W,D,Y,D,W,D,Y,D,G,W,G,D,G,W,G,Y,D,Y,D,Y,D,Y,D,Y)

banner2 = """
   {}[{}1{}]{} Encript      {}[{}2{}]{} Decrypt
""".format(G,W,G,W,G,W,G,W)

print banner
print banner2

def dekrip():
   try:
       sc = raw_input(ask + W + "Script " + G + "> " + W)
       f = open(sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")

       out = raw_input(ask + W + "Output" + G + " > " + W)
       f = open(out,'w')
       f.write(newdata)
       f.close()

       os.system("touch tes.sh")
       os.system("bash " + out + " > tes.sh")
       os.remove(out)
       os.system("mv -f tes.sh " + out)
       print (Encript + "Done..")

   except KeyboardInterrupt:
       print (Error + " Stopped!")
   except IOError:
       print (Error + " File Not Found!")

def enkrip():
   try:
       script = raw_input(ask + W + "Script " + G + "> " + W)
       output = raw_input(ask + W + "Output " + G + "> " + W)
       os.system("bash-obfuscate " + script + " -o " + output )
       print (Encript + "Done..")
   except KeyboardInterrupt:
       print (Error + " Stopped!")
   except IOError:
       print (Error + " File Not Found!")


takok = raw_input(W + "Choose" + G + " > ")

if takok == "1" or takok == "01":
   enkrip()
elif takok == "2" or takok == "02":
   dekrip()
else:
   print (Error + " Wrong input")
