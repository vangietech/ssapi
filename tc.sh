#!/usr/bin/bash

tc qdisc del dev eth0 root
tc qdisc add dev eth0 root handle 1: htb default 12
tc class add dev eth0 parent 1: classid 1:1 htb rate 10Mbit burst 3000000
tc class add dev eth0 parent 1:1 classid 1:11  htb rate 2Kbit burst 150
tc qd add dev eth0 parent 1:11 handle 111: sfq
tc class add dev eth0 parent 1:1 classid 1:12  htb rate 2Mbit burst 1500000
tc qd add dev eth0 parent 1:12 handle 122: sfq
tc class add dev eth0 parent 1:1 classid 1:13  htb rate 7Mbit burst 3500000
tc qd add dev eth0 parent 1:13 handle 133: sfq
#Record example for del filter
#tc filter del dev eth0 parent 1: handle 800::800 protocol ip pref 1 u32
#tc filter add dev eth0 parent 1: prio 1 protocol ip u32 match ip sport 8443 0xffff flowid 1:11
#tc filter add dev eth0 parent 1: prio 1 protocol ip u32 match ip sport 8443 0xffff flowid 1:13



