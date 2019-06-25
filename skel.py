#
# Quick'n dirty exploit template by @_hugsy_
# Modified for my own @iamalsaher
# Load with:
# gef> source /path/to/skel.py
#
# Use with
# gef> xpl
# gef> xpl host:port
#

import os, tempfile

TEMPLATE="""#!/usr/bin/env python2
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

#http://docs.pwntools.com/en/stable/context.html?highlight=context#pwnlib.context.ContextType.architectures

import sys,os
from pwn import *

context.update(arch="{arch}", endian="{endian}", os="linux", )

LOCAL = True
HOST="{host}"
PORT={port}

TARGET=os.path.realpath("{filepath}")
LIBRARY=""

e = ELF(TARGET, False)
# l = ELF(LIBRARY, False)

def exploit(r):

    r.interactive()
    payload=""
    payload+=""
    r.sendline(payload)
    return

if __name__ == "__main__":

    if len(sys.argv) > 1:
        LOCAL = False
        r = remote(HOST, PORT)
    else:
        LOCAL = True
        r = process([TARGET,])#,env={{'LD_PRELOAD':LIB}}) #remove the ')#'
        pause()

    exploit(r)

    sys.exit(0)
"""

class ExploitTemplateCommand(GenericCommand):
    """Generates a exploit template."""
    _cmdline_ = "exploit-template"
    _syntax_  = "{:s} optional [TARGET:PORT]".format(_cmdline_)
    _aliases_ = ["skel","xpl", ]

    def do_invoke(self, args):

        host, port = "127.0.0.1", "1337"
        if args:
            target, port = args[0].split(":")
        
        fname = open("xploit_{}.py".format(get_filepath().split('/')[-1]),'w')
        temp = TEMPLATE.format(host=host,
                               port=port,
                               arch="amd64" if "x86-64" in get_arch() else "i386",
                               endian="big" if is_big_endian() else "little",
                               filepath=get_filepath().split('/')[-1])
        fname.write(temp)
        fname.close()
        ok("Exploit template generated")
        return


if __name__ == "__main__":
    register_external_command( ExploitTemplateCommand() )
