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

# some helpful urls
# https://github.com/Naetw/CTF-pwn-tips
# http://ctfhacker.com/ctf/pwnable/2015/08/18/campctf-bitterman.html
# https://github.com/nnamon/linux-exploitation-course

# some certain helpful pwntools commands

# system_off = libc.symbols['system']
# binsh = next(libc.search('/bin/sh\\x00'))
# rop2.system(next(libc.search('/bin/sh\\x00'))) and print rop2.dump()

# elf = ELF('./binary')
# rop = ROP(elf)
# rop.puts(elf.got['puts'])
# rop.call(elf.symbols['main'])

from pwn import *
import sys
#context(arch='amd64', os='linux', endian='little')
#http://docs.pwntools.com/en/stable/context.html?highlight=context#pwnlib.context.ContextType.architectures
LOCAL = True

'''
    
    code3='''
def exploit(r):

    r.interactive()
    return

if __name__=="__main__":
    #binary = ELF(BINARY, checksec = False)
    #lib = ELF(LIB, checksec = False)
    #rop = ROP(lib)

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
