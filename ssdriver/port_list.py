import os

pscmd = "netstat -ntl |grep -v Active| grep -v Proto|awk '{print $4}'|awk -F: '{print $NF}'"
procs = os.popen(pscmd).read()
procarr = procs.split("\n")
print procarr


