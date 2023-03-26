#!/bin/bash

for i in {1..254};
do (ping -c 1 10.12.176.$i | grep "bytes from" &)
done;
