import getopt
import sys

import mcpfw_rest
import requests
import json

#mcp_command.py -c disks -s kime-win2016
hostname = "http://kime-win2016:"
portNum = '53210'
desiredMemorySize = 77
payload = {'DesiredMcpMemoryMW':str(desiredMemorySize)}
command = 'settings'
url = hostname + portNum + "/mcpfirmware/"+ command
print(url)
#command_resp = requests.put("http://kime-win2016:53210/mcpfirmware/settings",json=payload)
command_resp = requests.put(url, json=payload)

print("rslt:", command_resp)

if command_resp.status_code == requests.codes.ok:
    print("It worked!")
    print('{0} command accepted.'.format('settings'))
else:
    print('Error! :', command_resp)

cmd_resp = requests.get(url).json()
print("rslt: ", cmd_resp)

print(cmd_resp['DesiredMcpMemoryMW'])
if desiredMemorySize == cmd_resp['DesiredMcpMemoryMW']:
    print("Test passed!!!")
else:
    print("Test failed!!")
