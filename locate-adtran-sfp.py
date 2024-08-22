#!/usr/local/bin python3

import paramiko
import sys
import time
import re
import pprint
import os
import subprocess
import getpass

#ipaddr = ["syd-kent-olt1","syd-livp-olt2"]
ipaddr = ["syd-boty-olt1",
          "nme-burn-olt1",
          "syd-kinc-olt1",
          "syd-kent-olt2",
          "syd-harr-olt1",
          "syd-bsar-olt1",
          "syd-carw-olt1",
          "syd-cona-olt1",
          "syd-geos-olt1",
          "syd-herb-olt1",
          "syd-holt-olt1",
          "syd-lach-olt1",
          "syd-wahr-olt1",
          "syd-walk-olt1",
          "nme-burn-olt1",
          "nme-coll-olt1",
          "nme-quee-olt1",
          "nme-stka-olt1",
          "bri-cann-olt1",
          "bri-mari-olt1",
          "bri-quen-olt1",
          "bri-redc-olt1",
          "bri-wick-olt1",
          "per-stgt-olt1"]

sfpserial = sys.argv[1]
uname = sys.argv[2]
passwd = getpass.getpass()
port = "22"
i = 0

for output in ipaddr:
  conn = paramiko.SSHClient()
  conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  conn.connect(ipaddr[i], port, uname, passwd,auth_timeout=60, banner_timeout=60)
  commands = conn.invoke_shell()
  commands.send("enable\n")
  commands.send(f"display ont info by-sn {sfpserial}"+"\n")
  time.sleep(5)
  output = commands.recv(65535) 
  output = output.decode("ascii")
  #print (output)
  with open (f"sfp-located.txt", 'w') as f:
   f.write(output)

  sfp_pattern = re.compile(r'SFP-Pattern')
  with open('sfp-located.txt','r') as rfile:
   output2 = rfile.read()
   sfp_pattern_matched = sfp_pattern.search(output2)
 
  sfp_matched = subprocess.check_output("cat sfp-located.txt | grep 'SN\|Description\|exist'", shell=True).decode(sys.stdout.encoding).strip()
  time.sleep(2)
  #print(sfp_matched)
  #print("\n\n")
  
  if "SN" in sfp_matched:
   print (str(i+1) + "." + (ipaddr[i])) 
   print(f"SFP located at:{sfp_matched}" +"\n")
   break
  elif "not" in sfp_matched:
   print (str(i+1) + "." + (ipaddr[i]))
   print(f"SFP located at:{sfp_matched}" +"\n") 
   i = i + 1
   f.close()
   conn.close()
  else:
   break

f.close()
conn.close()