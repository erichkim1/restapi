import getopt
import sys

import mcpfw_rest
import requests
import json

#mcp_command.py -c disks -s kime-win2016
hostname = 'http://kime-win2016'
portNum = '53210'
desiredMemorySize = '78'
payload = {'DesiredMcpMemoryMW':desiredMemorySize}
command_resp = requests.put("http://kime-win2016:53210/mcpfirmware/settings",json=payload)

print("rslt:", command_resp)

if command_resp.status_code == requests.codes.ok:
    print("It worked!")
    print('{0} command accepted.'.format('settings'))
else:
    print('Error! :', command_resp)

cmd_resp = requests.get("http://kime-win2016:53210/mcpfirmware/settings").json()
print("rslt: ", cmd_resp)

print(cmd_resp['DesiredMcpMemoryMW'])
