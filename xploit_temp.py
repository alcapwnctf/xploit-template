#!/usr/bin/python3
import argparse
import os


def args_main():
    """
    Argument parsing function
    :return:
    """

    parser = argparse.ArgumentParser(description='Pwntools template')

    # Parse Arguments
    parser.add_argument('-r', help='Remote hostname/IP for the challenge', metavar='remote-host', default='127.0.0.1')
    parser.add_argument('-p', help='Remote port for the challenge', metavar='remote-port', default=1337)
    args = parser.parse_args()  

    return args


if __name__=="__main__":
    code='''#!/usr/bin/python2
from pwn import *
import sys

LOCAL = True

'''
    
    code3='''
def exploit(r):

    r.interactive()
    return

if __name__=="__main__":
    #binary = ELF(BINARY, checksec = False)
    #lib = ELF(LIB, checksec = False)
    if len(sys.argv) > 1:
        LOCAL = False
        r = remote(HOST, PORT)
        exploit(r)
    else:
        LOCAL = True
        r = process(BINARY)#,env={'LD_PRELOAD':LIB}) #remove the ')#'
        print (util.proc.pidof(r))
        pause()
        exploit(r)'''

    cwd = os.getcwd()
    ch = input("The current directory is " + cwd + "\nDo you want to continue?[y/n]")
    
    lib=''
    if ch == 'y' or ch == 'Y':
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            if f[-3:]=='.so':lib = './'+f
            if '.'not in f: 
                binary = f
                break
        
        args=args_main()
        
        code2='''HOST = "{}"\nPORT = {}\nBINARY = "./{}"\nLIB = "{}"'''.format(args.r, args.p, binary,lib)
        
        f=open('xploit.py','w')
        f.write(code+code2+code3)
        f.close()
    
    else:
        print ("Please run the program from right directory")
