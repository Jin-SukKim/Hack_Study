#!/bin/bash
if ["$1" == ""]
then
echo "You forgot an IP address!"
echo "Syntax: ./ipsweep.sh 192.168.1"

else
for ip in `seq 1 254`; do # go through sequence 1 to 254 and do something
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi # notice if clause is finished here

# ./ipsweep.sh 192.168.1 : how to use this script on shell
# check script file can be executed if not
# change it by chmod +x ipsweep.sh


# $1 is first argument as i understand
# $ip is ip value in for line