#!/usr/bin/env python3

import sys

from server import startServer
from client import startClient
from keyGen import genNewKeys,genKeysForApk

if __name__ == "__main__":
    mode="none"
    port=-1
    args=sys.argv

    try:
        for index in range(1,len(args)):
            i=args[index]
            if i== "-h" or i=="--help":
                print("Použití: TYPE=[c|s] PORT=\"port number\"")
                exit(0)
            elif i== "-g" or i=="--genKeys":
                genKeysForApk()
                exit(0)
            else:
                strList=i.split('=')
                if len(strList)<2:
                    raise Exception("Chyba v parametrech, zkuste -h")
                
                name = strList[0]
                value= strList[1]        
                if name.upper()=='TYPE':
                    mode=value.lower()
                elif name.upper()=="PORT":
                    port = int(value)
                elif name.upper()=="GEN":
                    genNewKeys(value)
                    exit(0)
                else:
                    raise Exception("Chyba v parametrech, zkuste -h")
                
        if port<0 or port>65535:
            raise Exception("Port služby je špatně zadán")
    except Exception as ex:
        print("Error:",ex)
    if mode=="c":
        startClient(port)
    elif mode=="s":
        startServer(port)
    else:
        raise Exception("Mód zpuštění je špatně zadán")